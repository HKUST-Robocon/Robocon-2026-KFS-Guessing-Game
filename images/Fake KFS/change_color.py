import os
from PIL import Image

def is_blue(pixel):
    r, g, b, a = pixel
    return b > r + 30 and b > g + 30  # Simple check to identify blue shades

def change_blue_to_color(input_dir, output_dir, new_color):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Convert the new color from hex to RGB
    new_color = tuple(int(new_color[i:i+2], 16) for i in (1, 3, 5))

    # Iterate through all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_dir, filename)
            img = Image.open(img_path)

            # Convert image to RGBA (if not already in that mode)
            img = img.convert('RGBA')
            data = img.getdata()

            # Create a new list for the modified image data
            new_data = []
            for item in data:
                # print(item)
                # Change blue shades to the new color
                if is_blue(item):
                    new_data.append(new_color + (item[3],))  # Keep the alpha channel
                else:
                    new_data.append(item)

            # Update image data and save the modified image
            img.putdata(new_data)
            output_path = os.path.join(output_dir, filename.replace("Blue", "Red"))
            img.save(output_path)

    print(f"All blue shades changed to {new_color} for all images in {input_dir}.")

# Example usage
input_directory = './'  # Change to your input directory
output_directory = './output'  # Change to your output directory
new_bg_color_hex = '#C12D27'  # New background color in hex
#272481

change_blue_to_color(input_directory, output_directory, new_bg_color_hex)