from pdfreader import SimplePDFViewer

# Open the PDF file in read binary mode
with open('cv.pdf', 'rb') as pdf_file:
    # Create a PDF viewer object
    viewer = SimplePDFViewer(pdf_file)

    # Loop over each page in the PDF document
    for canvas in viewer:
        # Get the text from the current page
        text = ''.join(canvas.strings)
        # Print the text to the console
        print(text)