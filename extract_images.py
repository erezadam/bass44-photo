import fitz  # PyMuPDF
import os

def extract_images_from_pdf(pdf_path, output_folder):
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"Error opening file: {e}")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print(f"Opening: {pdf_path}...")
    image_count = 0
    
    for page_index in range(len(doc)):
        page = doc[page_index]
        image_list = page.get_images(full=True)
        
        if image_list:
            print(f"[+] Page {page_index + 1}: Found {len(image_list)} images")
        
        for image_index, img in enumerate(image_list, start=1):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            # Save image
            image_name = f"page_{page_index + 1}_img_{image_index}.{image_ext}"
            image_path = os.path.join(output_folder, image_name)
            
            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)
                image_count += 1

    print(f"\nSuccess! Extracted {image_count} images into the folder: '{output_folder}'")

# --- הגדרות ---
# וודא שהשם כאן זהה בדיוק לשם הקובץ שלך
pdf_filename = "חוברת תרגילים מעשית.pdf" 
output_dir = "extracted_images"

# הרצת הפונקציה
if __name__ == "__main__":
    if os.path.exists(pdf_filename):
        extract_images_from_pdf(pdf_filename, output_dir)
    else:
        print(f"Error: The file '{pdf_filename}' was not found in this folder.")