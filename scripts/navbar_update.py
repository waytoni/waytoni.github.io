# build.py
from bs4 import BeautifulSoup
import os

class StaticSiteBuilder:
    def __init__(self, template_dir='scripts/templates'):
        self.template_dir = template_dir
        self.components = self.load_components()
    
    def load_components(self):
        """Load all template components"""
        components = {}
        component_files = {
            'navbar': 'navigation_header_template.html',
            #'header': 'header.html',  # Optional
            #'footer': 'footer.html',  # Optional
            #'sidebar': 'sidebar.html' # Optional
        }
        
        for name, filename in component_files.items():
            filepath = os.path.join(self.template_dir, filename)
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    components[name] = f.read()
                print(f"✓ Loaded component: {name}")
            else:
                print(f"⚠ Component not found: {filename}")
        
        return components
    
    def update_single_file(self, html_file, components_to_update=None):
        """
        Update specific components in a single HTML file
        
        Args:
            html_file: Path to HTML file to update
            components_to_update: List of component names to update
                                 If None, updates all available components
        """
        if not os.path.exists(html_file):
            print(f"✗ File not found: {html_file}")
            return False
        
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')
            
            #print(soup.title.string)
            
            updated = False
            components_to_update = components_to_update or list(self.components.keys())
            
            # print(components_to_update)
            
            # Update navbar if specified and available
            if 'navbar' in components_to_update and 'navbar' in self.components:
                
                navbar_div = soup.find('div', {'class': 'topnav', 'id': 'Topnavbar'})
                
                # print(navbar_div)
                
                if navbar_div:
                    navbar_div.clear()
                    navbar_div.append(BeautifulSoup(self.components['navbar'], 'html.parser'))
                    updated = True
                    print(f"  ✓ Updated navbar in {html_file}")
                else:
                    print(f"  ⚠ Navbar div not found in {html_file}")
            
            # Update footer if specified and available
            if 'footer' in components_to_update and 'footer' in self.components:
                # Find footer by ID, class, or tag
                footer_div = (soup.find('div', {'id': 'footer'}) or 
                            soup.find('footer') or 
                            soup.find('div', {'class': 'footer'}))
                if footer_div:
                    footer_div.clear()
                    footer_div.append(BeautifulSoup(self.components['footer'], 'html.parser'))
                    updated = True
                    print(f"  ✓ Updated footer in {html_file}")
            
            # Update header if specified and available
            if 'header' in components_to_update and 'header' in self.components:
                header_div = soup.find('div', {'id': 'header'})
                if header_div:
                    header_div.clear()
                    header_div.append(BeautifulSoup(self.components['header'], 'html.parser'))
                    updated = True
                    print(f"  ✓ Updated header in {html_file}")
            
            # Save if any updates were made
            if updated:
                new_content = soup.prettify()
                with open(html_file, 'w', encoding='utf-8') as f:
                #   f.write(str(soup))
                    f.write(new_content)
                return True
            else:
                print(f"  ⚠ No components updated in {html_file}")
                return False
                
        except Exception as e:
            print(f"✗ Error processing {html_file}: {str(e)}")
            return False
    
    def update_files(self, file_list, components_to_update=None):
        """
        Update specific components in a list of HTML files
        
        Args:
            file_list: List of file paths to update
            components_to_update: List of component names to update
        """
        print(f"\nUpdating {len(file_list)} file(s)...")
        print("-" * 40)
        
        successful = 0
        for file_path in file_list:
            print(f"\nProcessing: {file_path}")
            if self.update_single_file(file_path, components_to_update):
                successful += 1
        
        print(f"\n{'=' * 40}")
        print(f"Summary: {successful}/{len(file_list)} files updated successfully")
        return successful



class SmartSiteBuilder:
    def __init__(self, template_dir='scripts/templates', indent_size=2):
        self.template_dir = template_dir
        self.indent_size = indent_size
        self.components = self.load_components()
    
    def load_components(self):
        components = {}
        for component in ['navbar', 'footer', 'header']:
            filepath = os.path.join(self.template_dir, f'{component}_template.html')
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    components[component] = f.read().strip()
        return components
    
    def update_file_smart(self, html_file):
        """Smart update that preserves surrounding formatting"""
        with open(html_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        updated_lines = []
        in_navbar = False
        navbar_indent = 0
        updated = False
        
        for i, line in enumerate(lines):
            # Check if this line starts the navbar div
            if 'class="topnav"' in line and 'id="Topnavbar"' in line:
                in_navbar = True
                updated = True
                
                # Calculate current indentation
                navbar_indent = len(line) - len(line.lstrip())
                indent = ' ' * navbar_indent
                
                # Add the opening div tag
                updated_lines.append(line.rstrip('\n'))
                
                # Add the new navbar content with proper indentation
                if 'navbar' in self.components:
                    navbar_lines = self.components['navbar'].split('\n')
                    for nav_line in navbar_lines:
                        if nav_line.strip():  # Skip empty lines
                            updated_lines.append(indent + '  ' + nav_line)
                
                # Skip original navbar content until we find the closing div
                continue
            
            # Skip lines until we find the closing div for navbar
            if in_navbar:
                if line.strip().startswith('</div>'):
                    in_navbar = False
                    # Add closing div with original indentation
                    updated_lines.append(' ' * navbar_indent + '</div>')
                continue
            
            # Process footer similarly
            if any(tag in line for tag in ['id="footer"', '<footer', 'class="footer"']):
                # Similar logic for footer...
                pass
            else:
                updated_lines.append(line.rstrip('\n'))
        
        if updated:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(updated_lines))
        
        return updated


# Usage Example 1: Update specific files
if __name__ == "__main__":
    # Initialize builder
    builderOld = StaticSiteBuilder('scripts/templates')
    builder = SmartSiteBuilder('scripts/templates')
    
    # Define your list of files to update
    files_to_update = [
   
        'ChiththaChithasika/index.html', 

        # The following files are updated using gen_navbar_replace script 
        #'Anichcha_Dukka_Anathma_Series/Anichcha_Dukka_Anathma.html', 
        #'Paramartha_Video/Paramartha_Video.html',
        
        # The following files are updated using load-template.js script
        # Paramartha_Video/ParamarthaDarama.html
        # 404.html
        # 'KalutaraBodhiya/B_C_D_Batches.html',
    ]
    
    # Option 1: Update only navbar in all specified files
    print("=== Updating Navbar Only ===")
    builderOld.update_files(files_to_update, components_to_update=['navbar'])
    
    #for html_file in files_to_update:
    #    builder.update_file_smart(html_file)
    
    # Option 2: Update navbar and footer
    #print("\n=== Updating Navbar and Footer ===")
    #builder.update_files(files_to_update, components_to_update=['navbar', 'footer'])
    
    # Option 3: Update all available components
    #print("\n=== Updating All Components ===")
    #builder.update_files(files_to_update)  # Updates all available components