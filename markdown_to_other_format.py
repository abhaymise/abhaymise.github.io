#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module desciption: 
Description of what markdown_to_other_format.py does.
"""
# markdown_to_other_format.py created at 09-10-2023
__author__ = "Abhay Kumar"
__date__ = "09-10-2023"
__copyright__ = "Copyright 2022"

import argparse
import pypandoc
import markdown2
from pathlib import Path
import pdfkit


def insert_style(html_content):
    # Create HTML content with Georgia font enforced
    html_with_georgia_font = f"""
        <!DOCTYPE html>
        <html>
        <head>
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
    with open(markdown_file, 'r') as input_file:
        markdown_text = input_file.read()
        html_content = markdown2.markdown(markdown_text)
    html_content = insert_style(html_content)
    return html_content


def write_to_file(html_content, html_file):
    with open(html_file, 'w') as output_file:
        output_file.write(html_content)


def HTML_to_docx(html_file, word_file):
    try:
        pypandoc.convert_file(html_file, 'docx', outputfile=word_file)
        print(f"Conversion successful: {html_file} -> {word_file}")
    except Exception as e:
        print(f"Error: {e}")


def HTML_to_pdf(html_file, pdf_file):
    # Convert HTML to PDF using pdfkit
    options = {
        'page-size': 'A4',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'encoding': 'UTF-8'
    }
    path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    pdfkit.from_file(html_file, pdf_file, options=options, configuration=config)
    print(f"Conversion successful: {html_file} -> {pdf_file}")


def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to PDF and Word')
    parser.add_argument('input_file', help='Input Markdown file')
    args = parser.parse_args()
    input_markdown_file = args.input_file
    output_html_file = f"{Path(input_markdown_file).stem}.html"
    output_pdf_file = f"{Path(input_markdown_file).stem}.pdf"
    output_word_file = f"{Path(input_markdown_file).stem}.docx"

    # Convert Markdown to HTML
    html_content = markdown_to_html(input_markdown_file)
    write_to_file(html_content, output_html_file)

    HTML_to_docx(output_html_file, output_word_file)
    HTML_to_pdf(output_html_file, output_pdf_file)


if __name__ == "__main__":
    main()
