# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 539))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(-411, 0, 838, 448))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_11 = QtWidgets.QFrame(self.scrollAreaWidgetContents_6)
        self.frame_11.setMinimumSize(QtCore.QSize(820, 430))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame_11)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(9, 59, 801, 371))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.original_1 = PlotWidget(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.original_1.sizePolicy().hasHeightForWidth())
        self.original_1.setSizePolicy(sizePolicy)
        self.original_1.setMinimumSize(QtCore.QSize(380, 355))
        self.original_1.setObjectName("original_1")
        self.horizontalLayout_1.addWidget(self.original_1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_1.addItem(spacerItem)
        self.components_p1 = PlotWidget(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.components_p1.sizePolicy().hasHeightForWidth())
        self.components_p1.setSizePolicy(sizePolicy)
        self.components_p1.setMinimumSize(QtCore.QSize(380, 355))
        self.components_p1.setObjectName("components_p1")
        self.horizontalLayout_1.addWidget(self.components_p1)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.frame_11)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 10, 801, 51))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_Image2_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_Image2_2.setFont(font)
        self.label_Image2_2.setObjectName("label_Image2_2")
        self.horizontalLayout_6.addWidget(self.label_Image2_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.btn_open1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_open1.sizePolicy().hasHeightForWidth())
        self.btn_open1.setSizePolicy(sizePolicy)
        self.btn_open1.setMinimumSize(QtCore.QSize(80, 0))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.btn_open1.setFont(font)
        self.btn_open1.setObjectName("btn_open1")
        self.horizontalLayout_6.addWidget(self.btn_open1)
        self.comboBox_components1 = QtWidgets.QComboBox(self.horizontalLayoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_components1.sizePolicy().hasHeightForWidth())
        self.comboBox_components1.setSizePolicy(sizePolicy)
        self.comboBox_components1.setMinimumSize(QtCore.QSize(246, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.comboBox_components1.setFont(font)
        self.comboBox_components1.setObjectName("comboBox_components1")
        self.comboBox_components1.addItem("")
        self.comboBox_components1.addItem("")
        self.comboBox_components1.addItem("")
        self.comboBox_components1.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_components1)
        spacerItem2 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_6.addWidget(self.frame_11)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_6)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(-411, -211, 838, 448))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_12 = QtWidgets.QFrame(self.scrollAreaWidgetContents_7)
        self.frame_12.setMinimumSize(QtCore.QSize(820, 430))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.frame_12)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 60, 801, 371))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.original_3 = PlotWidget(self.horizontalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.original_3.sizePolicy().hasHeightForWidth())
        self.original_3.setSizePolicy(sizePolicy)
        self.original_3.setMinimumSize(QtCore.QSize(380, 355))
        self.original_3.setObjectName("original_3")
        self.horizontalLayout_9.addWidget(self.original_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.components_p2_2 = PlotWidget(self.horizontalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.components_p2_2.sizePolicy().hasHeightForWidth())
        self.components_p2_2.setSizePolicy(sizePolicy)
        self.components_p2_2.setMinimumSize(QtCore.QSize(380, 355))
        self.components_p2_2.setObjectName("components_p2_2")
        self.horizontalLayout_9.addWidget(self.components_p2_2)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.frame_12)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 10, 801, 51))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_Image2_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_Image2_3.setFont(font)
        self.label_Image2_3.setObjectName("label_Image2_3")
        self.horizontalLayout_10.addWidget(self.label_Image2_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.btn_open2_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.btn_open2_2.setMinimumSize(QtCore.QSize(103, 0))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_open2_2.setFont(font)
        self.btn_open2_2.setObjectName("btn_open2_2")
        self.horizontalLayout_10.addWidget(self.btn_open2_2)
        self.comboBox_components2_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_components2_2.sizePolicy().hasHeightForWidth())
        self.comboBox_components2_2.setSizePolicy(sizePolicy)
        self.comboBox_components2_2.setMinimumSize(QtCore.QSize(246, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.comboBox_components2_2.setFont(font)
        self.comboBox_components2_2.setObjectName("comboBox_components2_2")
        self.comboBox_components2_2.addItem("")
        self.comboBox_components2_2.addItem("")
        self.comboBox_components2_2.addItem("")
        self.comboBox_components2_2.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_components2_2)
        spacerItem5 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.verticalLayout_5.addWidget(self.frame_12)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_7)
        self.verticalLayout_3.addWidget(self.scrollArea_3)
        self.horizontalLayout_23.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 838, 448))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_21 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.frame_21.setMinimumSize(QtCore.QSize(820, 430))
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayoutWidget_13 = QtWidgets.QWidget(self.frame_21)
        self.horizontalLayoutWidget_13.setGeometry(QtCore.QRect(0, 10, 801, 51))
        self.horizontalLayoutWidget_13.setObjectName("horizontalLayoutWidget_13")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_Mixer_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_13)
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_Mixer_2.setFont(font)
        self.label_Mixer_2.setObjectName("label_Mixer_2")
        self.horizontalLayout_17.addWidget(self.label_Mixer_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem6)
        self.comboBox_outputs_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_outputs_2.sizePolicy().hasHeightForWidth())
        self.comboBox_outputs_2.setSizePolicy(sizePolicy)
        self.comboBox_outputs_2.setMinimumSize(QtCore.QSize(270, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.comboBox_outputs_2.setFont(font)
        self.comboBox_outputs_2.setObjectName("comboBox_outputs_2")
        self.comboBox_outputs_2.addItem("")
        self.comboBox_outputs_2.addItem("")
        self.horizontalLayout_17.addWidget(self.comboBox_outputs_2)
        spacerItem7 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem7)
        self.horizontalLayoutWidget_14 = QtWidgets.QWidget(self.frame_21)
        self.horizontalLayoutWidget_14.setGeometry(QtCore.QRect(0, 130, 801, 41))
        self.horizontalLayoutWidget_14.setObjectName("horizontalLayoutWidget_14")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_14)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_14)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_18.addWidget(self.label_3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem8)
        self.Img_compo1_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Img_compo1_2.sizePolicy().hasHeightForWidth())
        self.Img_compo1_2.setSizePolicy(sizePolicy)
        self.Img_compo1_2.setMinimumSize(QtCore.QSize(125, 0))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.Img_compo1_2.setFont(font)
        self.Img_compo1_2.setObjectName("Img_compo1_2")
        self.Img_compo1_2.addItem("")
        self.Img_compo1_2.addItem("")
        self.horizontalLayout_18.addWidget(self.Img_compo1_2)
        spacerItem9 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem9)
        self.slider1_2 = QtWidgets.QSlider(self.horizontalLayoutWidget_14)
        self.slider1_2.setOrientation(QtCore.Qt.Horizontal)
        self.slider1_2.setObjectName("slider1_2")
        self.horizontalLayout_18.addWidget(self.slider1_2)
        self.slider1_text_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_14)
        self.slider1_text_2.setObjectName("slider1_text_2")
        self.horizontalLayout_18.addWidget(self.slider1_text_2)
        self.horizontalLayoutWidget_15 = QtWidgets.QWidget(self.frame_21)
        self.horizontalLayoutWidget_15.setGeometry(QtCore.QRect(0, 170, 801, 51))
        self.horizontalLayoutWidget_15.setObjectName("horizontalLayoutWidget_15")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_15)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem10 = QtWidgets.QSpacerItem(190, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem10)
        self.Mixer_components1_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Mixer_components1_2.sizePolicy().hasHeightForWidth())
        self.Mixer_components1_2.setSizePolicy(sizePolicy)
        self.Mixer_components1_2.setMinimumSize(QtCore.QSize(252, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.Mixer_components1_2.setFont(font)
        self.Mixer_components1_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Mixer_components1_2.setAutoFillBackground(False)
        self.Mixer_components1_2.setObjectName("Mixer_components1_2")
        self.Mixer_components1_2.addItem("")
        self.Mixer_components1_2.addItem("")
        self.Mixer_components1_2.addItem("")
        self.Mixer_components1_2.addItem("")
        self.Mixer_components1_2.addItem("")
        self.Mixer_components1_2.addItem("")
        self.horizontalLayout_19.addWidget(self.Mixer_components1_2)
        self.horizontalLayoutWidget_16 = QtWidgets.QWidget(self.frame_21)
        self.horizontalLayoutWidget_16.setGeometry(QtCore.QRect(0, 290, 801, 41))
        self.horizontalLayoutWidget_16.setObjectName("horizontalLayoutWidget_16")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_16)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_16)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_20.addWidget(self.label_4)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem11)
        self.Img_compo2_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Img_compo2_2.sizePolicy().hasHeightForWidth())
        self.Img_compo2_2.setSizePolicy(sizePolicy)
        self.Img_compo2_2.setMinimumSize(QtCore.QSize(125, 0))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.Img_compo2_2.setFont(font)
        self.Img_compo2_2.setObjectName("Img_compo2_2")
        self.Img_compo2_2.addItem("")
        self.Img_compo2_2.addItem("")
        self.horizontalLayout_20.addWidget(self.Img_compo2_2)
        spacerItem12 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem12)
        self.slider2_2 = QtWidgets.QSlider(self.horizontalLayoutWidget_16)
        self.slider2_2.setOrientation(QtCore.Qt.Horizontal)
        self.slider2_2.setObjectName("slider2_2")
        self.horizontalLayout_20.addWidget(self.slider2_2)
        self.slider2_text_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_16)
        self.slider2_text_2.setObjectName("slider2_text_2")
        self.horizontalLayout_20.addWidget(self.slider2_text_2)
        self.horizontalLayoutWidget_17 = QtWidgets.QWidget(self.frame_21)
        self.horizontalLayoutWidget_17.setGeometry(QtCore.QRect(0, 330, 801, 51))
        self.horizontalLayoutWidget_17.setObjectName("horizontalLayoutWidget_17")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_17)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        spacerItem13 = QtWidgets.QSpacerItem(190, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem13)
        self.Mixer_components2_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Mixer_components2_2.sizePolicy().hasHeightForWidth())
        self.Mixer_components2_2.setSizePolicy(sizePolicy)
        self.Mixer_components2_2.setMinimumSize(QtCore.QSize(252, 28))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.Mixer_components2_2.setFont(font)
        self.Mixer_components2_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Mixer_components2_2.setAutoFillBackground(False)
        self.Mixer_components2_2.setObjectName("Mixer_components2_2")
        self.Mixer_components2_2.addItem("")
        self.Mixer_components2_2.addItem("")
        self.Mixer_components2_2.addItem("")
        self.Mixer_components2_2.addItem("")
        self.Mixer_components2_2.addItem("")
        self.Mixer_components2_2.addItem("")
        self.horizontalLayout_21.addWidget(self.Mixer_components2_2)
        self.verticalLayout_9.addWidget(self.frame_21)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_8)
        self.verticalLayout_4.addWidget(self.scrollArea_4)
        self.scrollArea_5 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 838, 448))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_22 = QtWidgets.QFrame(self.scrollAreaWidgetContents_9)
        self.frame_22.setMinimumSize(QtCore.QSize(820, 430))
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.frame_22)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 391, 51))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_out1_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_out1_2.setFont(font)
        self.label_out1_2.setAutoFillBackground(False)
        self.label_out1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_out1_2.setObjectName("label_out1_2")
        self.verticalLayout_8.addWidget(self.label_out1_2)
        self.horizontalLayoutWidget_18 = QtWidgets.QWidget(self.frame_22)
        self.horizontalLayoutWidget_18.setGeometry(QtCore.QRect(0, 60, 801, 361))
        self.horizontalLayoutWidget_18.setObjectName("horizontalLayoutWidget_18")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_18)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.output1_2 = PlotWidget(self.horizontalLayoutWidget_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output1_2.sizePolicy().hasHeightForWidth())
        self.output1_2.setSizePolicy(sizePolicy)
        self.output1_2.setMinimumSize(QtCore.QSize(380, 355))
        self.output1_2.setObjectName("output1_2")
        self.horizontalLayout_22.addWidget(self.output1_2)
        spacerItem14 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem14)
        self.output2_2 = PlotWidget(self.horizontalLayoutWidget_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output2_2.sizePolicy().hasHeightForWidth())
        self.output2_2.setSizePolicy(sizePolicy)
        self.output2_2.setMinimumSize(QtCore.QSize(380, 355))
        self.output2_2.setObjectName("output2_2")
        self.horizontalLayout_22.addWidget(self.output2_2)
        self.verticalLayout_10.addWidget(self.frame_22)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_9)
        self.verticalLayout_4.addWidget(self.scrollArea_5)
        self.horizontalLayout_23.addLayout(self.verticalLayout_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Image2_2.setText(_translate("MainWindow", "Image1"))
        self.btn_open1.setText(_translate("MainWindow", "Open Image 1"))
        self.comboBox_components1.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.comboBox_components1.setItemText(1, _translate("MainWindow", "Phase"))
        self.comboBox_components1.setItemText(2, _translate("MainWindow", "Real"))
        self.comboBox_components1.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.label_Image2_3.setText(_translate("MainWindow", "Image2"))
        self.btn_open2_2.setText(_translate("MainWindow", "Open Image 2"))
        self.comboBox_components2_2.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.comboBox_components2_2.setItemText(1, _translate("MainWindow", "Phase"))
        self.comboBox_components2_2.setItemText(2, _translate("MainWindow", "Real"))
        self.comboBox_components2_2.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.label_Mixer_2.setText(_translate("MainWindow", "Mixer Output to :"))
        self.comboBox_outputs_2.setItemText(0, _translate("MainWindow", "Output1"))
        self.comboBox_outputs_2.setItemText(1, _translate("MainWindow", "Output2"))
        self.label_3.setText(_translate("MainWindow", "Component 1:"))
        self.Img_compo1_2.setItemText(0, _translate("MainWindow", "Image1"))
        self.Img_compo1_2.setItemText(1, _translate("MainWindow", "Image2"))
        self.slider1_text_2.setText(_translate("MainWindow", "TextLabel"))
        self.Mixer_components1_2.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.Mixer_components1_2.setItemText(1, _translate("MainWindow", "Phase"))
        self.Mixer_components1_2.setItemText(2, _translate("MainWindow", "Real"))
        self.Mixer_components1_2.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.Mixer_components1_2.setItemText(4, _translate("MainWindow", "Uni Mag"))
        self.Mixer_components1_2.setItemText(5, _translate("MainWindow", "Uni Phase"))
        self.label_4.setText(_translate("MainWindow", "Component 2:"))
        self.Img_compo2_2.setItemText(0, _translate("MainWindow", "Image1"))
        self.Img_compo2_2.setItemText(1, _translate("MainWindow", "Image2"))
        self.slider2_text_2.setText(_translate("MainWindow", "TextLabel"))
        self.Mixer_components2_2.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.Mixer_components2_2.setItemText(1, _translate("MainWindow", "Phase"))
        self.Mixer_components2_2.setItemText(2, _translate("MainWindow", "Real"))
        self.Mixer_components2_2.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.Mixer_components2_2.setItemText(4, _translate("MainWindow", "Uni Mag"))
        self.Mixer_components2_2.setItemText(5, _translate("MainWindow", "Uni Phase"))
        self.label_out1_2.setText(_translate("MainWindow", "Output 1"))
from pyqtgraph import PlotWidget
