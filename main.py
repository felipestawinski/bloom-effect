import numpy as np
import cv2 

def mask(image, threshold):
    
    mask = image.copy()
    rows, cols, channels = image.shape
    for row in range(rows):
        for col in range(cols):
            if np.all(image[row, col] < threshold):
                mask[row, col] = 0.0
    return mask

def borrar_gaussian(image, sigma, size=5):
    if size % 2 == 0:
        size += 1
    image = cv2.GaussianBlur(image, (size, size), sigma)
    return image

def borrar_media(image, size):
    image = cv2.blur(image, (size, size))
    return image

def apply_bloom_gaussian(image, threshold=0.7, blur_amount=1.5):
    
    original = image.copy()
    blurred_images = np.zeros_like(image)
    mask_img = mask(image, threshold)
    
    for i in range(5): 
        blurred = borrar_gaussian(mask_img, blur_amount+(i*i*3), 5*i*2)
        blurred_images += blurred
        cv2.imshow(f'blurred Image {i}', blurred)
        cv2.waitKey(0)
    
    result = original + blurred_images
    return result

def apply_bloom_media(image, threshold=0.7, size=5):
    
    original = image.copy()
    blurred_images = np.zeros_like(image)
    mask_img = mask(image, threshold)
    
    for i in range(3):
        blurred = borrar_media(mask_img, size+(i*i*2))
        blurred_images += blurred
        cv2.imshow(f'blurred Image {i}', blurred)
        cv2.waitKey(0)
    result = original + blurred_images
    
    return result

def main():
    image = cv2.imread('./Wind Waker GC.bmp')
    if image is None:
        print("Error: Could not read the image.")
        return
    
    image = image.astype(np.float32) / 255
    # cv2.imshow('Original Image', image)
    # cv2.waitKey(0)
    
    bloom_gaussian = apply_bloom_gaussian(image, threshold=0.7, blur_amount=5.0)
    cv2.imshow('Gaussian Bloom Effect!!!', bloom_gaussian)
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    
    # bloom_box = apply_bloom_media(image, threshold=0.7, size=3)
    # cv2.imshow('Box Blur Bloom Effect', bloom_box)
    # cv2.waitKey(0)
    
    # image1 = cv2.GaussianBlur(image, (5, 5), 5)
    # image2 = cv2.GaussianBlur(image, (15, 15), 18)
    # cv2.imshow('Gaussian Bloom Effect5', image1)
    # cv2.imshow('Gaussian Bloom Effect518', image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()