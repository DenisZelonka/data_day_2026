from PIL import Image
from pillow_heif import register_heif_opener
import os
import numpy as np
import cv2


def heic_to_jpg(img_name: str) -> None:
    register_heif_opener()
    image = Image.open(img_name + ".heic")
    image.save(img_name + ".jpg", format="JPEG")


# heic_to_jpg("ervina.jpg")


def create_gif(
    input_images: list[str], output_path: str, duration: int = 1000, loop: int = 0
) -> None:
    """
    Creates a GIF and ensures all frames match the dimensions of the first image.
    """
    if not input_images:
        print("No images provided.")
        return

    # Load the first image to set the reference size
    first_image = Image.open(input_images[0]).convert("RGB")
    target_size = first_image.size  # (width, height)

    processed_frames = [first_image]

    # Process subsequent images
    for img_path in input_images[1:]:
        with Image.open(img_path).convert("RGB") as img:
            if img.size != target_size:
                # Resize if dimensions don't match
                img = img.resize(target_size, Image.Resampling.LANCZOS)
            processed_frames.append(img)

    # Save the sequence
    processed_frames[0].save(
        output_path,
        format="GIF",
        append_images=processed_frames[1:],
        save_all=True,
        duration=duration,
        loop=loop,
    )
    print(f"GIF saved to {output_path} at {target_size[0]}x{target_size[1]}")


# create_gif(sorted(["zoom/" + x for x in os.listdir("zoom")]),"zoom.gif")


def to_grayScale(img_path: str) -> None:
    Image.open(img_path).convert("L").save(img_path.split(".")[0] + "_gray.jpg")


# to_grayScale("ervina.jpg")


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

# original, decimated = process_fourier('ervina.jpg', radius=2)# 

# cv2.imwrite('decimated.jpg', cv2.cvtColor(decimated, cv2.COLOR_RGB2BGR))


# original, decimated = process_fourier('ervina.jpg', radius=0,inverse=True)# 

# cv2.imwrite('decimated_inverse.jpg', cv2.cvtColor(decimated, cv2.COLOR_RGB2BGR))


img =cv2.imread("eye_part.png",cv2.IMREAD_GRAYSCALE)

np.savetxt("pixels_gray.txt",img,"%d")


