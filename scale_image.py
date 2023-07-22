from PIL import Image
import numpy as np
import sys


def scale_image_with_pixel_padding(input_path, output_path):
    try:
        with Image.open(input_path) as image:
            # Get the original size of the image
            width, height = image.size
            # Calculate the new size (3 times the original)
            new_width, new_height = width * 3, height * 3

            # Convert the image to a NumPy array for faster processing
            img_array = np.array(image)

            # Create a new blank array with transparent background
            padded_array = np.empty((new_height, new_width, 4), dtype=np.uint8)
            padded_array.fill(0)
            padded_array[:, :, 3] = 0  # Set alpha channel to 0 (fully transparent)

            # Copy the original pixels to the padded image array
            padded_array[1::3, 1::3, :] = img_array

            # Convert the padded array back to an image
            padded_image = Image.fromarray(padded_array)

            # Save the scaled image with padding around each pixel
            padded_image.save(output_path)

        print("Image scaled with padding around each pixel successfully!")
    except Exception as e:
        print(f"Error while scaling the image: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scale_image.py input_image output_image")
    else:
        input_image = sys.argv[1]
        output_image = sys.argv[2]
        scale_image_with_pixel_padding(input_image, output_image)
