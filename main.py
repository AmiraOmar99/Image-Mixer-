import PyQt5.QtGui
from PyQt5 import  QtWidgets
import mainUI
from Image import Image
from Image import Output
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
        self.ui_elements=Ui(self)
        self.show()
        self.images = {0: None, 1:None} #store image path and object
        self.size = None
        self.imgs=0
        
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
        self.check_opened(self.images)


    def check_opened(self,image_objects):
        logger.debug("Checking if the user opens the 2 images")
        if self.images[0] != None and self.images[1] != None:
            self.ui_elements.enable_elem(self.ui_elements.img_mixer_combos)
            self.ui_elements.enable_elem(self.ui_elements.img_slider_combos)
            self.ui_elements.enable_elem(self.ui_elements.Combo_output)
            self.ui_elements.enable_elem(self.ui_elements.sliders)
            for i in range(2):
                self.setFunctions(i)
        self.showOutput(self.Select_Output())
            

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

    def selectImage(self, index):
        logger.debug("selecting image from which we choose the component")
        self.ui_elements.selectedImage = self.ui_elements.img_slider_combos[index].currentText()
        if self.ui_elements.selectedImage == "Image1":
            self.ui_elements.selectedImages[index] = 0
        elif self.ui_elements.selectedImage == "Image2":
            self.ui_elements.selectedImages[index] = 1
        logger.info("Image Combobox {} has changed to {}".format(index+1, self.ui_elements.selectedImages[index]+1))
        #print("Image Combobox {} has changed to {}".format(index+1, self.ui_elements.selectedImages[index]+1))
        self.showOutput(self.Select_Output())

    def setFunctions(self, index):

        self.ui_elements.img_slider_combos[index].activated[str].connect(lambda: self.selectImage(index))
        self.ui_elements.img_mixer_combos[index].activated[str].connect(lambda: self.selectComponent(index))
        self.ui_elements.sliders[index].valueChanged.connect(lambda: self.sliderMoved(index))
        self.ui_elements.sliders[index].sliderReleased.connect(lambda: self.sliderReleased(index))
        self.ui_elements.Combo_output[0].activated[str].connect(lambda: self.showOutput(self.Select_Output()))

    def sliderMoved(self, index):
        logger.info("Slider {}, Value {}".format(index, self.ui_elements.sliders[index].value()))
        #print("Slider {}, Value {}".format(index, self.ui_elements.sliders[index].value()))
        self.ui_elements.scaleValues[index] = self.ui_elements.sliders[index].value()/100
        #print(self.ui_elements.scaleValues[index])
        self.ui_elements.sliders_txts[index].setText(str(self.ui_elements.sliders[index].value())+" %")
        self.showOutput(self.Select_Output())

    def sliderReleased(self, index):

        logger.info("Slider {} moved to {}%".format(index+1, self.ui_elements.sliders[index].value()))
        scale1 = self.ui_elements.scaleValues[0]
        scale2 = self.ui_elements.scaleValues[1]
        comp1 = self.ui_elements.selectedComponents[0]
        comp2 = self.ui_elements.selectedComponents[1]
        index1 = self.ui_elements.selectedImages[0]
        index2 = self.ui_elements.selectedImages[1]
        logger.info("Mixing {} of {} of Image {} with {} of {} of Image {}".format(scale1, comp1, index1+1, scale2, comp2, index2+1))

    def selectComponent(self, index):

        selectedComponent = self.ui_elements.img_mixer_combos[index].currentText()
        self.ui_elements.selectedComponents[index] = selectedComponent
        if index == 0:
            mixType = self.getAbbreviation(selectedComponent)
            #print(mixType)
            self.setSecondCompo(mixType)
            self.ui_elements.selectedComponents[1] = self.ui_elements.img_mixer_combos[1].currentText()
            self.ui_elements.sliders[1].setEnabled(True)
        if selectedComponent == "Uni Mag" or selectedComponent == "Uni Phase":
            self.ui_elements.sliders[index].setEnabled(False)
        else:
            self.ui_elements.sliders[index].setEnabled(True)
        logger.debug("Component ComboBox {} of image {} changed to Image {}".format(index+1, self.ui_elements.selectedImages[index]+1, selectedComponent))
        self.showOutput(self.Select_Output())

    def setComponentCompo(self, index, mixType):
        logger.debug("adjusting items of combobox 2 according to component chosen in 1 ")
        if index == 1:
            self.setSecondCompo(mixType)

    def clearCompo(self,index):

        logger.debug("clears the items of the combobox")
        for i in range(self.ui_elements.img_mixer_combos[index].count()):
            self.ui_elements.img_mixer_combos[index].removeItem(0)

    def setSecondCompo(self, mixType):
        logger.debug("Changing items of combobox 2 according to component chosen from combobox 1")
        self.clearCompo(1)
        if mixType == "m" or mixType == "um":
            self.ui_elements.img_mixer_combos[1].addItem("Phase")
            self.ui_elements.img_mixer_combos[1].addItem("Uni Phase")

        elif mixType == "p" or mixType == "up":
            self.ui_elements.img_mixer_combos[1].addItem("Magnitude")
            self.ui_elements.img_mixer_combos[1].addItem("Uni Mag")

        elif mixType == "r":
            self.ui_elements.img_mixer_combos[1].addItem("Imaginary")

        elif mixType == "i":
            self.ui_elements.img_mixer_combos[1].addItem("Real")

    def getAbbreviation(self, comp):
        if comp == "Magnitude":
            mixType = "m"
        elif comp == "Phase":
            mixType = "p"
        elif comp == "Real":
            mixType = "r"
        elif comp == "Imaginary":
            mixType = "i"
        elif comp == "Uni Mag":
            mixType = "um"
        elif comp == "Uni Phase":
            mixType = "up"
        return mixType


    def getMixers(self, image1, image2, mixType, scale):
        logger.debug("checking the mixtype and scaling the component chosen")
        if mixType == "m":
            mixer = image1.magnitude * scale + image2.magnitude*(1-scale)
        elif mixType == "um":
            mixer = np.ones(image1.magnitude.shape)
        elif mixType == "p":
            mixer = image1.phase * scale + image2.phase * (1-scale)
        elif mixType == "up":
            mixer = np.zeros(image1.phase.shape)
        elif mixType == "r":
            mixer = image1.real * scale + image2.real * (1-scale)
        elif mixType == "i":
            mixer = image1.imaginary * scale + image2.imaginary * (1-scale)
        return mixer

    def multiplyMixers(self, mixer1, mixer2, mixType):

        logger.debug("combine the two mixers depending on the mixType")
        if mixType == "m" or mixType == "um":
            output = np.multiply(mixer1, np.exp(1j*mixer2))
        elif mixType == "p" or mixType == "up":
            output = np.multiply(mixer2, np.exp(1j*mixer1))
        elif mixType == "r":
            output = mixer1 + 1j*mixer2
        elif mixType == "i":
            output = mixer2 + 1j*mixer1
        return output

    def showOutput(self,index):

        logger.debug("Showing output image ")
        if self.images[0] != None and self.images[1] != None:
            mixType1 = self.getAbbreviation(self.ui_elements.selectedComponents[0])
            mixType2 = self.getAbbreviation(self.ui_elements.selectedComponents[1])
            # print(mixType1, mixType2)
            selected1 = self.ui_elements.selectedImages[0]
            selected2 = self.ui_elements.selectedImages[1]
            mixer1 = self.getMixers(self.images[selected1], self.images[selected2], mixType1,self.ui_elements.scaleValues[0])
            mixer2 = self.getMixers(self.images[selected2], self.images[selected1], mixType2,self.ui_elements.scaleValues[1])
            result = self.multiplyMixers(mixer1, mixer2, mixType1)
            imagedata = np.abs(np.fft.ifft2(result))
            self.show_result(self.ui_elements.outputs[index],imagedata)
            
    def Select_Output(self):
        logger.debug("Where to show the output")
        
        if self.ui_elements.Combo_output[0].currentText() =="Output1" :
            output_result= 0
            #print("Output1")
        elif self.ui_elements.Combo_output[0].currentText() =="Output2" :
            output_result =1 
            #print("Output2")
        return output_result

    def show_result(self,plot,data):
        self.plot=plot
        self.plot.clear()
        self.plot.invertY(True)
        self.image_item = pg.ImageItem(data.T)
        self.plot.addItem(self.image_item)
        self.plot.setXRange(min=0, max=data.shape[0], padding=0)
        self.plot.setYRange(min=0, max=data.shape[1], padding=0)
        self.plot.autoRange(padding=0)

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
