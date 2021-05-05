from PyQt5 import  QtWidgets
import logging
import numpy as np
import pyqtgraph as pg
from Image import Image
logger = logging.getLogger()


class Ui():
    def __init__(self,win) :
        logger.debug('UI Elements')
        self.image_test=Image()
        self.images = {0: None, 1:None} #store image path and object

        self.originals = [ win.original_1, win.original_2]
        self.components = [ win.components_p1, win.components_p2]
        self.outputs = [ win.output1, win.output2]
        self.plots=[self.originals,self.components,self.outputs]
        self.sliders = [win.slider1 , win.slider2]
        self.sliders_txts=[win.slider1_text , win.slider2_text]
        
        self.img_combos=[win.comboBox_components1 , win.comboBox_components2]
        self.img_mixer_combos=[win.Mixer_components1   , win.Mixer_components2 ]
        self.img_slider_combos=[win.Img_compo1  , win.Img_compo2 ]
        self.combo_output=[win.comboBox_outputs]
        self.mixing_items=[self.img_mixer_combos,self.img_slider_combos,self.combo_output,self.sliders,self.img_combos] #items to be enabled after uploading 2 images
        self.elements=[self.img_combos,self.img_mixer_combos,self.img_slider_combos,self.combo_output,self.sliders]

        self.config_sliders()

        for plot in self.plots:
            self.init_plots(plot)
        
        for element in self.elements:
            self.disable_elem(element)


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

    def disable_elem(self,element_list):
        for element in element_list:
            element.setDisabled(True)

    def enable_elem(self,element_list):
        for element in element_list:
            element.setEnabled(True)



    







    

    
        
        

