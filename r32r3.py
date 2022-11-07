from matplotlib.pyplot import imshow
import cv2
import numpy as np

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# создать изображение 100x100
image = np.zeros((100, 100, 3), np.uint8)

# залить его зеленым цветом
color = GREEN
out_color = tuple(reversed(color))
image[:] = out_color

# вывести на экран
imshow(image)

# сохранить в файл image.jpg
cv2.imwrite('image.jpg', image)