import base64
from io import BytesIO
from PIL import Image

def convert_image_to_greyscale() -> str:
    """Convert a uri image to greyscale and return image uri.

    Args:
        image_uri: an image uri string.
    """
    image_path = "C:\\Users\\ismail\\Downloads\\MainBefore.jpg"
    with open(image_path, "rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
    
    # Decode the base64 image
    image_data = base64.b64decode(image_base64)
    image = Image.open(BytesIO(image_data))

    # Convert to greyscale
    grey_image = image.convert("L")

    # Save to a BytesIO object and encode back to base64
    buffer = BytesIO()
    grey_image.save(buffer, format="JPEG")
    buffer.seek(0)

    # encode back to base64 and create a data URI
    grey_image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    uri = f"data:image/jpeg;base64,{grey_image_base64}"

    return uri

if __name__ == "__main__":
    # Test the function
    grey_image_uri = convert_image_to_greyscale()
    print(grey_image_uri)