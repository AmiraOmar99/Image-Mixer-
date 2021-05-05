from Image import Output
import logging
import numpy as np

logger = logging.getLogger()

class Mixer():
    def __init__(self,win):
        self.win=win
        self.outputs=[Output(),Output()]
        self.selected_images = [0,0]
        self.selected_components = ["Magnitude", "Phase"]
        self.scale_values = [0.5, 0.5]
        self.recieved_data = [None, None]
        self.selected_output = 0
        self.ouput_images = [None, None]

        self.mixers=[None , None]
        self.mix_types=[None , None]
        

        for item in self.win.ui_elements.mixing_items:
            self.win.ui_elements.enable_elem(item)

        for i in range(2):
            self.set_connections(i)
        
        self.show_output()

    def set_connections(self, index):
        self.win.ui_elements.img_slider_combos[index].activated[str].connect(lambda: self.select_image(index))
        self.win.ui_elements.img_mixer_combos[index].activated[str].connect(lambda: self.select_component(index))
        self.win.ui_elements.sliders[index].valueChanged.connect(lambda: self.slider_moved(index))
        #self.win.ui_elements.sliders[index].sliderReleased.connect(lambda: self.slider_released(index))
        self.win.ui_elements.combo_output[0].activated[str].connect(lambda: self.show_output())


    def select_image(self, index):
        logger.debug("selecting image from which we choose the component")
        self.selected_images[index] = self.win.ui_elements.img_slider_combos[index].currentIndex()
        logger.info("Image Combobox {} has changed to {}".format(index+1, self.selected_images[index]+1))
        self.show_output()


    def slider_moved(self, index):
        logger.info("Slider {}, Value {}".format(index+1, self.win.ui_elements.sliders[index].value()))
        self.scale_values[index] = self.win.ui_elements.sliders[index].value()/100
        self.win.ui_elements.sliders_txts[index].setText(str(self.win.ui_elements.sliders[index].value())+" %")

        #to log file
        scales=[self.scale_values[0] , self.scale_values[1]]
        comps=[self.selected_components[0] , self.selected_components[1]]
        indexes=[self.selected_images[0],self.selected_images[1]]
        logger.info("Mixing {} of {} of Image {} with {} of {} of Image {}".format(scales[0], comps[0], indexes[0]+1, scales[1], comps[1], indexes[1]+1)) 

        self.show_output()


    # def slider_released(self, index):
    #     logger.info("Slider {} moved to {}%".format(index+1, self.win.ui_elements.sliders[index].value()))
    #     scales=[self.scale_values[0] , self.scale_values[1]]
    #     comps=[self.selected_components[0] , self.selected_components[1]]
    #     indexes=[self.selected_images[0],self.selected_images[1]]
    #     logger.info("Mixing {} of {} of Image {} with {} of {} of Image {}".format(scales[0], comps[0], indexes[0]+1, scales[1], comps[1], indexes[1]+1)) 


    def select_component(self, index):
        #selected_components = self.win.ui_elements.img_mixer_combos[index].currentText() 
        self.selected_components [index] = self.win.ui_elements.img_mixer_combos[index].currentText() 
        if index == 0:
            self.mix_types[0] = self.get_abbreviation(self.selected_components[index])
            self.set_second_compo(self.mix_types[0])
            self.selected_components[1] = self.win.ui_elements.img_mixer_combos[1].currentText()
            self.win.ui_elements.sliders[1].setEnabled(True)
        if self.selected_components [index]== "Uni Mag" or self.selected_components [index] == "Uni Phase":
            self.win.ui_elements.sliders[index].setEnabled(False)
        else:
            self.win.ui_elements.sliders[index].setEnabled(True)
        logger.debug("Component ComboBox {} of image {} changed to Image {}".format(index+1, self.selected_images[index]+1, self.selected_components [index]))
        self.show_output()


    def set_second_compo(self, mixType):
        logger.debug("Changing items of combobox 2 according to component chosen from combobox 1")
        self.clear_compo(1)
        if mixType == "m" or mixType == "um":
            self.win.ui_elements.img_mixer_combos[1].addItem("Phase")
            self.win.ui_elements.img_mixer_combos[1].addItem("Uni Phase")

        elif mixType == "p" or mixType == "up":
            self.win.ui_elements.img_mixer_combos[1].addItem("Magnitude")
            self.win.ui_elements.img_mixer_combos[1].addItem("Uni Mag")

        elif mixType == "r":
            self.win.ui_elements.img_mixer_combos[1].addItem("Imaginary")

        elif mixType == "i":
            self.win.ui_elements.img_mixer_combos[1].addItem("Real")


    def clear_compo(self,index):
        logger.debug("clears the items of the combobox")
        for i in range(self.win.ui_elements.img_mixer_combos[index].count()):
            self.win.ui_elements.img_mixer_combos[index].removeItem(0)


    def get_abbreviation(self, comp):
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
        print(mixType)
        return mixType


    def get_mixers(self, image1, image2, mixType, scale):
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


    def multiply_mixers(self, mixer1, mixer2, mix_type):
        logger.debug("combine the two mixers depending on the mixType")
        if mix_type == "m" or mix_type == "um":
            output = np.multiply(mixer1, np.exp(1j*mixer2))
        elif mix_type == "p" or mix_type == "up":
            output = np.multiply(mixer2, np.exp(1j*mixer1))
        elif mix_type == "r":
            output = mixer1 + 1j*mixer2
        elif mix_type == "i":
            output = mixer2 + 1j*mixer1
        return output


    def show_output(self):
        logger.debug("Showing output image ")
        index = self.select_output()
    
        for i in range(2):
            self.mix_types[i]=self.get_abbreviation(self.selected_components[i])
            self.mixers[i]=self.get_mixers(self.win.images[self.selected_images[i]], self.win.images[self.selected_images[1-i]], self.mix_types[i],self.scale_values[i])

        result = self.multiply_mixers(self.mixers[0], self.mixers[1], self.mix_types[0])
        self.outputs[index].img_data= np.abs(np.fft.ifft2(result))
        self.outputs[index].show(self.win.ui_elements.outputs[index],self.outputs[index].img_data)

            
    def select_output(self):
        logger.debug("Where to show the output")
        output_result = self.win.ui_elements.combo_output[0].currentIndex()
        return output_result