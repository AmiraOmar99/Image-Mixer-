from PyQt5 import  QtWidgets
import logging
import numpy as np
import pyqtgraph as pg
logger = logging.getLogger()


class Ui():
    def __init__(self,win) :
        logger.debug('UI Elements')
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

        self.selectedImages = [0, 0]
        self.selectedComponents = ["Magnitude", "Phase"]
        self.scaleValues = [0.5, 0.5]
        self.recievedData = [None, None]
        self.selectedOutput = 0
        self.ouputImages = [None, None]

        for plot in self.plots:
            self.init_plots(plot)

        self.disable_elem(self.img_combos)
        self.disable_elem(self.img_mixer_combos)
        self.disable_elem(self.img_slider_combos)
        self.disable_elem(self.Combo_output)
        self.disable_elem(self.sliders)

        self.config_sliders()

        

    
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
        

    


    







    

    
        
        

