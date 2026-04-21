#!/usr/bin/env python
# -*- coding: utf-8 -*-
# markdown_to_other_format.py created at 09-10-2023 by Abhay Kumar
"""
Module desciption: 
Description of what markdown_to_other_format.py does.

Usage:
    python markdown_to_other_format.py -i <input_markdown_file> -o <output_directory>

    Directly run the script from the command line with the input markdown file and output directory as arguments.
    > pandoc resume/resume.md -o resume/other_formats/resume.docx
"""

import argparse
from datetime import datetime
import os
from pathlib import Path

import pypandoc
import markdown2


def insert_style(html_content):
    # Create HTML content with Georgia font enforced
    html_with_georgia_font = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{
                     font-family: Georgia, serif;
                     letter-spacing: 1px;
                }}
            </style>
        </head>
        <body>
        {html_content}
        </body>
        </html>
        """
    return html_with_georgia_font


def markdown_to_html(markdown_file):
    # Convert Markdown to HTML
    with open(markdown_file, 'r', encoding='utf-8') as input_file:
        markdown_text = input_file.read()
        html_content = markdown2.markdown(markdown_text)
    html_content = insert_style(html_content)
    return html_content


def write_to_file(html_content, html_file):
    with open(html_file, 'w', encoding='utf-8') as output_file:
        output_file.write(html_content)


def HTML_to_docx(html_file, word_file):
    try:
        # Convert HTML to Word using pypandoc
        pypandoc.convert_file(html_file, 'docx', outputfile=word_file)
        print(f"Conversion successful: {html_file} -> {word_file}")
    except Exception as e:
        print(f"Error: {e}")


def HTML_to_pdf(html_file, pdf_file):
    # Convert HTML to PDF using multiple methods
    # Method 1: Try using xhtml2pdf (pure Python, reliable)
    try:
        from xhtml2pdf import pisa
        with open(html_file, 'rb') as html_input:
            with open(pdf_file, 'wb') as pdf_output:
                pisa.CreatePDF(html_input, pdf_output)
        print(f"Conversion successful: {html_file} -> {pdf_file}")
        return
    except Exception as e:
        print(f"xhtml2pdf failed: {e}")
    
    # Method 2: Try using pdfkit with system wkhtmltopdf
    try:
        import pdfkit
        pdfkit.from_file(html_file, pdf_file)
        print(f"Conversion successful: {html_file} -> {pdf_file}")
        return
    except Exception as e:
        print(f"pdfkit failed: {e}")
    
    # Method 3: Try using pypandoc with system latex
    try:
        pypandoc.convert_file(html_file, 'pdf', outputfile=pdf_file)
        print(f"Conversion successful: {html_file} -> {pdf_file}")
        return
    except Exception as e:
        print(f"pypandoc failed: {e}")
    
    # Fallback message
    print(f"Warning: PDF conversion skipped for {os.path.basename(html_file)}")


def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to PDF and Word')
    parser.add_argument("-i", "--input_file", required=True, help='Input Markdown file')
    parser.add_argument("-o", "--out_dir", required=True,help="directrory to write results")
    args = parser.parse_args()
    input_markdown_file = args.input_file
    out_dir = args.out_dir
    current_date = datetime.now().strftime('%Y%m%d')
    output_html_file = f"{out_dir}/{Path(input_markdown_file).stem}_{current_date}.html"
    output_pdf_file = f"{out_dir}/{Path(input_markdown_file).stem}_{current_date}.pdf"
    output_word_file = f"{out_dir}/{Path(input_markdown_file).stem}_{current_date}.docx"
    
    # Remove existing files if they exist
    for file_path in [output_html_file, output_pdf_file, output_word_file]:
        if os.path.exists(file_path):
            os.remove(file_path)

    # Convert Markdown to HTML
    html_content = markdown_to_html(input_markdown_file)
    write_to_file(html_content, output_html_file)

    HTML_to_docx(output_html_file, output_word_file)
    HTML_to_pdf(output_html_file, output_pdf_file)


if __name__ == "__main__":
    main()
