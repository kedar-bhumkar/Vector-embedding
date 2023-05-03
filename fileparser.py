import PyPDF4

def parseFile():
    # Open the PDF file in read-binary mode
    pdf_file = open('./files/file1.pdf', 'rb')

    # Create a PDF reader object
    pdf_reader = PyPDF4.PdfFileReader(pdf_file)

    # Extract the text from each page of the PDF
    text = ''
    for page in range(pdf_reader.getNumPages()):
        text += pdf_reader.getPage(page).extractText()

    # Split the text into paragraphs
    paragraphs = text.split('\n\n')

    pdf_out = open("output.txt", "a", encoding="utf-8")

    res = []
    # Print the paragraphs
    for i, paragraph in enumerate(paragraphs):
        #print(f'Paragraph {i+1}:')
        # pdf_out.write(paragraph)
        res.append(paragraph)

    # pdf_out.close()
    return res


