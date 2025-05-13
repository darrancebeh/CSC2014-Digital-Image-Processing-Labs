import cv2
import numpy as np

IMAGE_SIZE = 512
BORDER_THICKNESS = 64
BABOON_IMAGE_PATH = 'Lab03/solution_img/baboon.bmp'

inner_square_size = IMAGE_SIZE - (2 * BORDER_THICKNESS)

mask = np.zeros((IMAGE_SIZE, IMAGE_SIZE), dtype=np.uint8)

start_coord = BORDER_THICKNESS
end_coord = BORDER_THICKNESS + inner_square_size
mask[start_coord:end_coord, start_coord:end_coord] = 255

img_baboon = cv2.imread(BABOON_IMAGE_PATH)
masked_baboon = cv2.bitwise_and(img_baboon, img_baboon, mask=mask)

cv2.imshow("Original Baboon Image", img_baboon)
cv2.imshow("Generated Mask", mask)
cv2.imshow("Masked Baboon (Logical AND)", masked_baboon)

cv2.imwrite('Lab03/solution_img/c03_generated_mask.png', mask)
cv2.imwrite('Lab03/solution_img/c03_masked_baboon.png', masked_baboon)

cv2.waitKey(0)
cv2.destroyAllWindows()