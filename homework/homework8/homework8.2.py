import cv2
import numpy as np

points = np.zeros((100, 2), np.int32)
counter = 0
distPix = 0
mapScale = 300/168  # metres/pixels
textOrigin = (800, 62)


def draw_line(event, x, y, flags, params):
    global counter
    global distPix
    if event == cv2.EVENT_LBUTTONDOWN:
        points[counter] = x, y
        counter += 1
        cv2.circle(streetMap, (x, y), 3, (0, 0, 255), 2)
        # print(points)

        if counter >= 2:
            # connect last two points
            cv2.line(streetMap, points[counter - 2], points[counter - 1], (0, 0, 255), thickness=2, lineType=cv2.LINE_AA)

            # compute the distance beetween current and previos points
            distPix += np.sqrt(np.square(points[counter-2][0] - points[counter-1][0])
                               + np.square(points[counter-2][1] - points[counter-1][1]))


streetMap = cv2.imread('assets/map.png')

while True:

    cv2.imshow('Draw Path', streetMap)
    cv2.setMouseCallback('Draw Path', draw_line)

    k = cv2.waitKey(20) & 0xFF  # stop on ESC
    if k == 27:
        if counter >= 2:
            # print the distance of route converted to metres according to the map's scale factor
            distM = np.round(distPix * mapScale)
            print(distM)

            # adding annotation to the image
            text = f'{distM} m'
            cv2.putText(streetMap, text, textOrigin, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(0, 0, 255))

            # save your route map
            cv2.imwrite('distanceMap.png', streetMap)
        break
cv2.destroyAllWindows()