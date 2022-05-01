import numpy as np
import cv2

def showimage(img):
    
    from matplotlib import pyplot as plt
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()


def main():
   
    obj_img = cv2.imread("imgs/goku.jpg") #obj_img = cv2.imread("imgs/goku.jpg", 0) deixa a imagem em preto e branco.
    showimage(obj_img) 
main()
