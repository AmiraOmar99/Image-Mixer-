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
        self.items={"Magnitude":["Phase","Uni Phase"],"Uni Mag":["Phase","Uni Phase"], "Phase":["Magnitude","Uni Mag"],"Uni Phase":["Magnitude","Uni Mag"], "Real":["Imaginary"],"Imaginary" : ["Real"]}
        self.mixers=[None , None]
        self.mix_types=[None , None]
        
        for item in self.win.ui_elements.mixing_items:
            self.win.ui_elements.enable_elem(item)

        for i in range(2):
            self.set_connections(i)
        
        self.show_output()
    
    def update(self):
        self.show_output()

    def set_connections(self, index):
        self.win.ui_elements.img_slider_combos[index].activated[str].connect(lambda: self.select_image(index))
        self.win.ui_elements.img_mixer_combos[index].activated[str].connect(lambda: self.select_component(index))
        self.win.ui_elements.sliders[index].valueChanged.connect(lambda: self.slider_moved(index))
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



    def select_component(self, index):
        self.selected_components [index] = self.win.ui_elements.img_mixer_combos[index].currentText() 
        if index == 0:
            self.mix_types[0] = self.selected_components[index]
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

        for key in self.items:
            if mixType == key:
                for comp in self.items[key]:
                    self.win.ui_elements.img_mixer_combos[1].addItem(comp)




    def clear_compo(self,index):
        logger.debug("clears the items of the combobox")
        for i in range(self.win.ui_elements.img_mixer_combos[index].count()):
            self.win.ui_elements.img_mixer_combos[index].removeItem(0)




    def get_mixers(self, image1, image2, mixType, scale):
        logger.debug("checking the mixtype and scaling the component chosen")
        self.mixers_out = {"Magnitude":image1.magnitude * scale + image2.magnitude*(1-scale),"Uni Mag":np.ones(image1.magnitude.shape),"Phase":image1.phase * scale + image2.phase * (1-scale),"Uni Phase":np.zeros(image1.phase.shape),"Real":image1.real * scale + image2.real * (1-scale),"Imaginary":image1.imaginary * scale + image2.imaginary * (1-scale)}
        
        for key in self.mixers_out:
            if key == mixType:
                mixer = self.mixers_out[key]
    
        return mixer


    def multiply_mixers(self, mixer1, mixer2, mix_type):
        logger.debug("combine the two mixers depending on the mixType")
        self.mixer_combine = {"Magnitude":np.multiply(mixer1, np.exp(1j*mixer2)),"Uni Mag":np.multiply(mixer1, np.exp(1j*mixer2)),"Phase":np.multiply(mixer2, np.exp(1j*mixer1)),"Uni Phase":np.multiply(mixer2, np.exp(1j*mixer1)),"Real":mixer1 + 1j*mixer2,"Imaginary":mixer2 + 1j*mixer1}

        for key in self.mixer_combine:
            if mix_type == key:
                output = self.mixer_combine[key]

        return output


    
    def show_output(self):
        logger.debug("Showing output image ")
        index = self.select_output()
    
        for i in range(2):
            self.mix_types[i]=self.selected_components[i]
            self.mixers[i]=self.get_mixers(self.win.images[self.selected_images[i]], self.win.images[self.selected_images[1-i]], self.mix_types[i],self.scale_values[i])

        result = self.multiply_mixers(self.mixers[0], self.mixers[1], self.mix_types[0])
        self.outputs[index].img_data= np.abs(np.fft.ifft2(result))
        self.outputs[index].show(self.win.ui_elements.outputs[index],self.outputs[index].img_data)


            
    def select_output(self):
        logger.debug("Where to show the output")
        output_result = self.win.ui_elements.combo_output[0].currentIndex()
        return output_result

        