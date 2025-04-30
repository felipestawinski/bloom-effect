import numpy as np
import cv2 

def mask(image, threshold):
    rows, cols, channels = image.shape
    for row in range(rows):
        for col in range(cols):
            if image[row, col] < threshold:
                image[row, col] = 0

    cv2.imshow('Edited Image', image)
    return

def main():
    image = cv2.imread('./Wind Waker GC.bmp')
    if image is None:
        print("Error: Could not read the image.")
        return
    
    # cv2.imshow('Original Image', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    #mask(image, )


if __name__ == "__main__":
    main()