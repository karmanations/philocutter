import fitz # install using: pip install PyMuPDF
"""
PyPDF:
- Reads per page
- Has a bult-in function "get_text"
- Needs multiple libs
- Works better with punctuation, no useless spaces
"""

def retrieveText(pdfName):
    with fitz.open(pdfName) as doc:
        pdfText = []
        for page in doc:
            pdfText.append(page.get_text())
    return pdfText
    
def outputFile(outputText):
    # Output retrieved data in file
    with open("fitz_sample_export.txt", "w",  encoding='UTF-8') as text_file:
        text_file.write(outputText)

def main():
    #pdfName = input("Enter PDF name with extension.\n$")
    retrievedText = retrieveText("example.pdf")
    outputFile(retrievedText)

main()


