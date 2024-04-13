from PIL import Image, ImageOps
import sys


def check_input(user_input: list[str]):
    if len(user_input) == 3:
        input_file, output_file = user_input[1], user_input[2]
        if input_file.lower().endswith((".jpeg",".jpg",".png")) and output_file.lower().endswith((".jpeg",".jpg",".png")):
            if input_file.split(".")[-1].lower() == output_file.split(".")[-1].lower():
                return input_file, output_file
    else:
        sys.exit(1)

def load_file(filename):
    try:
        return Image.open(filename)
    except:
        sys.exit(1)

def overlay_image(input_image):
    try:
        shirt_image = Image.open('shirt.png')  # Ensure 'shirt.png' is in the same directory
        input_resized = ImageOps.fit(input_image, shirt_image.size)
        input_resized.paste(shirt_image, (0, 0), shirt_image)
        return input_resized
    except:
        sys.exit(1)

def save_image(output_image, output_file):
    try:
        output_image.save(output_file)
    except Exception:
        sys.exit(1)

def main():

    input_file, output_file = check_input(sys.argv)
    input_image = load_file(input_file)
    output_image = overlay_image(input_image) 
    save_image(output_image,output_file)


if __name__ == "__main__":
    main()
