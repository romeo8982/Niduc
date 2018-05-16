import scrambler
import cv2
from Histogram import Histogram
from Bit_Counter import BitCounter
import numpy as np
dvb = scrambler.Additive(13, 14, 15, 49)     # tworze scrambler
img = cv2.imread('lul.jpg')
shp = img.shape
cv2.imshow("scrambled", img)
cv2.waitKey()
cv2.destroyAllWindows()
img.resize(img.size)
helpchar = ""   # pomocnicza zmienna do odkrecania scramblu sync
# petla glowna
print("")
counter = 0
for x in range(img.size):
    if x % (img.size/10) == 0:
        counter += 10
        print(counter, "%")
    img[x] = dvb.scrambleIn(img[x])

img.resize(shp)
print("")
cv2.imshow("scrambled", img)
cv2.waitKey()
cv2.destroyAllWindows()
img.resize(img.size)
his_bit = BitCounter(img)
his = Histogram(his_bit.list_of_ones, '1')
dvb.initialState()
counter = 0
for x in range(img.size):
    if x % (img.size/10) == 0:
        counter += 10
        print(counter, "%")
    img[x] = dvb.scrambleOut(img[x])
print("")
img.resize(shp)
cv2.imshow("scrambled", img)
cv2.waitKey()
cv2.destroyAllWindows()
img.resize(img.size)
