# PDF Hybrid Extractor

This is a simple Python tool that pulls the text out of any PDF, whether it's a digital file or a scanned image.

## How It Works

Script uses 3 methods to extract text from each page of the PDF, they are like fallbacks of each case.

1.  **Stage 1: Digital Text (Fast)**

      * By using pyMuPDF, it first tries to get the digital text directly from the PDF. 

2.  **Stage 2: OCR (Slow)**

      * If there's no digital text, it assumes the page is a scan. It uses Tesseract (OCR) to "read" the text from the page image.

3.  **Stage 3: Save as Image (The Fallback)**

      * If the OCR engine *still* can't find any text (like on a graph, chart, or diagram), it gives up and saves the page as a `.png` file. So no content is lost.

## How to Use

1.  **Clone the repo:**

    ```bash
    git clone https://github.com/your-username/pdf-hybrid-extractor.git
    cd pdf-hybrid-extractor
    ```

2.  **Set up the environment:**

      * This tool uses Conda to manage all dependencies.
      * Run `conda env create -f environment.yml` to create the environment and install all packages.
      * Then, activate it with `conda activate pdf_extractor`

3.  **Add your PDF:**

      * Place your file (e.g., `placeholder.pdf`) inside the `source_pdfs` folder.

4.  **Run the script:**

      * Open `extractor.py` and change the `PDF_FILE_NAME` variable at the bottom to match your file.
      * Run it from your terminal:
        ```bash
        python extractor.py
        ```
      * **Note**: After running if your txt has not all info or you want to keep more images, you can decrease or increase the `MIN_TEXT_LENGTH` variable depending on your needs.

## Output

After running, you'll get a new folder named `extracted_outputs`. Inside, you'll find `[your_pdf_name]_output/` which contains:

  * **`[your_pdf_name]_extracted.txt`:** A single text file with all the text from the PDF.
  * **`NonProcessablePages/`:** A folder containing any pages that were saved as images.
## Contact:
If you have any questions or feedback, feel free to reach out to     me via [email](mailto:berkeceylan12@hotmail.com)