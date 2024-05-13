import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Define image size
width, height = 256, 256

# Create grid of coordinates for the image
x = np.linspace(-3, 3, width)
y = np.linspace(-3, 3, height)
x, y = np.meshgrid(x, y)
# Create a 2D Gaussian distribution
sigma = 1.0
gaussian_kernel = np.exp(-(x**2 + y**2) / (2 * sigma**2))

# Normalize the kernel
gaussian_kernel /= np.sum(gaussian_kernel)

# Create a random image
image = np.random.rand(height, width)

# Convolve the image with the Gaussian kernel
gaussian_image = gaussian_filter(image, sigma=sigma)

# Plot the original and the Gaussian-filtered images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(gaussian_image, cmap='gray')
plt.title('Gaussian Filtered Image')
plt.axis('off')

plt.show()
