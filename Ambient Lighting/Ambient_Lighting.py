
from PIL import ImageGrab
import time
import numpy as np
import cv2
import sys
import matplotlib.pyplot as plt
import serial
ser = serial.Serial(port="COM4",baudrate=9600)

while True:  # petla zakonczy sie w momencie gdy nacisniemy przycisk q

    t0=time.perf_counter()
    imgTOP = ImageGrab.grab(bbox=(0, 0, 1920, 150))  # podzial lapania ekranu na 4 strefy
    imgBOT = ImageGrab.grab(bbox=(0, 930, 1920, 1080))
    imgLEFT = ImageGrab.grab(bbox=(0, 0, 150, 1080))
    imgRIGHT = ImageGrab.grab(bbox=(1770, 0, 1920, 1080))
    img_npTOP = np.array(imgTOP)
    img_npBOT = np.array(imgBOT)
    img_npLEFT = np.array(imgLEFT)
    img_npRIGHT = np.array(imgRIGHT)

    frameTOP = cv2.cvtColor(img_npTOP,cv2.COLOR_BGR2RGB)  # NP.array daje nam obraz BGR co zle wyswietla rzeczywiste kolory
                                                                  #            wiec zamieniamy z BGR na RGB
    frameBOT = cv2.cvtColor(img_npBOT, cv2.COLOR_BGR2RGB)
    frameLEFT = cv2.cvtColor(img_npLEFT, cv2.COLOR_BGR2RGB)
    frameRIGHT = cv2.cvtColor(img_npRIGHT, cv2.COLOR_BGR2RGB)

    #cv2.imshow("frameTOP", frameTOP)
    #cv2.imshow("frameBOT", frameBOT)
    #cv2.imshow("frameLEFT", frameLEFT)
    #cv2.imshow("frameRIGHT", frameRIGHT)

    averagebot = img_npBOT.mean(axis=0).mean(axis=0)
    averagetop = img_npTOP.mean(axis=0).mean(axis=0)
    averageleft = img_npLEFT.mean(axis=0).mean(axis=0)
    average = img_npRIGHT.mean(axis=0).mean(axis=0)
    #pixels = np.float32(img_npRIGHT.reshape(-1,3))
    #n_colors = 5
    #riteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    #flags = cv2.KMEANS_RANDOM_CENTERS

    #_, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)      #wyznacza n_colors dominujacych kolorow
   # _, counts = np.unique(labels, return_counts=True)       # wyznacza nam wskazniki na konkretne wartosci RGB i zlicza ile ich jest
   # dominant = palette[np.argmax(counts)]                   # wyznacza najczesciej pojawiajaca sie wartosc RGB


    averageR = int(average[0])
    averageG = int(average[1])
    averageB = int(average[2])

    averageR1 = str(averageR)
    averageG1 = str(averageG)
    averageB1 = str(averageB)

    averageend = '<'+averageR1+'-'+averageG1+'-'+averageB1+'>'
    #print(averageend)
    #print(palette)
    #print(counts)str(input_value).encode()
    #print(average)
    #print(averageR)
    #print(averageG)
   # print(averageB)
    
    ser.write((averageend.encode()))
    t1=time.perf_counter() - t0
    print("time elapsed:", t1-t0)

    #time.sleep(1)
    #ser.write((str(averageR).encode()))             #zamiana na tablice byte
    #ser.write((str(averageG)+'\n').encode())  
    #ser.write((str(averageB)+'\n').encode())  
    #print(dominant)
    #dominant_avgweight = np.average(palette,axis=0, weights=counts)             #srednia wayona kol. dominujacych
    #dominant_avg = palette.mean(axis=0)                                     
    #print(dominant_avg)
                                                                                #wizualizacja otrzymanych kolorow
    #avg_patch = np.ones(shape=img_npRIGHT.shape, dtype=np.uint8)*np.uint8(average)
    #domavgweight_patch = np.ones(shape=img_npRIGHT.shape, dtype=np.uint8)*np.uint8(dominant_avgweight)
    #domavg_patch = np.ones(shape=img_npRIGHT.shape, dtype=np.uint8)*np.uint8(dominant_avg)
    #indices = np.argsort(counts)[::-1]   
    #freqs = np.cumsum(np.hstack([[0], counts[indices]/float(counts.sum())]))
    #rows = np.int_(img_npRIGHT.shape[0]*freqs)
    #dom_patch = np.zeros(shape=img_npRIGHT.shape, dtype=np.uint8)
    #for i in range(len(rows) - 1):
    	#dom_patch[rows[i]:rows[i + 1], :, :] += np.uint8(palette[indices[i]])
    #fig, (ax0, ax1, ax3, ax4) = plt.subplots(1, 4, figsize=(12,6))
    #ax0.imshow(avg_patch)
    #ax0.set_title('Average color')
    #ax0.axis('off')
    #ax1.imshow(dom_patch)
    #ax1.set_title('Dominant colors')
    #ax1.axis('off')
    #ax3.imshow(domavg_patch)
    #ax3.set_title('Dominantavgweight color')
    #ax3.axis('off')
    #ax4.imshow(domavgweight_patch)
    #ax4.set_title('Dominantavgweight color')
    #ax4.axis('off')
    #plt.show()



    



    #avg_color_per_row = np.average(img_npBOT, axis=0)
    #avg_color = np.average(avg_color_per_row, axis=0)
    
    #print(avg_color)
    #print(np.mean(img_npBOT,axis=0))

# print(int(img_npTOP))

# print(frame[500,500])
# print(frame.shape)
# small_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)


# np.average(frame)
# h, w = frame.shape

# srednia= 1 liczba R+G+B/3
# R=x G=y B=z


# cv2.imshow("frame",small_frame)                            #pokazuje nam lapany obraz ekranu

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destoryAllWindows()