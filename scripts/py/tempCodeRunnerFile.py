    for pdf_file in pdf_dir.glob('*.pdf'):
        print(pdf_file)
        if search_pdf_for_terms(pdf_file, search_terms):
            matching_files.append(pdf_file.name)