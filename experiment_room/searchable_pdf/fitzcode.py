import fitz # install using: pip install PyMuPDF
"""
PyPDF:
- Reads per page
- Has a bult-in function "get_text"
- Needs multiple libs
- Works better with punctuation, no useless spaces
"""

with fitz.open("ocr2edit.pdf") as doc:
    text = ""
    for page in doc:
        text += page.get_text()

# Output retrieved data in file
with open("fitz_sample_export.txt", "w",  encoding='UTF-8') as text_file:
    text_file.write(text)