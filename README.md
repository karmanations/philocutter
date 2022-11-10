# philocutter

Uses fitz. Why?
- pymupdf / tika / PDFium are better than fitz, but the difference became rather small
- they are way faster, but not pure-Python.
- fitz handles better the punctuaton than PyPDF2 (no useless spaces)