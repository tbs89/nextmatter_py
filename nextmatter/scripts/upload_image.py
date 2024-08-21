from nextmatter.api import NextMatterAPI
import sys

def main(file_path: str):
    api = NextMatterAPI(api_key='YOUR_API_KEY')
    try:
        response = api.file.upload_file(file_path)
        print("File uploaded successfully:", response)
    except Exception as e:
        print("Error uploading file:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python upload_file.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    main(file_path)
