from PyPDF2 import PdfReader # pip install PyPDF2
"""
PyPDF:
- Reads per page
- Has a bult-in function "extract_text"
- Only one lib required, better than fitz
-  no useless spaces on punctuation encounter
"""

reader = PdfReader("example.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"


# Output retrieved data in file
with open("pypdf2_sample_export.txt", "w",  encoding='UTF-8') as text_file:
    text_file.write(text)