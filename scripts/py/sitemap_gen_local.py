import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse
from pathlib import Path
import xml.etree.ElementTree as ET
from datetime import datetime
import time
from collections import deque
import argparse
import stat

class SitemapGenerator:
    def __init__(self, base_url=None, max_urls=100, delay=1, user_agent=None, 
                 skip_dirs=None, local_path='.'):
        self.local_mode = base_url is None
        self.max_urls = max_urls
        self.delay = delay
        self.visited_urls = set()
        self.to_visit = deque()
        self.all_urls = set()
        self.skip_dirs = set(skip_dirs) if skip_dirs else {
            'testing', 'test', 'temp', 'tmp', 'node_modules', '.git', 
            '.vscode', '.idea', '__pycache__', 'vendor', 'cache',
            'logs', 'backup', 'private', 'secret'
        }
        self.local_path = Path(local_path).resolve()
        
        if self.local_mode:
            # Local file system mode
            self.base_url = f"file://{self.local_path}"
            # Start with the local path if we have permission
            if self.has_read_permission(self.local_path):
                self.to_visit.append(str(self.local_path))
            else:
                print(f"Warning: No read permission for {self.local_path}")
        else:
            # Web mode
            self.base_url = base_url.rstrip('/')
            self.to_visit.append(base_url)
            self.session = requests.Session()
            if user_agent:
                self.session.headers.update({'User-Agent': user_agent})
            else:
                self.session.headers.update({
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                })
    
    def has_read_permission(self, path):
        """Check if we have read permission for a path"""
        try:
            # Try to access the path
            if path.is_file():
                with open(path, 'rb') as f:
                    pass
            else:
                # For directories, try to list contents
                next(path.iterdir(), None)
            return True
        except PermissionError:
            return False
        except Exception:
            return False
    
    def should_skip_path(self, path):
        """Check if path should be skipped based on directory patterns"""
        try:
            path_str = str(path).lower()
            path_parts = path_str.split('/')
            
            # Skip hidden directories (starting with .)
            if any(part.startswith('.') for part in path_parts):
                return True
                
            # Skip specific directories
            for skip_dir in self.skip_dirs:
                if skip_dir.lower() in path_parts:
                    return True
                    
            return False
        except Exception:
            return True
    
    def is_valid_url(self, url):
        """Check if URL is valid and should be included"""
        if self.local_mode:
            try:
                local_path = Path(url)
                if not local_path.exists():
                    return False
                    
                # Check permissions
                if not self.has_read_permission(local_path):
                    return False
                    
                # Skip problematic paths
                if self.should_skip_path(local_path.relative_to(self.local_path)):
                    return False
                    
                if local_path.is_file():
                    return local_path.suffix.lower() in ['.html', '.htm', '.php', '.asp', '.aspx', '']
                return local_path.is_dir()
                
            except Exception:
                return False
        else:
            # Web mode checks
            parsed_url = urlparse(url)
            parsed_base = urlparse(self.base_url)
            
            # Only crawl same domain
            if parsed_url.netloc != parsed_base.netloc:
                return False
            
            # Skip common non-page extensions
            skip_extensions = [ '.jpg', '.jpeg', '.png', '.gif', '.zip', '.exe', '.css', '.js']
            if any(url.lower().endswith(ext) for ext in skip_extensions):
                return False
                
            return True
    
    def safe_iterdir(self, directory):
        """Safely iterate through directory contents"""
        try:
            if not self.has_read_permission(directory):
                return []
            return list(directory.iterdir())
        except PermissionError:
            print(f"Permission denied accessing: {directory}")
            return []
        except Exception as e:
            print(f"Error accessing {directory}: {e}")
            return []
    
    def discover_local_files(self, directory):
        """Discover HTML files in local directory safely"""
        html_files = []
        directory = Path(directory)
        
        if not directory.exists() or not directory.is_dir():
            return html_files
        
        try:
            for file_path in directory.rglob('*'):
                try:
                    if not file_path.exists():
                        continue
                        
                    # Skip if no read permission
                    if not self.has_read_permission(file_path):
                        continue
                        
                    # Skip problematic paths
                    rel_path = file_path.relative_to(self.local_path)
                    if self.should_skip_path(rel_path):
                        continue
                        
                    if file_path.is_file() and file_path.suffix.lower() in ['.html', '.htm']:
                        html_files.append(str(file_path))
                        
                except PermissionError:
                    continue
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
                    continue
                    
        except PermissionError:
            print(f"Permission denied traversing: {directory}")
        except Exception as e:
            print(f"Error traversing {directory}: {e}")
        
        return html_files
    
    def extract_links_local(self, file_path):
        """Extract links from local HTML file with error handling"""
        try:
            file_path = Path(file_path)
            
            # Check if it's a directory (look for index files)
            if file_path.is_dir():
                for index_file in ['index.html', 'index.htm', 'default.html']:
                    index_path = file_path / index_file
                    if index_path.exists() and self.has_read_permission(index_path):
                        return self.extract_links_local(str(index_path))
                return [], str(file_path)
            
            # Check permissions
            if not self.has_read_permission(file_path):
                return [], str(file_path)
            
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            soup = BeautifulSoup(content, 'html.parser')
            links = []
            
            for link in soup.find_all('a', href=True):
                href = link['href']
                
                # Skip external links in local mode
                if href.startswith(('http://', 'https://', '//', 'mailto:', 'tel:')):
                    continue
                
                # Handle absolute and relative paths
                if href.startswith('/'):
                    # Root-relative path
                    abs_path = self.local_path / href[1:]
                else:
                    # Relative path
                    current_dir = file_path.parent
                    abs_path = (current_dir / href).resolve()
                
                # Normalize path and ensure it's within our root
                try:
                    abs_path = abs_path.resolve()
                    rel_to_root = abs_path.relative_to(self.local_path)
                except (ValueError, RuntimeError):
                    # Path outside our root directory
                    continue
                
                # Check if path should be skipped
                if self.should_skip_path(rel_to_root):
                    continue
                
                # Check if path exists and we have permission
                if abs_path.exists() and self.has_read_permission(abs_path):
                    if abs_path.is_file() and abs_path.suffix.lower() in ['.html', '.htm']:
                        links.append(str(abs_path))
                    elif abs_path.is_dir():
                        # Check for index files in directory
                        for index_file in ['index.html', 'index.htm']:
                            index_path = abs_path / index_file
                            if index_path.exists() and self.has_read_permission(index_path):
                                links.append(str(index_path))
                                break
            
            return links, str(file_path)
            
        except PermissionError:
            print(f"Permission denied reading: {file_path}")
            return [], str(file_path)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return [], str(file_path)
    
    def extract_links_web(self, url):
        """Extract links from web page"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            links = []
            
            for link in soup.find_all('a', href=True):
                href = link['href']
                full_url = urljoin(url, href)
                
                # Clean URL - remove fragments
                full_url = full_url.split('#')[0]
                
                if self.is_valid_url(full_url):
                    links.append(full_url)
            
            return links, response.url
            
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return [], url
    
    def crawl(self):
        """Crawl the website to discover all URLs"""
        print(f"Starting {'local' if self.local_mode else 'web'} crawl")
        if self.local_mode:
            print(f"Local path: {self.local_path}")
            print(f"Checking read permissions...")
        else:
            print(f"Base URL: {self.base_url}")
        print(f"Maximum URLs to crawl: {self.max_urls}")
        print(f"Skipping directories: {', '.join(sorted(self.skip_dirs))}")
        print("-" * 50)
        
        while self.to_visit and len(self.all_urls) < self.max_urls:
            current_url = self.to_visit.popleft()
            
            if current_url in self.visited_urls:
                continue
                
            print(f"Crawling: {current_url}")
            
            if self.local_mode:
                links, final_url = self.extract_links_local(current_url)
            else:
                links, final_url = self.extract_links_web(current_url)
            
            self.visited_urls.add(current_url)
            
            # Convert local paths to web-style URLs for sitemap
            if self.local_mode:
                try:
                    file_path = Path(final_url)
                    if file_path.exists():
                        rel_path = file_path.relative_to(self.local_path)
                        web_url = f"/{rel_path.as_posix()}"
                        # For directories, use the directory name
                        if file_path.is_dir():
                            web_url = web_url.rstrip('/')
                        self.all_urls.add(web_url)
                except Exception as e:
                    print(f"Error processing path {final_url}: {e}")
            else:
                self.all_urls.add(final_url)
            
            # Add new links to the queue
            for link in links:
                if link not in self.visited_urls and link not in self.to_visit:
                    self.to_visit.append(link)
            
            # Respect the delay for web mode
            if not self.local_mode:
                time.sleep(self.delay)
        
        print("-" * 50)
        print(f"Crawl completed. Found {len(self.all_urls)} URLs.")
    
    def generate_sitemap(self, output_file='sitemap.xml', base_domain='https://waytoni.com'):
        """Generate the sitemap.xml file"""
        if not self.all_urls:
            print("No URLs found. Please run crawl() first.")
            return
        
        # Create XML structure
        urlset = ET.Element('urlset')
        urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
        
        for url in sorted(self.all_urls):
            url_element = ET.SubElement(urlset, 'url')
            
            loc = ET.SubElement(url_element, 'loc')
            # Convert local paths to full URLs
            if self.local_mode and not url.startswith(('http://', 'https://')):
                if url.startswith('/'):
                    full_url = base_domain.rstrip('/') + url
                else:
                    full_url = base_domain.rstrip('/') + '/' + url
                loc.text = full_url
            else:
                loc.text = url
            
            lastmod = ET.SubElement(url_element, 'lastmod')
            if self.local_mode:
                # Get file modification time for local files
                try:
                    local_path = self.local_path / url.lstrip('/')
                    if local_path.exists() and self.has_read_permission(local_path):
                        mtime = local_path.stat().st_mtime
                        lastmod.text = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
                    else:
                        lastmod.text = datetime.now().strftime('%Y-%m-%d')
                except:
                    lastmod.text = datetime.now().strftime('%Y-%m-%d')
            else:
                lastmod.text = datetime.now().strftime('%Y-%m-%d')
            
            changefreq = ET.SubElement(url_element, 'changefreq')
            changefreq.text = 'weekly'
            
            priority = ET.SubElement(url_element, 'priority')
            # Higher priority for root and important pages
            url_str = str(url).lower()
            if url_str in ['/', '/index.html', 'index.html', '/index.htm']:
                priority.text = '1.0'
            elif any(url_str.startswith(prefix) for prefix in ['/about', '/contact', '/services', '/products']):
                priority.text = '0.9'
            else:
                priority.text = '0.8'
        
        # Create XML tree and write to file
        tree = ET.ElementTree(urlset)
        try:
            with open(output_file, 'wb') as f:
                tree.write(f, encoding='utf-8', xml_declaration=True)
            
            print(f"Sitemap generated: {output_file}")
            print(f"Total URLs in sitemap: {len(self.all_urls)}")
        except PermissionError:
            print(f"Error: Permission denied writing to {output_file}")
            print("Try running with a different output filename or location")
        except Exception as e:
            print(f"Error writing sitemap: {e}")

def main():
    parser = argparse.ArgumentParser(description='Generate sitemap.xml for a website')
    parser.add_argument('--url', help='Base URL of the website to crawl (for web mode)')
    parser.add_argument('--local', action='store_true', 
                       help='Run in local mode (crawl local filesystem)')
    parser.add_argument('--local-path', default='.', 
                       help='Local directory to crawl (default: current directory)')
    parser.add_argument('-o', '--output', default='sitemap.xml', 
                       help='Output filename (default: sitemap.xml)')
    parser.add_argument('-m', '--max-urls', type=int, default=500,
                       help='Maximum number of URLs to crawl (default: 500)')
    parser.add_argument('-d', '--delay', type=float, default=1,
                       help='Delay between requests in seconds (web mode only, default: 1)')
    parser.add_argument('--user-agent', help='Custom User-Agent string (web mode only)')
    parser.add_argument('--base-domain', default='https://waytoni.com',
                       help='Base domain for local mode URLs (default: https://waytoni.com)')
    parser.add_argument('--skip-dirs', nargs='+', 
                       default=['testing', 'working', '.github', '.idea', 'scripts', '.git', '.vscode'],
                       help='Directories to skip (default: testing working .githun .idea scripts .git .vscode)')
    parser.add_argument('--skip-permission-errors', action='store_true',
                       help='Skip files and directories with permission errors')
    
    args = parser.parse_args()
    
    if args.local:
        # Local mode
        generator = SitemapGenerator(
            local_path=args.local_path,
            max_urls=args.max_urls,
            skip_dirs=args.skip_dirs
        )
    else:
        # Web mode
        if not args.url:
            parser.error("Either --url or --local must be specified")
        
        # Validate URL
        if not args.url.startswith(('http://', 'https://')):
            args.url = 'https://' + args.url
        
        generator = SitemapGenerator(
            base_url=args.url,
            max_urls=args.max_urls,
            delay=args.delay,
            user_agent=args.user_agent,
            skip_dirs=args.skip_dirs
        )
    
    generator.crawl()
    generator.generate_sitemap(args.output, args.base_domain)

if __name__ == "__main__":
    main()