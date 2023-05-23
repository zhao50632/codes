 
# Import necessary libraries
from PIL import Image
import math

# Define function to calculate the difference between two images
def image_difference(image1, image2):
    # Open images
    img1 = Image.open(image1)
    img2 = Image.open(image2)

    # Get image sizes
    width, height = img1.size

    # Calculate the difference between each pixel in the images
    total_diff = 0
    for x in range(width):
        for y in range(height):
            # Get the RGB values for each pixel in both images
            r1, g1, b1 = img1.getpixel((x, y))
            r2, g2, b2 = img2.getpixel((x, y))

            # Calculate the difference between the RGB values for each pixel
            diff = math.sqrt((r1 - r2)**2 + (g1 - g2)**2 + (b1 - b2)**2)

            # Add the difference to the total difference
            total_diff += diff

    # Calculate the average difference between the images
    avg_diff = total_diff / (width * height)

    # Return the average difference
    return avg_diff

# Test the function
print(image_difference(r'C:\Users\Administrator\Desktop\a1.jpg', r'C:\Users\Administrator\Desktop\i2.jpg'))

