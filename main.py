import PyQt5.QtGui
from PyQt5 import  QtWidgets
import mainUI
from Image import Image
from Image import Output

from uiElements import Ui
import sys
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
        self.ui_elements=Ui(self)
        self.show()
        self.images = {0: None, 1:None} #store image path and object
        self.size = None
        self.imgs=0
        
        
########connections
        self.btn_open1.clicked.connect(lambda: self.open_img(0))
        self.btn_open2.clicked.connect(lambda: self.open_img(1))
        # for slider in self.ui_elements.sliders:
        #     slider.valueChanged.connect() ##call self.ui_elements.config_slider in the slider change func
        
        self.comboBox_components1.currentIndexChanged.connect(lambda : self.img_comp(0))   
        self.comboBox_components2.currentIndexChanged.connect(lambda : self.img_comp(1))   

    def img_comp(self, index):
        logger.debug('plotting {} of image {}'.format(self.ui_elements.img_combos[index].currentText(), index+1))
        comp_index = self.ui_elements.img_combos[index].currentIndex()
        self.images[index].show(self.ui_elements.components[index],self.images[index].comps[comp_index])
        

        

    def open_img(self,index):
        logger.debug('open image {}'.format(index+1))
        img_path = PyQt5.QtWidgets.QFileDialog.getOpenFileName(None, 'open image', None, "PNG *.png;; JPG *.jpg")[0]
        if img_path:
            logger.info('Opening image : '+ img_path )
            self.images[index]= Image()
            self.images[index].read(img_path)
            if self.size_check(self.images[index],index):
                logger.debug("opened")
                #show original image and its combonents
                self.images[index].show(self.ui_elements.originals[index],self.images[index].img_data)
                self.img_comp(index)
                self.ui_elements.img_combos[index].setEnabled(True)

            else:
                del self.images[index]
                self.images[index]=None
                logger.debug('Not same size')
                msg = PyQt5.QtWidgets.QMessageBox()
                msg.setWindowTitle('ERROR')
                msg.setText('Error: please select an image of the same size as the other opened image')
                msg.setIcon(PyQt5.QtWidgets.QMessageBox.Critical)
                msg.exec_()
                self.logger.ERROR("Not Same Size")
        else:
            self.logger.debug("canceled")

                   

    def size_check(self,image,index):
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
                logger.debug("no other image")
                return 1
            
        else:
            self.size = image.img_shape #if only one image save size
            logger.debug('image size is'+str(self.size))
            return 1 

    


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = MainWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
