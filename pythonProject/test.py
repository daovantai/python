

import PyPDF2

# Mở file PDF
pdf_file = open('CV/CV.pdf', 'rb')

# Đối tượng PDF
pdf_reader = PyPDF2.PdfReader(pdf_file)

text=''
# Đọc nội dung các trang PDF
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    # print(page.extract_text())
    text += page.extract_text()
# Đóng file PDF
pdf_file.close()

words = text.split()
punctuations = '''!()-[]{};:•'"\✏✉,<> ©./?@#$%^&*_~⭐+●'''
cleaned_words = [word.lower().translate(str.maketrans('', '', punctuations)) for word in words]
stop_words = ['and', 'the', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'is', 'are', 'am', 'of', 'that', 'which', 'with', 'as', 'from','topcvvn']
filtered_words = [word for word in cleaned_words if word not in stop_words]
cleaned_text = ''.join(filtered_words)


check=''

my_list = ['mụctiêu', 'kinhnghiệm', 'kỹnăng', 'trìnhđộ', 'chứngchỉ','skill','họcvấn','education']
list_check=[]
for i in my_list:
    if i in cleaned_text:
        list_check.append(i)
print(cleaned_text)
print(list_check)
