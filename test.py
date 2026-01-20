import cv2
import numpy as np
import matplotlib.pyplot as plt

def process_fourier(image_path, radius=15, inverse=False):
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found.")
        return
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    channels = cv2.split(img)
    filtered_channels = []

    for char_img in channels:
        # 1. Forward FFT
        dft = np.fft.fft2(char_img)
        dft_shift = np.fft.fftshift(dft)
        
        rows, cols = char_img.shape
        crow, ccol = rows // 2, cols // 2
        
        # 2. Create the Mask
        # Default is Low-Pass (Color focus)
        mask = np.zeros((rows, cols), np.uint8)
        cv2.circle(mask, (ccol, crow), radius, 1, thickness=-1)
        
        # If inverse is True, we flip the mask to become a High-Pass (Detail focus)
        if inverse:
            mask = 1 - mask 
        
        # 3. Apply mask and Inverse FFT
        fshift_filtered = dft_shift * mask
        f_ishift = np.fft.ifftshift(fshift_filtered)
        img_back = np.fft.ifft2(f_ishift)
        
        # Use absolute value to handle complex numbers
        filtered_channels.append(np.abs(img_back))

    # Merge and normalize to 0-255 range
    result = cv2.merge(filtered_channels)
    result = np.uint8(np.clip(result, 0, 255))
    
    return img, result



# --- Execution ---

# --- Execution ---
original, decimated = process_fourier('cat.jpg', radius=2,inverse=True)#



# Visualization

cv2.imwrite('decimated_inverse.jpg', cv2.cvtColor(decimated, cv2.COLOR_RGB2BGR))
# plt.figure(figsize=(12, 6))
# plt.subplot(121), plt.imshow(original), plt.title('Original Image')
# plt.subplot(122), plt.imshow(decimated,"gray"), plt.title('Color Info Only (Fourier Decimated)')
# plt.show()