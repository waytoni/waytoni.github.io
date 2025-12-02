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

# Usage Example 1: Update specific files
if __name__ == "__main__":
    # Initialize builder
    builder = StaticSiteBuilder('scripts/templates')
    
    # Define your list of files to update
    files_to_update = [
        #'index.html',
        'Anichcha_Dukka_Anathma_Series/Anichcha_Dukka_Anathma.html', 
        'KalutaraBodhiya/B_C_D_Batches.html',
        'Paramartha_Video/Paramartha_Video.html',
        'ChiththaChithasika/index.html', 
        '404.html',
    ]
    
    # Option 1: Update only navbar in all specified files
    print("=== Updating Navbar Only ===")
    builder.update_files(files_to_update, components_to_update=['navbar'])
    
    # Option 2: Update navbar and footer
    #print("\n=== Updating Navbar and Footer ===")
    #builder.update_files(files_to_update, components_to_update=['navbar', 'footer'])
    
    # Option 3: Update all available components
    #print("\n=== Updating All Components ===")
    #builder.update_files(files_to_update)  # Updates all available components