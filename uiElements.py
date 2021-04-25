from PyQt5 import  QtWidgets

import logging
logger = logging.getLogger()


class Ui():
    def __init__(self,win) :
        logger.debug('UI Elements')
        self.plots = [ win.original_1, win.original_2, win.components_p1, win.components_p2,win.output1, win.output2]
        self.sliders = [win.slider1,win.slider2]
        self.sliders_txts=[win.slider1_text, win.slider2_text]
        self.img1 = [win.original_1 , win.components_p1]
        self.img2 = [win.original_2 , win.components_p2]
        self.img_plots=[self.img1,self.img2]
        self.outputs=[win.output1, win.output2]
        self.init_plots()
        self.config_sliders()

    
    def init_plots(self):
        for plot in self.plots:
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

    

    
        
        

