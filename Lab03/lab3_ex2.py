import cv2
import numpy as np

IMAGE_PATH_1 = 'Lab03/images/word1.bmp'
IMAGE_PATH_2 = 'Lab03/images/word2.bmp'
IMAGE_PATH_3 = 'Lab03/images/word3.bmp'
OUTPUT_WINDOW_NAME = 'Combined Words'

img1 = cv2.imread(IMAGE_PATH_1)
img2 = cv2.imread(IMAGE_PATH_2)
img3 = cv2.imread(IMAGE_PATH_3)

img1_f64 = img1.astype(np.float64)
img2_f64 = img2.astype(np.float64)
img3_f64 = img3.astype(np.float64)

temp_sum_f64 = cv2.add(img1_f64, img2_f64)
sum_image_f64 = cv2.add(temp_sum_f64, img3_f64)

max_value = sum_image_f64.max()
scaled_image_f64 = (sum_image_f64 / max_value) * 255.0

final_image_uint8 = scaled_image_f64.astype(np.uint8)

cv2.imshow(OUTPUT_WINDOW_NAME, final_image_uint8)
cv2.waitKey(0)
cv2.destroyAllWindows()