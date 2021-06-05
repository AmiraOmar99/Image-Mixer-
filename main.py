import PyQt5.QtGui
from PyQt5 import  QtWidgets
import mainUI
from Image import Image
from mixer import Mixer
from uiElements import Ui
import numpy as np
import sys
import pyqtgraph as pg
import logging

#Create and configure logger
logging.basicConfig(filename="logging.log", format='%(asctime)s %(message)s',filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class MainWindow(QtWidgets.QMainWindow, mainUI.Ui_MainWindow):
    def __init__(self):
        logger.debug('Program Execution')
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.ui_elements = Ui(self)
        self.showMaximized()
        self.show()
        self.images = {0: None, 1:None} 
        self.size = None
        self.imgs=0
        self.mixer=None

########connections
        self.btn_open1.clicked.connect(lambda: self.open_img(0))
        self.btn_open2.clicked.connect(lambda: self.open_img(1))
        
        for index , combo in enumerate(self.ui_elements.img_combos):
            self.connect_img_combos(index)


    def connect_img_combos(self, index):
        self.ui_elements.img_combos[index].currentIndexChanged.connect(lambda :self.img_comp(index))

    
    def img_comp(self, index):
        logger.debug('plotting {} of image {}'.format(self.ui_elements.img_combos[index].currentText(), index+1))
        comp_index = self.ui_elements.img_combos[index].currentIndex()
        self.images[index].show(self.ui_elements.components[index],self.images[index].comps[comp_index])


    def check_opened(self):
        if self.mixer == None:
            logger.debug("Checking if the user opens the 2 images")
            if self.images[0] != None and self.images[1] != None:
                # create mixer object
                self.mixer = Mixer(self) # pass self (main object) to mixer
        else:
            self.mixer.update()
            

        

    def open_img(self,index):
        logger.debug('open image {}'.format(index+1))
        img_path = PyQt5.QtWidgets.QFileDialog.getOpenFileName(None, 'open image', None, "PNG *.png;; JPG *.jpg")[0]
        if img_path:
            logger.info('Opening image : '+ img_path )
            image= Image()
            image.read(img_path)
            #check size
            if self.size_check(image,index):
                self.images[index]=image
                self.size = image.img_shape #if only one image save size
                logger.debug("opened")
                #show original image and its combonents
                self.images[index].show(self.ui_elements.originals[index],self.images[index].img_data)
                self.img_comp(index)
                self.ui_elements.img_combos[index].setEnabled(True)

            else:
                logger.debug('Not same size')
                msg = PyQt5.QtWidgets.QMessageBox()
                msg.setWindowTitle('ERROR')
                msg.setText('Error: please select an image of the same size as the other opened image')
                msg.setIcon(PyQt5.QtWidgets.QMessageBox.Critical)
                msg.exec_()
                #logger.ERROR("Not Same Size")
        else:
            logger.debug("canceled")

        self.check_opened()
         

    def size_check(self,image,index ):
        logger.debug('check image {} size '.format(index+1))
        #check if there is more than one image opened , if same size return 1
        if self.size:
            if (index == 0 and self.images[1]) or (index == 1 and self.images[0]):
                logger.debug("there is another image obened")
                if image.img_shape == self.size:
                    logger.debug("same size")
                    return 1
                else:
                    logger.debug("not same size")
                    return 0
            else:
                self.size = image.img_shape
                logger.debug("no other image")
                return 1
            
        else:
            logger.debug('image size is'+str(self.size))
            return 1 



def main():
    app = QtWidgets.QApplication(sys.argv)
    application = MainWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()