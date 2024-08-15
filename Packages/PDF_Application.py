import requests
import os
from tkinter import filedialog
from tkinter import Tk
import io

api_key = "project_public_dad7cc0bc1de9ad7cd2cf2d027cecae4_1xJMq178702e165d7055f18e6ee8366b05543" # Add your ILOVEPDF API Key here

# API URLs
pdf_to_pdf_api_url = "https://api.ilovepdf.com/v1/task/start"
pdf_to_text_api_url = "https://api.ilovepdf.com/v1/task/start"
text_to_pdf_api_url = "https://api.ilovepdf.com/v1/task/start"
pdf_to_image_api_url = "https://api.ilovepdf.com/v1/task/start"
image_to_pdf_api_url = "https://api.ilovepdf.com/v1/task/start"


class PDFProcessor:

    def __init__(self):
        self.pdf_files = []

    def combine_pdfs(self):
        pass

    def separate_pdf_pages(self):
        pass

    def remove_pdf_password(self):
        pass

    def extract_all_text(self):
        pass

    def convert_images_to_pdf(self):
        pass


def main():
    # Initialize PDFProcessor
    pdf_processor = PDFProcessor()

    # Open file dialog to select PDF files
    root = Tk()
    root.withdraw()
    pdf_processor.pdf_files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])

    # Display menu for user to select the operation
    operation = input("Enter the operation you want to perform (1. Combine PDFs, 2. Separate PDF Pages, 3. Remove PDF Password, 4. Extract All Text, 5. Convert Images to PDF): ")

    if operation == '1':
        pdf_processor.combine_pdfs()
    elif operation == '2':
        pdf_processor.separate_pdf_pages()
    elif operation == '3':
        pdf_processor.remove_pdf_password()
    elif operation == '4':
        pdf_processor.extract_all_text()
    elif operation == '5':
        pdf_processor.convert_images_to_pdf()
    else:
        print("Invalid operation.")

if __name__ == "__main__":
    main()
