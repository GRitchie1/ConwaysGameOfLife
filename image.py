from PIL import Image
import numpy as np


class Image_Array():
    def __init__(self, image):
        self.image = image
        self.convertToBW()
        self.exportImage()
    
    def imageSizes(self):
        return [len(self.grid_array), len(self.grid_array[0])]

    def convertToBW(self):
        col = Image.open(self.image)
        gray = col.convert('L')
        
        bw = np.asarray(gray).copy()
        bw[bw < 128] = 0    # Off
        bw[bw >= 128] = 1 # On
        self.grid_array = bw

    def getArray(self):
        return self.grid_array

    def exportImage(self):
        img = np.asarray(self.grid_array).copy()
        img[img == 0] = 0    # Off
        img[img == 1] = 255 # On
        imfile = Image.fromarray(img)
        imfile.save("result_bw.png")
        