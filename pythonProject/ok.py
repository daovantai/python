import PyPDF2

# Mở file PDF
pdf_file = open('test2.pdf', 'rb')

# Đối tượng PDF
pdf_reader = PyPDF2.PdfReader(pdf_file)


# Đọc nội dung các trang PDF
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    print(page.extract_text())

# Đóng file PDF
pdf_file.close()