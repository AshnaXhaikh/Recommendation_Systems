from PIL import Image, ImageDraw, ImageFont
import requests
import io

def get_cover_image(url):
    """Fetches book cover or returns placeholder with 'No Cover' text"""
    # Create gray placeholder (200x300 pixels)
    placeholder = Image.new('RGB', (200, 300), '#222222')
    draw = ImageDraw.Draw(placeholder)
    
    try:
        if not url or not isinstance(url, str):
            raise ValueError("Invalid URL")
            
        # Fetch image with timeout
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        # Verify image content
        if 'image' not in response.headers.get('content-type', ''):
            raise ValueError("Not an image")
            
        # Return resized cover
        img = Image.open(io.BytesIO(response.content))
        return img.resize((200, 300))
        
    except Exception as e:
        # Add error text to placeholder
        draw.text((50, 140), "No Cover", fill="white")
        return placeholder


def is_placeholder(img):
    """Detects if an image is our custom error placeholder.
    
    Args:
        img: PIL.Image object to check
        
    Returns:
        bool: True if the image matches our placeholder signature
    """
    # Early return for non-images
    if not isinstance(img, Image.Image):
        return True
    
    try:
        # Check basic properties first
        if img.size != (200, 300):
            return False
        
        # Verify background color (RGB 34,34,34 or #222222)
        background_pixel = img.getpixel((10, 10))
        if background_pixel != (34, 34, 34):
            return False
        
        # Check for "No Cover" text by sampling expected text area
        text_area = img.crop((40, 130, 160, 150))  # Area where text would be
        text_pixels = list(text_area.getdata())
        
        # Count white pixels (RGB 255,255,255) in text area
        white_pixels = sum(1 for pixel in text_pixels if pixel == (255, 255, 255))
        
        # If we find between 50-500 white pixels, assume text exists
        return 50 < white_pixels < 500
        
    except Exception as e:
        print(f"Placeholder check error: {str(e)}")
        return False
