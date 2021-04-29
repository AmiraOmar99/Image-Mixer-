from PyQt5 import  QtWidgets

import logging
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
        self.img_combos=[win.comboBox_components1 , win.comboBox_components2]

        for plot in self.plots:
            self.init_plots(plot)

        self.disable_combos(self.img_combos)
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
            slider.setSingleStep(5)
            slider.setTickInterval(10)
            self.sliders_txts[i].setText(str(slider.value()))

    def disable_combos(self,combo_list):
        for combobox in combo_list:
            combobox.setDisabled(True)



    

    
        
        

