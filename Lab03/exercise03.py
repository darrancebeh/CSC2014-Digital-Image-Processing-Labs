import cv2
import numpy as np

INPUT_IMAGE_PATH = 'Lab03/images/ufo.bmp'
OUTPUT_IMAGE_PATH = 'Lab03/solution_img/baboon.bmp'

img_ufo = cv2.imread(INPUT_IMAGE_PATH, cv2.IMREAD_GRAYSCALE)

# alpha is contrast control
alpha = 2.5

#beta is brightness control
beta = 50

img_zeros = np.zeros_like(img_ufo)

# cv2.addWeighted: output = img_ufo*alpha + img_zeros*0 + beta
img_contrast_adjusted = cv2.addWeighted(img_ufo, alpha, img_zeros, 0, beta)

cv2.imshow("Original UFO Image", img_ufo)
cv2.imshow("Contrasted UFO Image (Baboon)", img_contrast_adjusted)

cv2.imwrite(OUTPUT_IMAGE_PATH, img_contrast_adjusted)
print(f"Adjusted image saved as '{OUTPUT_IMAGE_PATH}'")

cv2.waitKey(0)
cv2.destroyAllWindows()