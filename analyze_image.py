import docker
import json
import sys

def analyze_image(image_name):
    client = docker.from_env()
    try:
        # Fetch image details
        image = client.images.get(image_name)
        print(f"Image '{image_name}' found.")
        print("Metadata:")
        print(json.dumps(image.attrs, indent=4))
    except docker.errors.ImageNotFound:
        print(f"Image '{image_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python analyze_image.py <image_name>")
        sys.exit(1)

    image_name = sys.argv[1]
    analyze_image(image_name)

if __name__ == "__main__":
    main()
