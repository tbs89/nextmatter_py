from nextmatter.api import NextMatterAPI
import sys

def main(image_path: str):
    api = NextMatterAPI(api_key='YOUR_API_KEY')
    try:
        response = api.image.upload_image(image_path)
        print("Image uploaded successfully:", response)
    except Exception as e:
        print("Error uploading image:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python upload_image.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    main(image_path)
