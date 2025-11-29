    # Write output file
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(template_content)
        print(f"Successfully generated {output_file}")
    except Exception as e:
        print(f"Error writing output file: {e}")