import cv2
import os

def denoise_image(image):
    # Apply Non-Local Means Denoising algorithm
    denoised_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
    return denoised_image

# Load image
image = cv2.imread('test.jpg')

# Apply denoising
denoised_image = denoise_image(image)

# Save denoised image to a folder
output_folder = 'denoised_images'
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, 'denoised_image.jpg')
cv2.imwrite(output_path, denoised_image)

print(f"Denoised image saved to: {output_path}")

# Display the original and denoised images (optional)
# cv2.imshow('Original Image', image)
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
