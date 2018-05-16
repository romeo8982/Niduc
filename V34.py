import scrambler
import cv2
from Histogram import Histogram
from Bit_Counter import BitCounter
import numpy as np
V34 = scrambler.Additive(13, 14, 15, 49)     # tworze scrambler
syncseq = int("11111111", 2)    # 8 bitowa sekwencja synchronizujaca
truebyte = int("11111111", 2)   # to tu jest na wszelki wypadek
currentseq = 0  # zmienna do okreslania sekwencji
img = cv2.imread('lul.jpg')
shp = img.shape
cv2.imshow("scrambled", img)
cv2.waitKey()
cv2.destroyAllWindows()
img.resize(img.size)
helpchar = ""   # pomocnicza zmienna do odkrecania scramblu sync
# petla glowna
print("")
for x in range(0, img.size):
    if x % (img.size/10) == 0:
        print("-")
    if x % 9 == 0:
        V34.initialState()
    znak = img[x]     # zmienna do przechowywania pojedynczego chara do scrambl
    data = znak      # wartosc chara
    znak = V34.scramble(znak)
    # po scramblowaniu chara sprawdzam czy wystapila sekwencja
    for y in range(0, 8):
        currentseq = currentseq >> 1 | (data >> y & 1) << 7
        if currentseq == syncseq:
            currentseq = 0 # posluzy za pomocnicza zmienna i tak juz tego nie potrzebujemy
            #nastepne 2 petle przygotowuja ciagi bitow tak by przykryc zescramblowana sekwencje w poprzednim i we wlasciwym bajcie np 11100000 i 00011111
            for i in range(0, y+1):
                currentseq = currentseq << 1
                currentseq += 1
            znak = znak | currentseq
            currentseq = 0
            try:
                helpchar = img[x-1]  # poprzedni zescramblowany znak
                for i in range(0, 8):
                    currentseq = currentseq << 1
                    if 8 - i > y + 1:
                        currentseq += 1
                helpchar = helpchar | currentseq
                img[x-1] = helpchar
            except:
                pass
            currentseq = 0
            #zapis poprawionych bajtow
    img[x] = znak

img.resize(shp)
print("")
cv2.imshow("scrambled", img)
cv2.waitKey()
cv2.destroyAllWindows()
img.resize(img.size)
his_bit = BitCounter(img)
his = Histogram(his_bit.list_of_ones, '1')
his = Histogram(his_bit.list_of_zeros, '0')
V34.initialState()
currentseq = 0
for x in range(0, img.size):
    if x % (img.size / 10) == 0:
        print("%")
    if x % 9 == 0:
        V34.initialState()
    znak = img[x]
    data = znak
    znak = V34.scramble(znak)
    for y in range(0, 8):
        currentseq = currentseq >> 1 | (data >> y & 1) << 7
        if currentseq == syncseq:
            currentseq = 0
            for i in range(0, y + 1):
                currentseq = currentseq << 1
                currentseq += 1
            znak = znak | currentseq
            currentseq = 0
            try:
                helpchar = img[x-1]
                for i in range(0, 8):
                    currentseq = currentseq << 1
                    if 8 - i > y + 1:
                        currentseq += 1
                helpchar = helpchar | currentseq
                img[x-1] = helpchar
            except:
                pass
            currentseq = 0
    img[x] = znak
img.resize(shp)
cv2.imshow("unscrambled", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
