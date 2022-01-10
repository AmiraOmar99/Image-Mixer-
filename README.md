# Task Description

- A software that has the ability to open and show two images. For each image, the software has two displays (one fixed display for the image, while the second display can show several components based on a drop-menu selection of: 
1) FT Magnitude.
2) FT Phase.
3) FT Real component.
4) FT Imaginary component.

**Note** the software imposes that the two images have the same size. i.e. when opening the second image, the sw checks that it has the same size of the one previously opened. Otherwise, gives an error message.

- A mixing panel where an output will be formed based on the mix of two components. Each one of these components should be determined from:<br>
    1. which image (via a drop-menu). Available images are image 1, and image 2.
    2. Which component of the image FT (via a drop-menu). Available components are: Magnitude, Phase, Real, Imaginary, uniform magnitude (i.e. all magnitude values are set to 1), uniform phase (i.e. all phase values are set to 0).
    3. The mixing ratio (via a slider ranging from 0 to 100%).


- Based on the mixing panel, an output image will be generated and displayed for the user. There are two available displays, each for one output. The mixing panel sends the output to either display-Output 1 or 2. The display is determined using a drop-menu in the mixing panel. 

- The output is generated on the fly whenever the user changes a mixing option.


**Run main.py to run the GUI**
