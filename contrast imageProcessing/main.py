import cv2
import os

def contrast_enhancement(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply histogram equalization
    enhanced = cv2.equalizeHist(gray)
    
    # Convert back to BGR (if needed)
    enhanced_bgr = cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)
    
    return enhanced_bgr

# Load image
image = cv2.imread('test.jpg')

# Apply contrast enhancement
enhanced_image = contrast_enhancement(image)

# Save enhanced image to a folder
output_folder = 'enhanced_images'
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, 'enhanced_image.jpg')
cv2.imwrite(output_path, enhanced_image)

print(f"Enhanced image saved to: {output_path}")
