from PIL import Image
import sys


def remove_pixel_padding(input_path, output_path):
    try:
        with Image.open(input_path) as padded_image:
            # Get the original size of the image (before padding)
            width, height = padded_image.size
            original_width, original_height = width // 3, height // 3

            # Create a new blank image without padding
            unpadded_image = Image.new("RGBA", (original_width, original_height), (0, 0, 0, 0))

            # Copy every third pixel from the padded image to the unpadded image
            for y in range(original_height):
                for x in range(original_width):
                    px, py = x * 3 + 1, y * 3 + 1
                    pixel_color = padded_image.getpixel((px, py))
                    unpadded_image.putpixel((x, y), pixel_color)

            # Save the unpadded image
            unpadded_image.save(output_path)

        print("Image with padding removed successfully!")
    except Exception as e:
        print(f"Error while removing padding from the image: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python remove_padding.py input_padded_image output_unpadded_image")
    else:
        input_padded_image = sys.argv[1]
        output_unpadded_image = sys.argv[2]
        remove_pixel_padding(input_padded_image, output_unpadded_image)
