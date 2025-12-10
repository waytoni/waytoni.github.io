def generate_html_from_template(template_filename):
    """
    Read a template file and replace placeholders with content.
    
    Args:
        template_filename: Name of the template file in scripts/templates folder
        
    Returns:
        The processed HTML content with placeholders replaced
    """
    # Read the main template
    template_path = f"scripts/templates/{template_filename}"
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Read the navigation header template
    nav_header_path = "scripts/templates/navigation_header_template.html"
    with open(nav_header_path, 'r', encoding='utf-8') as f:
        nav_header = f.read()
    
    # Replace placeholder
    content = content.replace("$NAVIGATION_HEADER$", nav_header)
    
    return content


if __name__ == "__main__":
    # Generate HTML from template
    
    # Anichcha Dukka Anaththa Series 
    html_content = generate_html_from_template("ADA_template.html")
    output_path = "Anichcha_Dukka_Anathma_Series/Anichcha_Dukka_Anathma.html"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generated {output_path}")
    
    
    # Paramartha Video 
    html_content = generate_html_from_template("Paramartha_Video_template.html")
    output_path = "Paramartha_Video/Paramartha_Video.html"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generated {output_path}")
    
    # Chiththa Chithasika Chart
    html_content = generate_html_from_template("ChiththaChithasika_template.html")
    output_path = "ChiththaChithasika/index.html"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generated {output_path}")