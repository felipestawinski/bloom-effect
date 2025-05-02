import numpy as np
import cv2 

def mask(image, threshold):
    rows, cols, channels = image.shape
    for row in range(rows):
        for col in range(cols):
            if np.all(image[row, col] < threshold):
                image[row, col] = 0.0

    cv2.imshow('Edited Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

def main():
    image = cv2.imread('./Wind Waker GC.bmp')
    if image is None:
        print("Error: Could not read the image.")
        return
    #image = image.reshape ((image.shape [0], image.shape [1], 1))
    image = image.astype (np.float32) / 255
    
    # cv2.imshow('Original Image', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    mask(image, 0.8)


if __name__ == "__main__":
    main()