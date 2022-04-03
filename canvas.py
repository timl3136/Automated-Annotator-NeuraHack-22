import numpy as np
import cv2
from PIL import Image


def create_canvas(background_path, size):
    background = cv2.imread(background_path)

    size = size
    window_name = "canvas"

    # shade
    white = np.zeros(background.shape, dtype=np.uint8)
    white.fill(255)

    background = cv2.addWeighted(white, 0.7, background, 0.3, 0)

    cv2.namedWindow(window_name)
    cv2.imshow(window_name, background)

    return background

    

def draw(x, y, b, g, r, size, background):

    hf = size / 2
    sp = (int(x - hf), int(y - hf))
    ep = (int(x + hf), int(y + hf))

    cv2.rectangle(background, sp, ep, (b, g, r), -1)
    cv2.imshow("canvas", background)




if __name__ == "__main__":

    test_canvas = create_canvas("dog.png", 10)

    x, y = 8, 8
    b, g, r = 0, 0, 255
    import time

    for i in range(10):
        key = cv2.waitKey(1) & 0xff
        if key==ord('q'):
            break

        draw(i * x, i * y, b, g, r, 10, test_canvas)
        # print(i)
        time.sleep(2)

    cv2.destroyAllWindows()
    # cv2.waitKey(0)
    # test_canvas.close()
    



