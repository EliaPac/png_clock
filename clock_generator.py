from PIL import Image, ImageDraw, ImageFont
import datetime

def generate_time_png(filename="current_time.png"):
    """
    Generates a PNG image with the current time as white text on a black background.
    The image is saved with the specified filename, overwriting if it exists.
    """
    # Get current time
    current_time = datetime.datetime.now().strftime("%H:%M")

    # Image dimensions (adjust as needed)
    img_width = 1200
    img_height = 400

    # Create a black image
    img = Image.new('RGBA', (img_width, img_height), color = (255, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # Try to load a font (you might need to specify a path to a font file)
    try:
        font_size = 120
        # Common font paths:
        # Windows: C:/Windows/Fonts/arial.ttf
        # macOS: /Library/Fonts/Arial.ttf
        # Linux: /usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf (or similar)
        # If you don't have a specific font, Pillow will use a default
        font = ImageFont.truetype("Montserrat-ExtraBold.ttf", font_size) # Replace "arial.ttf" with a font available on your system if needed
    except IOError:
        font = ImageFont.load_default()
        # print("Could not load specified font, using default.")

    # Text color (white)
    text_color = (255, 255, 255)

    # Get text size
    bbox = d.textbbox((0,0), current_time, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Calculate position to center the text
    x = (img_width - text_width) / 2
    y = (img_height - text_height) / 2

    # Draw the text
    d.text((x, y), current_time, fill=text_color, font=font)

    # Save the image
    img.save(filename)
    # print(f"Generated '{filename}' with current time: {current_time}")

if __name__ == "__main__":
    # Ensure you have the necessary libraries installed:
    # pip install pypng Pillow

    # The script will save the image in the directory where it's run.
    generate_time_png("current_time.png")