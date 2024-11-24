#Install pillow using CMD (pip install pillow).
import os
from PIL import Image

def images_to_pdf():
    images_dir = r"" #Path to get the Images.
    pdf_dir = r"" #Path to Save the PDF.
    
    os.makedirs(pdf_dir, exist_ok=True) #It creates the PDF folder if it doesn't exist.
    
    image_files = [file for file in os.listdir(images_dir) if file.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'tiff'))]
    
    if not image_files:
        print("No images found in the 'Images' folder.") #If there is no Images in the folder.
        return
    image_files.sort()
    
    images = []
    for file in image_files:
        img_path = os.path.join(images_dir, file)
        img = Image.open(img_path)
        images.append(img.convert('RGB'))   

    pdf_name = os.path.splitext(image_files[0])[0] + ".pdf" #Uses the First image name as PDF name.
    pdf_path = os.path.join(pdf_dir, pdf_name)
    
    images[0].save(pdf_path, save_all=True, append_images=images[1:]) #Saves all images into Single PDF.
    print(f"PDF saved successfully at: {pdf_path}")

if __name__ == "__main__":
    images_to_pdf()
