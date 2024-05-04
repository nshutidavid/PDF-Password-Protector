from PyPDF2 import PdfWriter, PdfReader

pdf_writer = PdfWriter()
pdf_reader = PdfReader("/home/nshuti_dav/Apps/pdf password protector/PDF-Password-Protector/ID.pdf")

for page_num in range(len(pdf_reader.pages)):
    pdf_writer.add_page(pdf_reader.pages[page_num])


password = "nshuti"
pdf_writer.encrypt(user_password=password, use_128bit=True)

with open('myID.pdf', 'wb') as f:
    pdf_writer.write(f)



