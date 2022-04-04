import numpy as np
import cv2
import pandas as pd
import time
import os


def create_canvas(background_path):
    background = cv2.imread(background_path)

    window_name = "canvas"

    # shade
    white = np.zeros(background.shape, dtype=np.uint8)
    white.fill(255)

    background = cv2.addWeighted(white, 0.7, background, 0.3, 0)

    cv2.namedWindow(window_name)
    cv2.imshow(window_name, background)

    return background


def draw(x, y, b, g, r, length, height, background):

    sp = x,y
    ep = x+length, y+height

    cv2.rectangle(background, sp, ep, (b, g, r), -1)
    cv2.imshow("canvas", background)


def random_color():
    import random
    rand = random.randrange(0,20)
    color = [(0, 255, 0), (78, 247, 0), (109, 238, 0), (131, 230, 0), (149, 221, 0), (164, 212, 0), 
    (178, 202, 0), (190, 192, 0), (200, 182, 0), (210, 172, 0), (219, 161, 0), (227, 150, 0), (233, 138, 0), (239, 126, 0),
    (244, 112, 0), (248, 99, 0), (252, 83, 0), (254, 66, 0), (255, 44, 0), (255, 0, 0)]
    return color[rand]

def color_generate(data):
    np.random.rand(42)
    weight = np.random.rand(8,30)
    bias = np.random.rand(30)
    def sigmoid(x):
        z = np.exp(-x)
        sig = 1 / (1 + z)
        return sig
    color = [(0, 255, 0), (78, 247, 0), (109, 238, 0), (131, 230, 0), (149, 221, 0), (164, 212, 0), 
    (178, 202, 0), (190, 192, 0), (200, 182, 0), (210, 172, 0), (219, 161, 0), (227, 150, 0), (233, 138, 0), (239, 126, 0),
    (244, 112, 0), (248, 99, 0), (252, 83, 0), (254, 66, 0), (255, 44, 0), (255, 0, 0)]
    res = np.mean(np.dot(data, weight) + bias) - 38610
    print(res)
    res = sigmoid(res)
    print(res)
    return color[int(res*20)]


if __name__ == "__main__":

    data = pd.read_csv('data.csv')

    image_list = [os.path.join('pic', p) for p in os.listdir('pic')]
    print(image_list)
    row_idx = 0

    for image in (image_list):
        temp_canvas = create_canvas(image)
        x, y = 0,0
        canvas_size = temp_canvas.shape
        print(canvas_size)
        num_row, num_col = 4,5
        length, height = int(canvas_size[1]/num_col), int(canvas_size[0]/num_row)
        
        
        for row in range(num_row):
            for col in range(num_col):
                key = cv2.waitKey(1) & 0xff
                if key==ord('q'):
                    break
                df = data.loc[row_idx*100:(row_idx+1)*100].to_numpy()
                r, g, b = random_color()
                draw(x+col * length, y+row * height, b, g, r, length, height, temp_canvas)
                row_idx += 1
                time.sleep(0.5)

        cv2.waitKey(1)
        time.sleep(10)
        cv2.destroyAllWindows()

    # test_canvas.close()
    



