import cv2
import os

def region_detection(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Perform Canny edge detection
    edges = cv2.Canny(blurred, 100, 200)
    
    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours on the original image
    image_with_contours = cv2.drawContours(image.copy(), contours, -1, (0, 0, 255), 2)
    
    return image_with_contours

# Load image
image_path = 'test.jpeg'

# Print the current working directory
print(f"Current working directory: {os.getcwd()}")

# Check if the image file exists
if not os.path.isfile(image_path):
    print(f"Error: File not found at {image_path}")
else:
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Unable to load image at {image_path}")
    else:
        # Apply region detection
        image_with_contours = region_detection(image)

        # Save the image with contours to a folder
        output_folder = 'region_detection_images'
        os.makedirs(output_folder, exist_ok=True)
        output_path = os.path.join(output_folder, 'image_with_contours.jpg')
        cv2.imwrite(output_path, image_with_contours)

        print(f"Image with contours saved to: {output_path}")

        # Display the original and the image with contours (optional)
        cv2.imshow('Original Image', image)
        cv2.imshow('Image with Contours', image_with_contours)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
