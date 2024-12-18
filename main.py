import fitz  # PyMuPDF
import os
from pathlib import Path

def create_directory(path):
    """
    Creates a directory if it doesn't exist.

    Args:
        path (Path): The path of the directory to create.
    """
    if not path.exists():
        path.mkdir(parents=True)
        print(f"Created directory: {path}")

def convert_pdf_to_images(pdf_path, output_dir, output_format='png'):
    """
    Converts each page of a PDF to an image and saves them in the output directory.

    Args:
        pdf_path (Path): Path to the input PDF file.
        output_dir (Path): Directory where the images will be saved.
        output_format (str): The image format ('png' or 'jpeg'). Defaults to 'png'.
    """
    try:
        # Open the PDF file
        doc = fitz.open(pdf_path)
        print(f"Opened PDF: {pdf_path.name}")

        # Iterate through each page and save as image
        for page_num in range(doc.page_count):
            page = doc[page_num]
            pix = page.get_pixmap()
            output_filename = output_dir / f"{pdf_path.stem}_page_{page_num + 1}.{output_format.lower()}"
            pix.save(output_filename)
            print(f"Saved {output_filename.name}")

        print(f"Conversion complete for '{pdf_path.name}'. {doc.page_count} images saved in '{output_dir}'.\n")

    except Exception as e:
        print(f"An error occurred while converting '{pdf_path.name}': {e}")

def main():
    """
    Main function to execute the PDF to image conversion.
    """
    # Define input and output directories
    base_dir = Path(__file__).parent
    input_dir = base_dir / "input"
    output_dir = base_dir / "output"

    # Create directories if they don't exist
    create_directory(input_dir)
    create_directory(output_dir)

    # Prompt user for desired output format
    output_format = input("Enter the desired output format (png/jpeg) [png]: ").strip().lower()
    if output_format not in ['png', 'jpeg', 'jpg']:
        print("Invalid format selected. Defaulting to 'png'.")
        output_format = 'png'

    # Process each PDF in the input directory
    pdf_files = list(input_dir.glob("*.pdf"))
    if not pdf_files:
        print(f"No PDF files found in '{input_dir}'. Please add PDF files to convert.")
        return

    for pdf_file in pdf_files:
        # Convert PDF to images
        convert_pdf_to_images(pdf_file, output_dir, output_format)

    print("All PDF files have been processed.")

if __name__ == "__main__":
    main()