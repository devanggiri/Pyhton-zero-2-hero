import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

# Load image using OpenCV
image_path = 'input_image.jpg'
img = cv2.imread(image_path)

# 1. Convert to Grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Resize Image (keeping aspect ratio)
def resize_image(image, width=None, height=None):
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        ratio = height / float(h)
        dim = (int(w * ratio), height)
    else:
        ratio = width / float(w)
        dim = (width, int(h * ratio))
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

resized_img = resize_image(gray_img, width=500)

# 3. Noise Reduction (using Gaussian Blur)
denoised_img = cv2.GaussianBlur(resized_img, (5, 5), 0)

# 4. Contrast Adjustment (using Histogram Equalization)
equalized_img = cv2.equalizeHist(denoised_img)

# 5. Edge Detection (using Canny Edge Detection)
edges = cv2.Canny(equalized_img, 100, 200)

# 6. Rotate Image to Correct Orientation (if necessary)
def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

# Assuming an angle of correction
corrected_img = rotate_image(edges, angle=0)  # Adjust angle as needed

# 7. Remove Small Noise (using Morphological Operations)
kernel = np.ones((5, 5), np.uint8)
cleaned_img = cv2.morphologyEx(corrected_img, cv2.MORPH_CLOSE, kernel)

# 8. Save or Display the Cleaned Image
cv2.imwrite('cleaned_image.jpg', cleaned_img)
cv2.imshow('Cleaned Image', cleaned_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 9. (Optional) Further Enhancement using PIL
# Convert back to PIL Image for additional enhancements
pil_img = Image.fromarray(cleaned_img)

# 9.1 Brightness Enhancement
enhancer = ImageEnhance.Brightness(pil_img)
enhanced_img = enhancer.enhance(1.5)  # Increase brightness by 1.5x

# 9.2 Sharpening the Image
sharpened_img = enhanced_img.filter(ImageFilter.SHARPEN)

# Save or Display the Final Enhanced Image
sharpened_img.save('final_cleaned_image.jpg')
sharpened_img.show()


'''
Explanation of Steps
Convert to Grayscale: Converting the image to grayscale simplifies processing by reducing color complexity.
Resize Image: Resizes the image while maintaining the aspect ratio, which is useful for standardizing image dimensions.
Noise Reduction: Applies Gaussian Blur to reduce noise and smooth the image.
Contrast Adjustment: Uses histogram equalization to improve contrast in the image.
Edge Detection: Detects edges using the Canny method, which is useful for further analysis or object detection.
Rotate Image: Corrects the orientation of the image by rotating it to the desired angle.
Remove Small Noise: Uses morphological operations to remove small noise and imperfections.
Save or Display: Saves the cleaned image or displays it using OpenCV.
Further Enhancement (Optional): Uses PIL for additional image enhancements such as brightness and sharpening.
'''
