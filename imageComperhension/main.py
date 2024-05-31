import cv2
import os

def compress_image(image_path, output_path, quality=90):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Unable to load image at {image_path}")
        return

    # Compress the image by saving it with a lower quality
    compression_params = [cv2.IMWRITE_JPEG_QUALITY, quality]

    # Save the compressed image
    cv2.imwrite(output_path, image, compression_params)

    print(f"Compressed image saved to: {output_path}")

# Path to the input image
image_path = 'test.jpeg'

# Path to save the compressed image
output_path = 'compressed_image.jpg'

# Desired quality for compression (0-100, higher is better quality)
quality = 50  # Adjust the quality as needed

# Print the current working directory
print(f"Current working directory: {os.getcwd()}")

# Check if the image file exists
if not os.path.isfile(image_path):
    print(f"Error: File not found at {image_path}")
else:
    # Compress the image
    compress_image(image_path, output_path, quality)
