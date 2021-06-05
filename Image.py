import cv2
import numpy as np
import logging
import pyqtgraph as pg

logger = logging.getLogger()

class Image():
    def __init__(self):
        self.img_data =None
        self.img_shape=None
        self.magnitude=None
        self.phase=None
        self.real=None
        self.imaginary=None

    def read(self,path):
        self.img_data = cv2.imread(path,0)
        self.img_shape=self.img_data.shape
        logger.info("image shape is"+str(self.img_shape))
        self.img_fft = np.fft.fft2(self.img_data)
        self.magnitude = np.abs(self.img_fft)
        self.phase = np.angle(self.img_fft)
        self.real = self.img_fft.real
        self.imaginary = self.img_fft.imag
        self.img_fftshift = np.fft.fftshift(self.img_fft)
        self.comps=[np.log(np.abs(self.img_fftshift)+1) , np.angle(self.img_fftshift) , np.log(self.img_fftshift.real+1) , np.log(self.img_fftshift.imag+1)]
    
    def show(self,plot,data):
        self.plot=plot
        self.plot.clear()
        self.plot.invertY(True)
        self.image_item = pg.ImageItem(data.T)
        self.plot.addItem(self.image_item)
        self.plot.autoRange(padding=0)


class Output(Image):
    def __init__(self):
        super().__init__()


