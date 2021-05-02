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
        self.comps=[np.log(np.abs(self.img_fftshift)) , np.angle(self.img_fftshift) , np.log(self.img_fftshift.real+1) , np.log(self.img_fftshift.imag+1)]
    
    def show(self,plot,data):
        self.plot=plot
        self.plot.clear()
        self.plot.invertY(True)
        self.image_item = pg.ImageItem(data.T)
        self.plot.addItem(self.image_item)
        self.plot.setXRange(min=0, max=data.shape[0], padding=0)
        self.plot.setYRange(min=0, max=data.shape[1], padding=0)
        self.plot.autoRange(padding=0)



# class Output(Image):
#     def __init__(self):
#         super().__init__()
#         self.ui_elements=Ui(self)

#     def selectImage(self, index):
#         logger.debug("selecting image from which we choose the component")
#         self.ui_elements.selectedImage = self.ui_elements.img_slider_combos[index].currentText()
#         if self.ui_elements.selectedImage == "Image1":
#             self.ui_elements.selectedImages[index] = 0
#         elif self.ui_elements.selectedImage == "Image2":
#             self.ui_elements.selectedImages[index] = 1
#         logger.info("Image Combobox {} has changed to {}".format(index+1, self.ui_elements.selectedImages[index]+1))
#         #print("Image Combobox {} has changed to {}".format(index+1, self.ui_elements.selectedImages[index]+1))
#         self.showOutput(self.Select_Output())

#     def sliderMoved(self, index):
#         logger.info("Slider {}, Value {}".format(index, self.ui_elements.sliders[index].value()))
#         #print("Slider {}, Value {}".format(index, self.ui_elements.sliders[index].value()))
#         self.ui_elements.scaleValues[index] = self.ui_elements.sliders[index].value()/100
#         #print(self.ui_elements.scaleValues[index])
#         self.ui_elements.sliders_txts[index].setText(str(self.ui_elements.sliders[index].value())+" %")
#         self.showOutput(self.Select_Output())

#     def sliderReleased(self, index):

#         logger.info("Slider {} moved to {}%".format(index+1, self.ui_elements.sliders[index].value()))
#         scale1 = self.ui_elements.scaleValues[0]
#         scale2 = self.ui_elements.scaleValues[1]
#         comp1 = self.ui_elements.selectedComponents[0]
#         comp2 = self.ui_elements.selectedComponents[1]
#         index1 = self.ui_elements.selectedImages[0]
#         index2 = self.ui_elements.selectedImages[1]
#         logger.info("Mixing {} of {} of Image {} with {} of {} of Image {}".format(scale1, comp1, index1+1, scale2, comp2, index2+1)) 

#     def selectComponent(self, index):

#         selectedComponent = self.ui_elements.img_mixer_combos[index].currentText()
#         self.ui_elements.selectedComponents[index] = selectedComponent
#         if index == 0:
#             mixType = self.getAbbreviation(selectedComponent)
#             #print(mixType)
#             self.setSecondCompo(mixType)
#             self.ui_elements.selectedComponents[1] = self.ui_elements.img_mixer_combos[1].currentText()
#             self.ui_elements.sliders[1].setEnabled(True)
#         if selectedComponent == "Uni Mag" or selectedComponent == "Uni Phase":
#             self.ui_elements.sliders[index].setEnabled(False)
#         else:
#             self.ui_elements.sliders[index].setEnabled(True)
#         logger.debug("Component ComboBox {} of image {} changed to Image {}".format(index+1, self.ui_elements.selectedImages[index]+1, selectedComponent))
#         self.showOutput(self.Select_Output())

#     def setComponentCompo(self, index, mixType):
#         logger.debug("adjusting items of combobox 2 according to component chosen in 1 ")
#         if index == 1:
#             self.setSecondCompo(mixType)

#     def clearCompo(self,index):

#         logger.debug("clears the items of the combobox")
#         for i in range(self.ui_elements.img_mixer_combos[index].count()):
#             self.ui_elements.img_mixer_combos[index].removeItem(0)

#     def setSecondCompo(self, mixType):
#         logger.debug("Changing items of combobox 2 according to component chosen from combobox 1")
#         self.clearCompo(1)
#         if mixType == "m" or mixType == "um":
#             self.ui_elements.img_mixer_combos[1].addItem("Phase")
#             self.ui_elements.img_mixer_combos[1].addItem("Uni Phase")

#         elif mixType == "p" or mixType == "up":
#             self.ui_elements.img_mixer_combos[1].addItem("Magnitude")
#             self.ui_elements.img_mixer_combos[1].addItem("Uni Mag")

#         elif mixType == "r":
#             self.ui_elements.img_mixer_combos[1].addItem("Imaginary")

#         elif mixType == "i":
#             self.ui_elements.img_mixer_combos[1].addItem("Real")

#     def getAbbreviation(self, comp):
#         if comp == "Magnitude":
#             mixType = "m"
#         elif comp == "Phase":
#             mixType = "p"
#         elif comp == "Real":
#             mixType = "r"
#         elif comp == "Imaginary":
#             mixType = "i"
#         elif comp == "Uni Mag":
#             mixType = "um"
#         elif comp == "Uni Phase":
#             mixType = "up"
#         return mixType


#     def getMixers(self, image1, image2, mixType, scale):
#         logger.debug("checking the mixtype and scaling the component chosen")
#         if mixType == "m":
#             mixer = image1.magnitude * scale + image2.magnitude*(1-scale)
#         elif mixType == "um":
#             mixer = np.ones(image1.magnitude.shape)
#         elif mixType == "p":
#             mixer = image1.phase * scale + image2.phase * (1-scale)
#         elif mixType == "up":
#             mixer = np.zeros(image1.phase.shape)
#         elif mixType == "r":
#             mixer = image1.real * scale + image2.real * (1-scale)
#         elif mixType == "i":
#             mixer = image1.imaginary * scale + image2.imaginary * (1-scale)
#         return mixer

#     def multiplyMixers(self, mixer1, mixer2, mixType):

#         logger.debug("combine the two mixers depending on the mixType")
#         if mixType == "m" or mixType == "um":
#             output = np.multiply(mixer1, np.exp(1j*mixer2))
#         elif mixType == "p" or mixType == "up":
#             output = np.multiply(mixer2, np.exp(1j*mixer1))
#         elif mixType == "r":
#             output = mixer1 + 1j*mixer2
#         elif mixType == "i":
#             output = mixer2 + 1j*mixer1
#         return output

#     def showOutput(self,index):

#         logger.debug("Showing output image ")
#         if self.images[0] != None and self.images[1] != None:
#             mixType1 = self.getAbbreviation(self.ui_elements.selectedComponents[0])
#             mixType2 = self.getAbbreviation(self.ui_elements.selectedComponents[1])
#             # print(mixType1, mixType2)
#             selected1 = self.ui_elements.selectedImages[0]
#             selected2 = self.ui_elements.selectedImages[1]
#             mixer1 = self.getMixers(self.images[selected1], self.images[selected2], mixType1,self.ui_elements.scaleValues[0])
#             mixer2 = self.getMixers(self.images[selected2], self.images[selected1], mixType2,self.ui_elements.scaleValues[1])
#             result = self.multiplyMixers(mixer1, mixer2, mixType1)
#             self.img_data= np.abs(np.fft.ifft2(result))
#             self.show(self.ui_elements.outputs[index],self.img_data)
#             #imagedata = np.abs(np.fft.ifft2(result))
#             #self.show_result(self.ui_elements.outputs[index],imagedata)
            
#     def Select_Output(self):
#         logger.debug("Where to show the output")
        
#         if self.ui_elements.Combo_output[0].currentText() =="Output1" :
#             output_result= 0
#             #print("Output1")
#         elif self.ui_elements.Combo_output[0].currentText() =="Output2" :
#             output_result =1 
#             #print("Output2")
#         return output_result



