import tkinter as tk
from tkinter import filedialog
import rasterio
from PIL import Image, ImageTk  
import numpy as np  

def upload_image():
    global image_data
    file_path = filedialog.askopenfilename(title="Select Image File (6 bands)", filetypes=[("TIF files", "*.tif *.tiff")])
    if file_path:
        try:
            with rasterio.open(file_path) as src:
                image_data = src.read()  
                print("Image uploaded successfully!")
                print("Number of bands:", image_data.shape[0])

        except Exception as e:
            print(f"Error reading image: {e}")
    if image_data is None or image_data.shape[0] != 6:
        print("Error: No image data loaded or incorrect number of bands.")
        return

    try:
        # Select any 3 bands for RGB display (modify these indices as needed)
        red_band = image_data[0]
        green_band = image_data[1]
        blue_band = image_data[2]

        # Create an RGB image by stacking the selected bands
        rgb_image = np.dstack((red_band, green_band, blue_band))

        # Display the RGB image
        display_image(rgb_image)

    except Exception as e:
        print(f"Error filtering image: {e}")

   
def display_image(img):
    # Convert NumPy array to a format compatible with tkinter
    img = Image.fromarray(img.astype('uint8'))
    img_tk = ImageTk.PhotoImage(img)

    # Create a new tkinter window to display the image
    window = tk.Toplevel()
    window.title("Filtered Image")

    # Add a label to display the image with some styling
    label = tk.Label(window, image=img_tk, bg="white", padx=20, pady=20)
    label.pack()

    # Keep a reference to the image to prevent it from being garbage collected
    label.image = img_tk

def print_segmented_image():
    image_path = r"D:\NARSS\omar\ZirconAI.tif"  
    try:
        with rasterio.open(image_path) as src:
            image_data = src.read()
            
            red_band = image_data[0]
            green_band = image_data[1]
            blue_band = image_data[2]

            # Create an RGB image by stacking the selected bands
            rgb_image = np.dstack((red_band, green_band, blue_band))

            # Display the RGB image
            display_image(rgb_image)
    except Exception as e:
            print( image_data.shape)
            
            print(f"Error reading or displaying image: {e}")

# GUI setup
root = tk.Tk()
root.title("Spectral Image Processing")
root.geometry("500x300")  # Set initial size of the main window

upload_button = tk.Button(root, text="Upload Image", command=upload_image, font=("Arial", 16), bg="blue", fg="white")
upload_button.pack(pady=20)

display_button = tk.Button(root, text="Display Image",command=print_segmented_image, font=("Arial", 16), bg="green", fg="white")
display_button.pack(pady=20)

root.mainloop()
