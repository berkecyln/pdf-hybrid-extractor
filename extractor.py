import fitz # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os
import sys

def extract_text_from_page(page):
    text = page.get_text("text")
    return text
def extract_text_from_image(images, page_num):
    try:
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
def save_page_as_image(images, page_num, image_output_folder, pdf_name):
    try:
        if images:
            image_filename = f"{pdf_name}_page_{page_num + 1}.png"
            image_path = os.path.join(image_output_folder, image_filename)
            images[0].save(image_path, 'PNG')
            print(f"Saved page {page_num + 1} as image: {image_path} since it was non-processable.")
            return f"{pdf_name} page {page_num + 1} is saved as image: {image_filename}\n"
        else:
            print(f"Conversion of page {page_num + 1} to image returned no images.")
            return ""
    except Exception as e:
        print(f"Error saving page {page_num + 1} as image: {e}")
        return ""

def extract_data_from_pdf(pdf_path, image_output_folder, min_text_length=100):
    full_text = []
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    print("Starting PDF text extraction...\n")
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"Error opening PDF file: {e}")
        return
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        
        # Option 1: Direct Text Extraction
        text = extract_text_from_page(page)

        if len(text.strip()) > min_text_length:
            print(f"Page {page_num + 1}/{len(doc)}: Extracted text directly.")
            full_text.append(f"Page {page_num + 1}:\n{text}\n")
        else:
            # Option 2: OCR Extraction
            print(f"Page {page_num + 1}/{len(doc)}: Direct extraction insufficient, performing OCR...")
            images = convert_from_path(pdf_path, first_page=page_num + 1, last_page=page_num + 1)
            ocr_text = extract_text_from_image(images, page_num)
            if len(ocr_text.strip()) > min_text_length:
                print(f"Page {page_num + 1}/{len(doc)}: Extracted text via OCR.")
                full_text.append(f"Page {page_num + 1}:\n{ocr_text}\n")
            else:
                # Option 3: Save as Image
                print(f"Page {page_num + 1}/{len(doc)}: OCR extraction insufficient, saving page as image.")
                placeholder = save_page_as_image(images, page_num, image_output_folder, pdf_name)
                full_text.append(placeholder)
    doc.close()
    print("PDF text extraction completed.")
    return "\n".join(full_text)

if __name__ == "__main__":
    PDF_FILE_NAME = "ComputerVision04.pdf"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    FILE_PATH = os.path.join(BASE_DIR, "source_pdfs", PDF_FILE_NAME)

    PARENT_OUTPUT_FOLDER = os.path.join(BASE_DIR, "extracted_outputs")

    OUTPUT_FOLDER_CHILD = os.path.join(PARENT_OUTPUT_FOLDER, f"{os.path.splitext(PDF_FILE_NAME)[0]}_output")

    TXT_OUTPUT = os.path.join(OUTPUT_FOLDER_CHILD, f"{os.path.splitext(PDF_FILE_NAME)[0]}_extracted.txt")

    IMAGE_OUTPUT_FOLDER = os.path.join(OUTPUT_FOLDER_CHILD, "NonProcessablePages")

    MIN_TEXT_LENGTH = 100  # Tune this based on your pdf file

    if not os.path.exists(PARENT_OUTPUT_FOLDER):
        os.makedirs(PARENT_OUTPUT_FOLDER)
    if not os.path.exists(OUTPUT_FOLDER_CHILD):
        os.makedirs(OUTPUT_FOLDER_CHILD)
    if not os.path.exists(IMAGE_OUTPUT_FOLDER):
        os.makedirs(IMAGE_OUTPUT_FOLDER)

    if not os.path.exists(FILE_PATH):
        print(f"Error: File not found at {FILE_PATH}")
        print(f"Please put '{PDF_FILE_NAME}' in the 'test_pdfs' folder.")
        sys.exit(1)

    extracted_text = extract_data_from_pdf(FILE_PATH, IMAGE_OUTPUT_FOLDER, MIN_TEXT_LENGTH)

    if extracted_text:
        with open(TXT_OUTPUT, "w", encoding="utf-8") as f:
            f.write(extracted_text)
        print(f"\nExtracted text and images saved to:\n{OUTPUT_FOLDER_CHILD}")
    else:
        print("No text was extracted.")


