import os
from PIL import Image

# Set the directory containing the PNG files
input_dir = "./"  # Change this to your folder path

# Output directory
output_dir = os.path.join(input_dir, "concatenated")
os.makedirs(output_dir, exist_ok=True)

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".png") and filename.startswith("output_"):
        continue  # Skip output_x.png to avoid duplicate processing

    if filename.endswith(".png"):
        x = filename[:-4]  # Strip '.png'
        left_path = os.path.join(input_dir, f"{x}.png")
        right_path = os.path.join(input_dir, f"output_{x}.png")

        # Check if both files exist
        if os.path.exists(left_path) and os.path.exists(right_path):
            left_img = Image.open(left_path)
            right_img = Image.open(right_path)

            # Ensure heights match
            if left_img.height != right_img.height:
                max_height = max(left_img.height, right_img.height)
                left_img = left_img.resize(
                    (left_img.width, max_height), Image.BICUBIC
                )
                right_img = right_img.resize(
                    (right_img.width, max_height), Image.BICUBIC
                )

            # Create new image with combined width
            total_width = left_img.width + right_img.width
            combined_img = Image.new("RGB", (total_width, left_img.height))

            # Paste both images
            combined_img.paste(left_img, (0, 0))
            combined_img.paste(right_img, (left_img.width, 0))

            # Save the combined image
            output_path = os.path.join(output_dir, f"concat_{x}.png")
            combined_img.save(output_path)
            print(f"Saved {output_path}")
