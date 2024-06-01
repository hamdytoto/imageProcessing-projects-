import cv2
import numpy as np
from scipy.signal import convolve2d
from scipy.fftpack import fft2, ifft2, fftshift

def wiener_deconvolution(image, kernel, K):
    kernel = np.flipud(np.fliplr(kernel))
    dummy = np.copy(image)
    dummy = fft2(dummy)
    kernel = fft2(kernel, s=image.shape)
    kernel = np.conj(kernel) / (np.abs(kernel) ** 2 + K)
    dummy = dummy * kernel
    dummy = np.abs(ifft2(dummy))
    return dummy

def motion_blur_kernel(length, angle):
    kernel = np.zeros((length, length))
    d = length // 2
    for i in range(length):
        for j in range(length):
            if np.abs(i - d) + np.abs(j - d) <= d:
                kernel[i, j] = 1
    kernel = cv2.warpAffine(kernel, cv2.getRotationMatrix2D((d, d), angle, 1.0), (length, length))
    return kernel / kernel.sum()

def restore_image(image_path, output_path, length, angle, K=0.01):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Unable to load image at {image_path}")
        return

    # Create the motion blur kernel
    kernel = motion_blur_kernel(length, angle)

    # Perform Wiener deconvolution
    restored_image = wiener_deconvolution(image, kernel, K)

    # Save the restored image
    cv2.imwrite(output_path, restored_image)

    print(f"Restored image saved to: {output_path}")

# Path to the input image
image_path = 'input_image.jpg'

# Path to save the restored image
output_path = 'restored_image.jpg'

# Motion blur parameters
length = 15  # Length of the motion blur
angle = 45   # Angle of the motion blur

# Print the current working directory
print(f"Current working directory: {os.getcwd()}")

# Check if the image file exists
if not os.path.isfile(image_path):
    print(f"Error: File not found at {image_path}")
else:
    # Restore the image
    restore_image(image_path, output_path, length, angle)
