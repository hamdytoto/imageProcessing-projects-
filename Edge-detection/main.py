import cv2
import os

def edge_detection(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply GaussianBlur to reduce noise and improve edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Perform Canny edge detection
    edges = cv2.Canny(blurred, 100, 200)
    
    return edges

# Load image
image_path = 'input_image.jpg'

# Check if the image file exists
if not os.path.isfile(image_path):
    print(f"Error: File not found at {image_path}")
else:
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Unable to load image at {image_path}")
    else:
        # Apply edge detection
        edges = edge_detection(image)

        # Save edges image to a folder
        output_folder = 'edge_detection_images'
        os.makedirs(output_folder, exist_ok=True)
        output_path = os.path.join(output_folder, 'edges_image.jpg')
        cv2.imwrite(output_path, edges)

        print(f"Edges image saved to: {output_path}")

        # Display the original and edges images (optional)
        cv2.imshow('Original Image', image)
        cv2.imshow('Edges Image', edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
