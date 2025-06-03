# Bloom Effect Image Filter

This project implements a **bloom effect** filter using Python and OpenCV. The bloom effect is a popular post-processing technique in computer graphics that makes bright areas of an image glow, creating a dreamy or ethereal look. This is achieved by masking bright regions, blurring them, and then adding the result back to the original image.

---

## Features

- **Bloom with Gaussian Blur:** Enhances bright areas using multiple Gaussian blurs.
- **Bloom with Box Blur:** Alternative bloom effect using box (mean) blur.
- **Customizable Parameters:** Adjust threshold, blur amount, and kernel sizes.
- **Step-by-step Visualization:** Shows intermediate blurred images for debugging and learning.

---

## Requirements

- Python 3.7+
- [NumPy](https://numpy.org/)
- [OpenCV](https://opencv.org/) (`opencv-python`)

Install dependencies with:

```sh
pip install numpy opencv-python
```

---

## Usage

1. **Place your image** (e.g., `Wind Waker GC.bmp`) in the project directory.
2. **Run the script:**

   ```sh
   python main.py
   ```

3. **Adjust parameters** in `main.py` as needed:
   - `threshold`: Controls which pixels are considered "bright" (default: 0.7)
   - `blur_amount`: Controls the strength of the Gaussian blur
   - `size`: Kernel size for box blur

---

## How It Works

1. **Masking:**  
   The `mask` function keeps only pixels above a brightness threshold, setting others to black.

2. **Blurring:**  
   The masked image is blurred several times (with increasing kernel sizes) using either Gaussian or box blur.

3. **Compositing:**  
   The blurred images are summed and added back to the original, creating the bloom effect.

---

## Example

```python
image = cv2.imread('./Wind Waker GC.bmp')
image = image.astype(np.float32) / 255

bloom_gaussian = apply_bloom_gaussian(image, threshold=0.7, blur_amount=5.0)
cv2.imshow('Gaussian Bloom Effect', bloom_gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## File Structure

```
bloom-effect/
│
├── main.py         # Main script with bloom effect functions
├── Wind Waker GC.bmp  # Example image (not included)
└── README.md       # This file
```

---

## Customization

- **Change the image:** Replace `Wind Waker GC.bmp` with your own image.
- **Tune the effect:** Edit parameters in `main.py` for different looks.
- **Try both bloom methods:** Use `apply_bloom_gaussian` or `apply_bloom_media`.

---

## License

This project is for educational purposes.

---

## References

- [OpenCV Documentation](https://docs.opencv.org/)
- [Bloom (Shader) - Wikipedia](https://en.wikipedia.org/wiki/Bloom_(shader_effect))

---

**Enjoy creating glowing images!**