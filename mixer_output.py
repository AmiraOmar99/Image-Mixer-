from PyQt5 import  QtWidgets
import logging
import numpy as np
import pyqtgraph as pg
from Image import Image
logger = logging.getLogger()


class Mixer():
    def __init__(self,win) :
        self.image_test=Image()
        self.images = {0: None, 1:None} #store image path and object
        
        self.originals = [ win.original_1, win.original_2]
        self.components = [ win.components_p1, win.components_p2]
        self.outputs = [ win.output1, win.output2]
        self.plots=[self.originals,self.components,self.outputs]
        self.sliders = [win.slider1,win.slider2]
        self.sliders_txts=[win.slider1_text, win.slider2_text]

        ##WIndow Elements##
        self.img_combos=[win.comboBox_components1 , win.comboBox_components2]
        self.img_mixer_combos=[win.Mixer_components1   , win.Mixer_components2 ]
        self.img_slider_combos=[win.Img_compo1  , win.Img_compo2 ]
        self.Combo_output=[win.comboBox_outputs]

        self.mixing_items=[self.img_mixer_combos,self.img_slider_combos,self.Combo_output,self.sliders,self.img_combos] #items to be enabled after uploading 2 images

        self.selectedImages = [0, 0]
        self.selectedComponents = ["Magnitude", "Phase"]
        self.scaleValues = [0.5, 0.5]
        self.recievedData = [None, None]
        self.selectedOutput = 0
        self.ouputImages = [None, None]

        for plot in self.plots:
            self.init_plots(plot)

        for item in self.mixing_items:
                self.disable_elem(item)    

        # self.disable_elem(self.img_combos)
        # self.disable_elem(self.img_mixer_combos)
        # self.disable_elem(self.img_slider_combos)
        # self.disable_elem(self.Combo_output)
        # self.disable_elem(self.sliders)

        self.config_sliders()

    def setFunctions(self, index):

        self.img_slider_combos[index].activated[str].connect(lambda: self.selectImage(index))
        self.img_mixer_combos[index].activated[str].connect(lambda: self.selectComponent(index))
        self.sliders[index].valueChanged.connect(lambda: self.sliderMoved(index))
        self.sliders[index].sliderReleased.connect(lambda: self.sliderReleased(index))
        self.Combo_output[0].activated[str].connect(lambda: self.showOutput(self.Select_Output()))

    def init_plots(self,plot_list):
        for plot in plot_list:
            plot.showAxis('bottom', False)
            plot.showAxis('left', False)
            plot.setBackground('w')
    
    def config_sliders(self):
        for i , slider in enumerate(self.sliders):
            slider.setMinimum(0)
            slider.setMaximum(100)
            slider.setSingleStep(10)
            slider.setTickInterval(10)
            slider.setValue(50)
            #self.sliders_txts[i].setText(str(slider.value()))

    def disable_elem(self,element_list):
        for element in element_list:
            element.setDisabled(True)

    def enable_elem(self,element_list):
        for element in element_list:
            element.setEnabled(True)


    def selectImage(self, index):
        logger.debug("selecting image from which we choose the component")
        self.selectedImage = self.img_slider_combos[index].currentText()
        if self.selectedImage == "Image1":
            self.selectedImages[index] = 0
        elif self.selectedImage == "Image2":
            self.selectedImages[index] = 1
        logger.info("Image Combobox {} has changed to {}".format(index+1, self.selectedImages[index]+1))
        #print("Image Combobox {} has changed to {}".format(index+1, self.selectedImages[index]+1))
        self.showOutput(self.Select_Output())

    def sliderMoved(self, index):
        logger.info("Slider {}, Value {}".format(index, self.sliders[index].value()))
        #print("Slider {}, Value {}".format(index, self.sliders[index].value()))
        self.scaleValues[index] = self.sliders[index].value()/100
        #print(self.scaleValues[index])
        self.sliders_txts[index].setText(str(self.sliders[index].value())+" %")
        self.showOutput(self.Select_Output())

    def sliderReleased(self, index):

        logger.info("Slider {} moved to {}%".format(index+1, self.sliders[index].value()))
        scale1 = self.scaleValues[0]
        scale2 = self.scaleValues[1]
        comp1 = self.selectedComponents[0]
        comp2 = self.selectedComponents[1]
        index1 = self.selectedImages[0]
        index2 = self.selectedImages[1]
        logger.info("Mixing {} of {} of Image {} with {} of {} of Image {}".format(scale1, comp1, index1+1, scale2, comp2, index2+1)) 

    def selectComponent(self, index):

        selectedComponent = self.img_mixer_combos[index].currentText()
        self.selectedComponents[index] = selectedComponent
        if index == 0:
            mixType = self.getAbbreviation(selectedComponent)
            #print(mixType)
            self.setSecondCompo(mixType)
            self.selectedComponents[1] = self.img_mixer_combos[1].currentText()
            self.sliders[1].setEnabled(True)
        if selectedComponent == "Uni Mag" or selectedComponent == "Uni Phase":
            self.sliders[index].setEnabled(False)
        else:
            self.sliders[index].setEnabled(True)
        logger.debug("Component ComboBox {} of image {} changed to Image {}".format(index+1, self.selectedImages[index]+1, selectedComponent))
        self.showOutput(self.Select_Output())

    def setComponentCompo(self, index, mixType):
        logger.debug("adjusting items of combobox 2 according to component chosen in 1 ")
        if index == 1:
            self.setSecondCompo(mixType)

    def clearCompo(self,index):

        logger.debug("clears the items of the combobox")
        for i in range(self.img_mixer_combos[index].count()):
            self.img_mixer_combos[index].removeItem(0)

    def setSecondCompo(self, mixType):
        logger.debug("Changing items of combobox 2 according to component chosen from combobox 1")
        self.clearCompo(1)
        if mixType == "m" or mixType == "um":
            self.img_mixer_combos[1].addItem("Phase")
            self.img_mixer_combos[1].addItem("Uni Phase")

        elif mixType == "p" or mixType == "up":
            self.img_mixer_combos[1].addItem("Magnitude")
            self.img_mixer_combos[1].addItem("Uni Mag")

        elif mixType == "r":
            self.img_mixer_combos[1].addItem("Imaginary")

        elif mixType == "i":
            self.img_mixer_combos[1].addItem("Real")

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
            mixType1 = self.getAbbreviation(self.selectedComponents[0])
            mixType2 = self.getAbbreviation(self.selectedComponents[1])
            # print(mixType1, mixType2)
            selected1 = self.selectedImages[0]
            selected2 = self.selectedImages[1]
            mixer1 = self.getMixers(self.images[selected1], self.images[selected2], mixType1,self.scaleValues[0])

            mixer2 = self.getMixers(self.images[selected2], self.images[selected1], mixType2,self.scaleValues[1])
            result = self.multiplyMixers(mixer1, mixer2, mixType1)
            self.image_test.img_data= np.abs(np.fft.ifft2(result))
            self.image_test.show(self.outputs[index],self.image_test.img_data)
            #imagedata = np.abs(np.fft.ifft2(result))
            #self.show_result(self.outputs[index],imagedata)
            
    def Select_Output(self):
        logger.debug("Where to show the output")
        
        if self.Combo_output[0].currentText() =="Output1" :
            output_result= 0
            #print("Output1")
        elif self.Combo_output[0].currentText() =="Output2" :
            output_result =1 
            #print("Output2")
        return output_result


    


    







    

    
        
        

