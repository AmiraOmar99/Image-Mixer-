from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize , QCoreApplication , QMetaObject
import logging

logger = logging.getLogger()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        logger.debug("UI_MainWindow")
        MainWindow.resize(1665, 880)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1718, 983))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        # self.frame.setGeometry(QtCore.QRect(9, 9, 1640, 861))
        self.frame.setMinimumSize(QtCore.QSize(1700, 900))

        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setFrameStyle(QtWidgets.QFrame.Panel | QtWidgets.QFrame.Raised)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")



        self.frame_11 = QtWidgets.QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setMinimumSize(QtCore.QSize(820, 430))
        # self.frame_11.setGeometry(QtCore.QRect(1, 1, 811, 431))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setFrameStyle(QtWidgets.QFrame.Panel | QtWidgets.QFrame.Raised)

    
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame_11)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(9, 59, 801, 371))
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.original_1 = PlotWidget(self.horizontalLayoutWidget_3)
        self.original_1.setObjectName(u"original_1")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.original_1.sizePolicy().hasHeightForWidth())
        self.original_1.setSizePolicy(sizePolicy)
        self.original_1.setMinimumSize(QtCore.QSize(380, 355))

        self.horizontalLayout_1.addWidget(self.original_1)
# 
        self.horizontalSpacer_1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_1.addItem(self.horizontalSpacer_1)

        self.components_p1 = PlotWidget(self.horizontalLayoutWidget_3)
        self.components_p1.setObjectName(u"components_p1")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.components_p1.sizePolicy().hasHeightForWidth())
        self.components_p1.setSizePolicy(sizePolicy)
        self.components_p1.setMinimumSize(QtCore.QSize(380, 355))

        self.horizontalLayout_1.addWidget(self.components_p1)

        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.frame_11)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 10, 801, 51))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_Image2_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_Image2_2.setObjectName(u"label_Image2_2")
        font = QFont()
        font.setFamily(u"MS UI Gothic")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_Image2_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_Image2_2)

        self.horizontalSpacer_2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btn_open1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.btn_open1.setObjectName(u"btn_open1")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_open1.sizePolicy().hasHeightForWidth())
        self.btn_open1.setSizePolicy(sizePolicy)
        self.btn_open1.setMinimumSize(QtCore.QSize(80, 0))
        font1 = QFont()
        font1.setFamily(u"Rockwell")
        font1.setPointSize(10)
        self.btn_open1.setFont(font1)

        self.horizontalLayout_2.addWidget(self.btn_open1)

        self.comboBox_components1 = QtWidgets.QComboBox(self.horizontalLayoutWidget_6)
        self.comboBox_components1.addItem("")
        self.comboBox_components1.addItem("")
        self.comboBox_components1.addItem("")
        self.comboBox_components1.addItem("")
        self.comboBox_components1.setObjectName(u"comboBox_components1")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_components1.sizePolicy().hasHeightForWidth())
        self.comboBox_components1.setSizePolicy(sizePolicy)
        self.comboBox_components1.setMinimumSize(QtCore.QSize(246, 28))
        self.comboBox_components1.setFont(font1)

        self.horizontalLayout_2.addWidget(self.comboBox_components1)

        self.horizontalSpacer_3 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.gridLayout.addWidget(self.frame_11, 0, 0, 1, 1)

        self.frame_21 = QtWidgets.QFrame(self.frame)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        # self.frame_21.setMinimumSize(QtCore.QSize(820, 430))
        # self.frame_21.setGeometry(QtCore.QRect(820, 1, 820, 431))
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setFrameStyle(QtWidgets.QFrame.Panel | QtWidgets.QFrame.Raised)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.frame_21)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 801, 51))
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        # self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setContentsMargins(10, 2, 2, 2)
        self.label_Mixer = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_Mixer.setObjectName(u"label_Mixer")
        self.label_Mixer.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_Mixer)

        self.horizontalSpacer_10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)

        self.comboBox_outputs = QtWidgets.QComboBox(self.horizontalLayoutWidget_5)
        self.comboBox_outputs.addItem("")
        self.comboBox_outputs.addItem("")
        self.comboBox_outputs.setObjectName(u"comboBox_outputs")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_outputs.sizePolicy().hasHeightForWidth())
        self.comboBox_outputs.setSizePolicy(sizePolicy)
        self.comboBox_outputs.setMinimumSize(QtCore.QSize(270, 28))
        self.comboBox_outputs.setFont(font1)

        self.horizontalLayout_7.addWidget(self.comboBox_outputs)

        self.horizontalSpacer_11 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_11)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_21)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 130, 801, 41))
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamily(u"Rockwell")
        font2.setPointSize(15)
        self.label.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label)

        self.horizontalSpacer_7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.Img_compo1 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.Img_compo1.addItem("")
        self.Img_compo1.addItem("")
        self.Img_compo1.setObjectName(u"Img_compo1")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Img_compo1.sizePolicy().hasHeightForWidth())
        self.Img_compo1.setSizePolicy(sizePolicy)
        self.Img_compo1.setMinimumSize(QtCore.QSize(125, 0))
        self.Img_compo1.setFont(font1)

        self.horizontalLayout_5.addWidget(self.Img_compo1)

        self.horizontalSpacer_8 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.slider1 = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.slider1.setObjectName(u"slider1")
        self.slider1.setOrientation(QtCore.Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.slider1)

        self.slider1_text = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.slider1_text.setObjectName(u"slider1_text")

        self.horizontalLayout_5.addWidget(self.slider1_text)

        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.frame_21)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(10, 170, 801, 51))
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_12 = QtWidgets.QSpacerItem(190, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)

        self.Mixer_components1 = QtWidgets.QComboBox(self.horizontalLayoutWidget_8)
        self.Mixer_components1.addItem("")
        self.Mixer_components1.addItem("")
        self.Mixer_components1.addItem("")
        self.Mixer_components1.addItem("")
        self.Mixer_components1.addItem("")
        self.Mixer_components1.addItem("")
        self.Mixer_components1.setObjectName(u"Mixer_components1")
        sizePolicy1 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Mixer_components1.sizePolicy().hasHeightForWidth())
        self.Mixer_components1.setSizePolicy(sizePolicy1)
        self.Mixer_components1.setMinimumSize(QSize(252, 28))
        self.Mixer_components1.setFont(font1)
        self.Mixer_components1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Mixer_components1.setAutoFillBackground(False)

        self.horizontalLayout_8.addWidget(self.Mixer_components1)

        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.frame_21)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(10, 290, 801, 41))
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.horizontalLayout_9.addWidget(self.label_2)

        self.horizontalSpacer_14 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_14)

        self.Img_compo2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_9)
        self.Img_compo2.addItem("")
        self.Img_compo2.addItem("")
        self.Img_compo2.setObjectName(u"Img_compo2")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Img_compo2.sizePolicy().hasHeightForWidth())
        self.Img_compo2.setSizePolicy(sizePolicy)
        self.Img_compo2.setMinimumSize(QSize(125, 0))
        self.Img_compo2.setFont(font1)

        self.horizontalLayout_9.addWidget(self.Img_compo2)

        self.horizontalSpacer_13 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)

        self.slider2 = QtWidgets.QSlider(self.horizontalLayoutWidget_9)
        self.slider2.setObjectName(u"slider2")
        self.slider2.setOrientation(QtCore.Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.slider2)

        self.slider2_text = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.slider2_text.setObjectName(u"slider2_text")

        self.horizontalLayout_9.addWidget(self.slider2_text)

        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.frame_21)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        # self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(0, 330, 801, 51))
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(10, 330, 801, 51))
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QtWidgets.QSpacerItem(190, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.Mixer_components2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_10)
        self.Mixer_components2.addItem("")
        self.Mixer_components2.addItem("")
        # self.Mixer_components2.addItem("")
        # self.Mixer_components2.addItem("")
        # self.Mixer_components2.addItem("")
        # self.Mixer_components2.addItem("")
        self.Mixer_components2.setObjectName(u"Mixer_components2")
        sizePolicy1 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Mixer_components2.sizePolicy().hasHeightForWidth())
        self.Mixer_components2.setSizePolicy(sizePolicy1)
        self.Mixer_components2.setMinimumSize(QSize(252, 28))
        self.Mixer_components2.setFont(font1)
        self.Mixer_components2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Mixer_components2.setAutoFillBackground(False)

        self.horizontalLayout_6.addWidget(self.Mixer_components2)

        self.gridLayout.addWidget(self.frame_21, 0, 1, 1, 1)

        self.frame_12 = QtWidgets.QFrame(self.frame)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setMinimumSize(QtCore.QSize(820, 430))
        # self.frame_12.setGeometry(QtCore.QRect(1, 439, 811, 441))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setFrameStyle(QtWidgets.QFrame.Panel | QtWidgets.QFrame.Raised)

        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame_12)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 60, 801, 371))
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.original_2 = PlotWidget(self.horizontalLayoutWidget_4)
        self.original_2.setObjectName(u"original_2")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.original_2.sizePolicy().hasHeightForWidth())
        self.original_2.setSizePolicy(sizePolicy)
        self.original_2.setMinimumSize(QSize(380, 355))

        self.horizontalLayout_4.addWidget(self.original_2)

        self.horizontalSpacer_6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.components_p2 = PlotWidget(self.horizontalLayoutWidget_4)
        self.components_p2.setObjectName(u"components_p2")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.components_p2.sizePolicy().hasHeightForWidth())
        self.components_p2.setSizePolicy(sizePolicy)
        self.components_p2.setMinimumSize(QSize(380, 355))

        self.horizontalLayout_4.addWidget(self.components_p2)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_12)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 801, 51))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_Image2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_Image2.setObjectName(u"label_Image2")
        self.label_Image2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_Image2)

        self.horizontalSpacer_4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.btn_open2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_open2.setObjectName(u"btn_open2")
        self.btn_open2.setMinimumSize(QSize(103, 0))
        font3 = QFont()
        font3.setFamily(u"Rockwell")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.btn_open2.setFont(font3)

        self.horizontalLayout_3.addWidget(self.btn_open2)

        self.comboBox_components2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_components2.addItem("")
        self.comboBox_components2.addItem("")
        self.comboBox_components2.addItem("")
        self.comboBox_components2.addItem("")
        self.comboBox_components2.setObjectName(u"comboBox_components2")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_components2.sizePolicy().hasHeightForWidth())
        self.comboBox_components2.setSizePolicy(sizePolicy)
        self.comboBox_components2.setMinimumSize(QSize(246, 28))
        self.comboBox_components2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.comboBox_components2)

        self.horizontalSpacer_5 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.gridLayout.addWidget(self.frame_12, 1, 0, 1, 1)


        self.frame_22 = QtWidgets.QFrame(self.frame)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setMinimumSize(QtCore.QSize(820, 430))
        # self.frame_22.setGeometry(QtCore.QRect(820, 439, 820, 431))
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        # 
        self.frame_22.setFrameStyle(QtWidgets.QFrame.Panel | QtWidgets.QFrame.Raised)

        # self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_22)
        # self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        # self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 391, 51))
        # self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()        
        self.verticalLayout.setObjectName(u"verticalLayout")
        # 
        # self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_out1 = QtWidgets.QLabel(self.frame_22)
        # self.label_out1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_out1.setObjectName(u"label_out1")
        font4 = QFont()
        font4.setFamily(u"MS UI Gothic")
        font4.setPointSize(25)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_out1.setFont(font4)
        self.label_out1.setAutoFillBackground(False)
        self.label_out1.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_out1)
        self.horizontalLayout.addLayout(self.verticalLayout)

# 
        # self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.frame_22)
        # self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        # self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(0, 60, 801, 361))
        # self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        # self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        # self.horizontalLayout_10.setContentsMargins(10, 10, 10, 10)
        # self.output1 = PlotWidget(self.horizontalLayoutWidget_7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_out2 = QtWidgets.QLabel(self.frame_22)
        self.label_out2.setFont(font4)
        self.label_out2.setAutoFillBackground(False)
        self.label_out2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_out2.setObjectName("label_out2")
        self.verticalLayout_3.addWidget(self.label_out2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.output1 = PlotWidget(self.frame_22)

        self.output1.setObjectName(u"output1")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output1.sizePolicy().hasHeightForWidth())
        self.output1.setSizePolicy(sizePolicy)
        self.output1.setMinimumSize(QSize(380, 355))

        self.horizontalLayout_10.addWidget(self.output1)

        self.horizontalSpacer_15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_15)

        # self.output2 = PlotWidget(self.horizontalLayoutWidget_7)
        self.output2 = PlotWidget(self.frame_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.output2.setObjectName(u"output2")
        sizePolicy.setHeightForWidth(self.output2.sizePolicy().hasHeightForWidth())
        self.output2.setSizePolicy(sizePolicy)
        self.output2.setMinimumSize(QSize(380, 355))

        self.horizontalLayout_10.addWidget(self.output2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.gridLayout.addWidget(self.frame_22, 1, 1, 1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_5.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_6.addWidget(self.scrollArea)

        # self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        # self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        # self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1270, 440, 371, 51))
        # self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        # self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        # self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        # self.label_out2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        # self.label_out2.setObjectName(u"label_out2")
        # self.label_out2.setFont(font4)
        # self.label_out2.setAutoFillBackground(False)
        # self.label_out2.setAlignment(QtCore.Qt.AlignCenter)

        # self.verticalLayout_2.addWidget(self.label_out2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_Image2_2.setText(QCoreApplication.translate("MainWindow", u"Image1", None))
        self.btn_open1.setText(QCoreApplication.translate("MainWindow", u"Open Image 1", None))
        self.comboBox_components1.setItemText(0, QCoreApplication.translate("MainWindow", u"Magnitude", None))
        self.comboBox_components1.setItemText(1, QCoreApplication.translate("MainWindow", u"Phase", None))
        self.comboBox_components1.setItemText(2, QCoreApplication.translate("MainWindow", u"Real", None))
        self.comboBox_components1.setItemText(3, QCoreApplication.translate("MainWindow", u"Imaginary", None))

        self.label_Mixer.setText(QCoreApplication.translate("MainWindow", u"Mixer Output to :", None))
        self.comboBox_outputs.setItemText(0, QCoreApplication.translate("MainWindow", u"Output1", None))
        self.comboBox_outputs.setItemText(1, QCoreApplication.translate("MainWindow", u"Output2", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"Component 1:", None))
        self.Img_compo1.setItemText(0, QCoreApplication.translate("MainWindow", u"Image1", None))
        self.Img_compo1.setItemText(1, QCoreApplication.translate("MainWindow", u"Image2", None))
        
        self.Mixer_components1.setItemText(0, QCoreApplication.translate("MainWindow", u"Magnitude", None))
        self.Mixer_components1.setItemText(1, QCoreApplication.translate("MainWindow", u"Phase", None))
        self.Mixer_components1.setItemText(2, QCoreApplication.translate("MainWindow", u"Real", None))
        self.Mixer_components1.setItemText(3, QCoreApplication.translate("MainWindow", u"Imaginary", None))
        self.Mixer_components1.setItemText(4, QCoreApplication.translate("MainWindow", u"Uni Mag", None))
        self.Mixer_components1.setItemText(5, QCoreApplication.translate("MainWindow", u"Uni Phase", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Component 2:", None))
        self.Img_compo2.setItemText(0, QCoreApplication.translate("MainWindow", u"Image1", None))
        self.Img_compo2.setItemText(1, QCoreApplication.translate("MainWindow", u"Image2", None))

        # self.Mixer_components2.setItemText(0, QCoreApplication.translate("MainWindow", u"Magnitude", None))
        self.Mixer_components2.setItemText(0, QCoreApplication.translate("MainWindow", u"Phase", None))
        # self.Mixer_components2.setItemText(2, QCoreApplication.translate("MainWindow", u"Real", None))
        # self.Mixer_components2.setItemText(3, QCoreApplication.translate("MainWindow", u"Imaginary", None))
        # self.Mixer_components2.setItemText(4, QCoreApplication.translate("MainWindow", u"Uni Mag", None))
        self.Mixer_components2.setItemText(1, QCoreApplication.translate("MainWindow", u"Uni Phase", None))

        self.label_Image2.setText(QCoreApplication.translate("MainWindow", u"Image2", None))
        self.btn_open2.setText(QCoreApplication.translate("MainWindow", u"Open Image 2", None))
        self.comboBox_components2.setItemText(0, QCoreApplication.translate("MainWindow", u"Magnitude", None))
        self.comboBox_components2.setItemText(1, QCoreApplication.translate("MainWindow", u"Phase", None))
        self.comboBox_components2.setItemText(2, QCoreApplication.translate("MainWindow", u"Real", None))
        self.comboBox_components2.setItemText(3, QCoreApplication.translate("MainWindow", u"Imaginary", None))

        self.label_out1.setText(QCoreApplication.translate("MainWindow", u"Output 1", None))
        self.label_out2.setText(QCoreApplication.translate("MainWindow", u"Output 1", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main = Ui_MainWindow()
    main.setupUi(MainWindow)
    MainWindow.showMaximized()
    MainWindow.show()
    sys.exit(app.exec_())