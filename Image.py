import cv2
import numpy as np
import logging

logger = logging.getLogger()

class Image():
    def __init__(self,path=None):
        logger.debug("create_image")
        self.im_path=path
        self.img_data = cv2.imread(path)
        self.img_shape=self.img_data.shape
        logger.info("image shape is"+str(self.img_shape))
        self.img_fft = np.fft.rfft2(self.img_data)
        self.magnitude = np.abs(self.img_fft)
        self.phase = np.angle(self.img_fft)
        self.real = self.img_fft.real
        self.imaginary = self.img_fft.imag
    
    def show_img(self):
        pass
    
    def plot_comp(self):
        pass



