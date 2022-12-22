import cv2 as cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pic = cv2.imread('city-full.jpeg')
    resizeScale = 0.15

    img = cv2.resize(pic, None, fx=resizeScale, fy=resizeScale, interpolation=cv2.INTER_LINEAR)

    height, width, channelsN = img.shape
    print(height, width, channelsN)

    h0 = w0 = 1
    picCounter = 1
    h_interval = height // 3
    w_interval = width // 3

    for h in range(h_interval-1, height-1, h_interval):
        w0 = 1
        for w in range(w_interval-1, width-1, w_interval):
            cropped_pic = img[h0:h, w0:w]
            cv2.imwrite(f"cropped/city-cropped{picCounter}.jpg", cropped_pic)
            w0 = w
            picCounter += 1
        h0 = h

    gSize = 2

    # show cropped pictures
    f, axarr = plt.subplots(gSize, gSize)
    for i in range(1, picCounter):
        pic = cv2.imread(f'cropped/city-cropped{i}.jpg')
        axarr[i // gSize - 1, i % gSize - 1].imshow(cv2.cvtColor(pic, cv2.COLOR_BGR2RGB))
        axarr[i // gSize - 1, i % gSize - 1].axis('off')
    plt.show()