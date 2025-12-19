import imageio.v2 as imageio
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# 1. Baca citra hasil Sobel
# ===============================
image = imageio.imread("output_sobel.png")

# Jika citra RGB, ubah ke grayscale
if len(image.shape) == 3:
    image = np.mean(image, axis=2).astype(np.uint8)

# ===============================
# 2. Basic Thresholding
# ===============================
threshold_value = 50  # bisa diubah (eksperimen 30–100)
binary_image = np.zeros_like(image)

binary_image[image >= threshold_value] = 255
binary_image[image < threshold_value] = 0

# ===============================
# 3. Visualisasi Hasil
# ===============================
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title("Citra Hasil Deteksi Tepi Sobel")
plt.imshow(image, cmap="gray")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title(f"Hasil Segmentasi Threshold (T={threshold_value})")
plt.imshow(binary_image, cmap="gray")
plt.axis("off")

plt.tight_layout()
plt.show()
