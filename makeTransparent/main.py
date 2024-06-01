import tkinter as tk
from tkinter import filedialog
from PIL import Image
import numpy as np

def make_background_transparent(image_path, output_path, bg_color=(255, 255, 255), tolerance=10):
    # Open the image
    img = Image.open(image_path).convert("RGBA")
    data = np.array(img)

    # Extract the individual color channels
    red, green, blue, alpha = data.T

    # Calculate the difference from the background color
    background = (np.abs(red - bg_color[0]) <= tolerance) & \
                 (np.abs(green - bg_color[1]) <= tolerance) & \
                 (np.abs(blue - bg_color[2]) <= tolerance)

    # Replace the background with transparency
    data[..., 3][background.T] = 0

    # Create a new image from the modified array
    new_img = Image.fromarray(data)
    new_img.save(output_path, "PNG")

def select_image():
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename()
    if file_path:
        # Set the output path
        output_path = "output_image.png"
        # Process the image to make background transparent
        make_background_transparent(file_path, output_path, bg_color=(255, 255, 255), tolerance=30)
        print(f"Processed image saved as {output_path}")

# Create the main window
root = tk.Tk()
root.title("Background Transparency Tool")

# Create a button to select an image
button = tk.Button(root, text="Select Image", command=select_image)
button.pack(pady=20)

# Run the GUI event loop
root.mainloop()
