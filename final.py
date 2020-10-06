import cv2 as cv
import numpy as np
from PIL import Image

import pytesseract as pt
from pytesseract import Output
import os



# Create an Image object from an Image

imageObject = Image.open("D:/TRF IP TASK/ocr/images/final2.jpg")

imgo=cv.resize(cv.imread('D:/TRF IP TASK/ocr/images/final2.jpg',0 ),(550,700))
cut=cv.resize(cv.imread('D:/TRF IP TASK/ocr/images/final2.jpg' ,0),(550,700))

edges = cv.Canny(imgo,50,150,apertureSize = 3)
#cv.imshow("asdasd",edges)
lines = cv.HoughLines(edges,1,np.pi/180, 200)
r1=[]
theta1=[]
index1=[]
print(lines)
for i in range(len(lines)):
        r1.append(lines[i][0][0])
        theta1.append(lines[i][0][1])
#print(r1.index(min(r1)))
print(int(min(r1)))
index1.append(r1.index(min(r1)))
index1.append(r1.index(max(r1)))
coor=[]
#print(theta1)
#print(lines[1][0][0])
for i in  index1:
        for r, theta in lines[i]:
            # Stores the value of cos(theta) in at
                #print("r---",r)
                #print("theta---",theta)
                a = np.cos(theta)

                # Stores the value of sin(theta) in b
                b = np.sin(theta)

                # x0 stores the value rcos(theta)
                x0 = a * r

                # y0 stores the value rsin(theta)
                y0 = b * r
                print(x0,y0)
                # x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
                x1 = int(x0 + 600 * (-b))

                # y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
                y1 = int(y0 + 600 * (a))

                # x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
                x2 = int(x0 - 1000 * (-b))

                # y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
                y2 = int(y0 - 1000 * (a))

                # cv2.line draws a line in img from the point(x1,y1) to (x2,y2).
                # (0,0,255) denotes the colour of the line to be
                # drawn. In this case, it is red.
                print("x1--",x1,"y1--",y1,"x2--",x2,"y2---",y2)
                imgo=cv.line(imgo, (x1, y1), (x2, y2), (0, 0, 255), 2)
                coor.append(x1)
                coor.append(y1)
                coor.append(x2)
                coor.append(y2)


dst1 = imgo[int(min(r1)):int(max(r1)), 0:600]
cv.imshow("print", imgo)
cv.imshow("per",dst1 )

# written on a new image houghlines.jpg

cv.imwrite('D:/TRF IP TASK/ocr/final/linesDetected.jpg', dst1)

#------------------------------------------------------
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

cl1 = clahe.apply(dst1)
cv.imwrite('D:/TRF IP TASK/ocr/final/linesDetected1.jpg', cl1)

#-------------------------------------------------------

'''cv.waitKey(0)
cv.destroyAllWindows()'''
#-------------------------------------------------------

pt.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
def main():
    print("---------")
    # path for the folder for getting the raw images
    path =("D:/TRF IP TASK/ocr/final/") #add the location of input images in this
    print("---------")
    # link to the file in which output needs to be kept
    tempPath =("D:/TRF IP TASK/ocr/text") #add the location of output images in this
    # iterating the images inside the folder
    print("---------")
    for imageName in os.listdir(path):
        print("------")
        inputPath = os.path.join(path, imageName)
        img = Image.open(inputPath)
        img = np.array(img)
        h, w = img.shape
        #cv2.imshow("sdjf",img)

        # applying ocr using pytesseract for python
        #text = pt.image_to_string(img, lang ="eng")

        custom_config = r'--oem 3 --psm 6'
        text = pt.image_to_string(img,config=custom_config)

        d = pt.image_to_data(img, output_type=Output.DICT)
        n_boxes = len(d['text'])
       



        fullTempPath = os.path.join(tempPath, 'time_' + imageName + ".txt")
        # print(text)

        # saving the  text for every image in a separate .txt file
        file1 = open(fullTempPath, "w")
        file1.write(text)
        file1.close()
        img=cv.resize(img,(600,800))
        cv.imshow('img', img)
        cv.waitKey(0)
cv.waitKey(0)
cv.destroyAllWindows()
if __name__ == '__main__':
    main()




#-----------------------------------------------------

filename="D:/TRF IP TASK/ocr/text/time_linesDetected.jpg.txt"
string1 = 'RED BLOOD CELLS'
lenght1=len(string1)
string='WHITE BLODD CELLS'
lenght2=len(string)



with open(filename) as myFile:
# for find count in the from of  RED BLOOD CELLS
    out=[]
    for num, line in enumerate(myFile, 1):
       # print(num,line)
        if string1 in line:
            out=line
            print(string1,end=' :')

            l=len(out)
    for j in range(lenght1+1,lenght1+4):
        if out[j].isnumeric():
            print(out[j],end='')
            print(out[j],end='')




    with open(filename) as myFile:    # for find count in the from of  WHITE BLOOD CELLS

        for num, line2 in enumerate(myFile, 1):
           # print(num,line)
            if string in line2:
                out1=line2
                print("\n",string,end=' :')
                l2=len(out1)

        for k in range(lenght2+1,lenght2+4):

            if out1[k].isnumeric():
                print(out1[k],end='')


