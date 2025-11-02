import fitz # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os
import sys

def extract_text_from_page(page):
    text = page.get_text("text")
    return text
def extract_text_from_image(pdf_path, page_num):
    try:
        # Convert page to image
        images = convert_from_path(pdf_path, first_page=page_num + 1, last_page=page_num + 1)
        if images:
            # OCR
            text = pytesseract.image_to_string(images[0])
            return text
        else:
            print(f"Conversion of page {page_num + 1} to image returned no images.")
            return ""
    except Exception as e:
        print(f"Error extracting text from image on page {page_num + 1}: {e}")
        return ""
def save_page_as_image(pdf_path, page_num, image_output_folder, pdf_name):
    try:
        images = convert_from_path(pdf_path, first_page=page_num + 1, last_page=page_num + 1)
        if images:
            image_filename = f"{pdf_name}_page_{page_num + 1}.png"
            image_path = os.path.join(image_output_folder, image_filename)
            images[0].save(image_path, 'PNG')
            print(f"Saved page {page_num + 1} as image: {image_path} since it was non-processable.")
        else:
            print(f"Conversion of page {page_num + 1} to image returned no images.")
            return ""
    except Exception as e:
        print(f"Error saving page {page_num + 1} as image: {e}")
        return ""

def extract_data_from_pdf(pdf_path, output_txt_path):
    pass


if __name__ == "__main__":
    PDF_FILE_NAME = "my_lecture.pdf"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    FILE_PATH = os.path.join(BASE_DIR, "source_pdfs", PDF_FILE_NAME)

    OUTPUT_FOLDER_PATH = os.path.join(BASE_DIR, f"{os.path.splitext(PDF_FILE_NAME)[0]}_output")
    
    TXT_OUTPUT = os.path.join(OUTPUT_FOLDER_PATH, f"{os.path.splitext(PDF_FILE_NAME)[0]}_extracted.txt")
    
    IMAGE_OUTPUT_FOLDER = os.path.join(OUTPUT_FOLDER_PATH, "NonProcessablePages")


