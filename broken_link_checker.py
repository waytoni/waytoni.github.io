import os
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import concurrent.futures
from pathlib import Path
import time
import sys

class BrokenLinkChecker:
    def __init__(self, base_url=None, local_path=None, max_workers=10, timeout=10):
        """
        Initialize the link checker
        
        Args:
            base_url: Online URL of the website (optional)
            local_path: Path to local website files
            max_workers: Number of concurrent workers
            timeout: Request timeout in seconds
        """
        self.base_url = base_url
        self.local_path = local_path
        self.max_workers = max_workers
        self.timeout = timeout
        
        # Store all found links
        self.visited_links = set()
        self.broken_links = []
        self.valid_links = []
        
        # Session for persistent connections
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def is_valid_url(self, url):
        """Check if URL is valid for testing"""
        parsed = urlparse(url)
        return bool(parsed.netloc) or bool(parsed.path)
    
    def normalize_url(self, url, base_url):
        """Normalize URL to absolute form"""
        if not url:
            return None
        
        # Handle fragment links
        if url.startswith('#'):
            return None
        
        # Handle mailto, tel, javascript links
        if url.startswith(('mailto:', 'tel:', 'javascript:', 'ftp:')):
            return None
        
        # Convert to absolute URL
        if not url.startswith(('http://', 'https://', '//')):
            if self.local_path and os.path.exists(os.path.join(self.local_path, url.lstrip('/'))):
                return url
            url = urljoin(base_url, url)
        
        # Remove fragments
        parsed = urlparse(url)
        return parsed.scheme + '://' + parsed.netloc + parsed.path if parsed.scheme else url
    
    def check_local_file(self, file_path):
        """Extract links from a local HTML file"""
        links = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            soup = BeautifulSoup(content, 'html.parser')
            
            # Find all links
            for tag in soup.find_all(['a', 'img', 'link', 'script']):
                if tag.name == 'a':
                    href = tag.get('href')
                    if href:
                        links.append(href)
                elif tag.name == 'img':
                    src = tag.get('src')
                    if src:
                        links.append(src)
                elif tag.name == 'link':
                    href = tag.get('href')
                    if href:
                        links.append(href)
                elif tag.name == 'script':
                    src = tag.get('src')
                    if src:
                        links.append(src)
                        
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
        
        return links
    
    def check_url(self, url):
        """Check if a URL is accessible"""
        try:
            # Handle local files
            if self.local_path and not url.startswith(('http://', 'https://')):
                local_file = os.path.join(self.local_path, url.lstrip('/'))
                if os.path.exists(local_file):
                    return True, url, 200
                else:
                    return False, url, 404
            
            # Handle online URLs
            response = self.session.head(url, timeout=self.timeout, allow_redirects=True)
            
            # Some servers don't allow HEAD, try GET if HEAD fails
            if response.status_code == 405:
                response = self.session.get(url, timeout=self.timeout, stream=True)
            
            is_valid = response.status_code < 400
            return is_valid, url, response.status_code
            
        except requests.exceptions.RequestException as e:
            return False, url, str(e)
        except Exception as e:
            return False, url, str(e)
    
    def crawl_local_site(self):
        """Crawl local website directory to find all HTML files and links"""
        if not self.local_path:
            return []
        
        all_links = []
        html_files = []
        
        # Find all HTML files
        for root, dirs, files in os.walk(self.local_path):
            for file in files:
                if file.endswith(('.html', '.htm')):
                    html_files.append(os.path.join(root, file))
        
        print(f"Found {len(html_files)} HTML files")
        
        # Extract links from each HTML file
        for html_file in html_files:
            relative_path = os.path.relpath(html_file, self.local_path)
            
            # Get base URL for this file (for relative link resolution)
            if self.base_url:
                file_base_url = urljoin(self.base_url, relative_path.replace('\\', '/'))
            else:
                file_base_url = 'file://' + relative_path
            
            links = self.check_local_file(html_file)
            
            for link in links:
                normalized = self.normalize_url(link, file_base_url)
                if normalized and normalized not in self.visited_links:
                    all_links.append(normalized)
                    self.visited_links.add(normalized)
        
        return all_links
    
    def crawl_online_site(self, start_url):
        """Crawl online website starting from given URL"""
        # This is a simplified version. For full crawling, you'd need to handle
        # same-domain restriction, robots.txt, etc.
        try:
            response = self.session.get(start_url, timeout=self.timeout)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            links = []
            for tag in soup.find_all('a'):
                href = tag.get('href')
                if href:
                    normalized = self.normalize_url(href, start_url)
                    if normalized and normalized not in self.visited_links:
                        links.append(normalized)
                        self.visited_links.add(normalized)
            
            return links
        except Exception as e:
            print(f"Error crawling {start_url}: {e}")
            return []
    
    def check_links(self, links):
        """Check multiple links concurrently"""
        print(f"\nChecking {len(links)} links...")
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_url = {executor.submit(self.check_url, url): url for url in links}
            
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    is_valid, checked_url, status = future.result()
                    
                    if is_valid:
                        self.valid_links.append((checked_url, status))
                        print(f"✓ {checked_url} - {status}")
                    else:
                        self.broken_links.append((checked_url, status))
                        print(f"✗ {checked_url} - {status}")
                        
                except Exception as e:
                    self.broken_links.append((url, str(e)))
                    print(f"✗ {url} - ERROR: {e}")
    
    def generate_report(self):
        """Generate a summary report"""
        report = []
        report.append("=" * 60)
        report.append("BROKEN LINK CHECKER REPORT")
        report.append("=" * 60)
        report.append(f"\nTotal links checked: {len(self.visited_links)}")
        report.append(f"Valid links: {len(self.valid_links)}")
        report.append(f"Broken links: {len(self.broken_links)}")
        
        if self.broken_links:
            report.append("\nBROKEN LINKS:")
            report.append("-" * 40)
            for url, status in self.broken_links:
                report.append(f"URL: {url}")
                report.append(f"Status/Error: {status}")
                report.append("-" * 20)
        
        report.append("\nSUMMARY:")
        report.append("-" * 40)
        report.append(f"Success rate: {(len(self.valid_links)/len(self.visited_links)*100):.1f}%")
        
        return "\n".join(report)
    
    def save_results(self, filename="broken_links_report.txt"):
        """Save results to a file"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(self.generate_report())
        print(f"\nReport saved to {filename}")
    
    def run_local_check(self):
        """Run link check on local website files"""
        if not self.local_path:
            print("No local path specified!")
            return
        
        print(f"Starting local link check on: {self.local_path}")
        
        # Find all links in local HTML files
        links = self.crawl_local_site()
        
        if not links:
            print("No links found in local files")
            return
        
        # Check all found links
        self.check_links(links)
        
        # Generate and display report
        print("\n" + self.generate_report())
        
        # Save results
        self.save_results("local_broken_links_report.txt")

def main():
    """Main function to run the link checker"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Check for broken links in a website')
    parser.add_argument('--local', type=str, help='Path to local website files')
    parser.add_argument('--url', type=str, help='Online URL of the website')
    parser.add_argument('--workers', type=int, default=10, help='Number of concurrent workers')
    parser.add_argument('--timeout', type=int, default=10, help='Request timeout in seconds')
    
    args = parser.parse_args()
    
    if not args.local and not args.url:
        print("Please specify either --local or --url option")
        parser.print_help()
        sys.exit(1)
    
    # Create checker instance
    checker = BrokenLinkChecker(
        base_url=args.url,
        local_path=args.local,
        max_workers=args.workers,
        timeout=args.timeout
    )
    
    # Run checks
    if args.local:
        checker.run_local_check()
    
    # You could add online checking here if needed
    # if args.url and not args.local:
    #     checker.run_online_check(args.url)

if __name__ == "__main__":
    main()