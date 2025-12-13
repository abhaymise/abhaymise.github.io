# markdown_to_other_format.py

Small helper to convert Markdown resumes to HTML and Word (and optionally PDF).

## Overview

The script `tools/markdown_to_other_format.py` converts a Markdown file to HTML and DOCX. The generated HTML enforces the Georgia font. PDF generation is available but disabled by default.

## Prerequisites

- Python 3.8+
- pip
- pandoc (required by `pypandoc`)
- Optional: wkhtmltopdf (required for PDF output via `pdfkit`)

Install pandoc on macOS:

    brew install pandoc

Install wkhtmltopdf (optional):

    brew install --cask wkhtmltopdf

## Install Python dependencies

From the repository root:

    python3 -m pip install -r tools/requirements.txt

## Usage

Basic example (converts to HTML and DOCX):

    python3 tools/markdown_to_other_format.py -i resume/resume.md -o resume/other_formats

This writes `<stem>.html` and `<stem>.docx` to the output directory. For `resume/resume.md` the outputs will be written to `resume/other_formats/`.

## Enabling PDF output

PDF conversion uses `wkhtmltopdf` via `pdfkit`. To enable PDF output:

1. Install `wkhtmltopdf` (see Prerequisites).
2. Update the `path_wkhtmltopdf` variable in `tools/markdown_to_other_format.py` to the correct binary path for your system (macOS commonly `/usr/local/bin/wkhtmltopdf` or `/opt/homebrew/bin/wkhtmltopdf`).
3. Uncomment the `HTML_to_pdf(...)` call near the end of the script.

## Notes

- `pypandoc` requires the pandoc binary; if you see conversion errors, ensure `pandoc` is installed and on your PATH.
- The script adds simple styling (Georgia font and letter spacing) to the generated HTML.

## Example

    python3 tools/markdown_to_other_format.py -i resume/resume.md -o resume/other_formats

Outputs:
- `resume/other_formats/resume.html`
- `resume/other_formats/resume.docx`
- `resume/other_formats/resume.pdf` (only if PDF generation enabled)

