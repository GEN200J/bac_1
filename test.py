# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bac1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

#Most labels and buttons are created with Pyqt5 designer
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 861)
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, -20, 811, 121))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.male_image = QtWidgets.QLabel(self.centralwidget)
        self.male_image.setGeometry(QtCore.QRect(60, 80, 111, 121))
        self.male_image.setText("")
        self.male_image.setPixmap(QtGui.QPixmap("male.png"))
        self.male_image.setScaledContents(True)
        self.male_image.setObjectName("male_image")
        self.female_image = QtWidgets.QLabel(self.centralwidget)
        self.female_image.setGeometry(QtCore.QRect(270, 80, 81, 121))
        self.female_image.setText("")
        self.female_image.setPixmap(QtGui.QPixmap("female.png"))
        self.female_image.setScaledContents(True)
        self.female_image.setObjectName("female_image")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 280, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 239, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 360, 67, 71))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("beer.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 440, 91, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 360, 61, 71))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("wine.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(190, 440, 67, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(300, 360, 61, 71))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("liquor.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(300, 440, 67, 17))
        self.label_9.setObjectName("label_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 480, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 480, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 480, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(70, 560, 291, 81))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(80, 604, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(220, 600, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 610, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(290, 610, 67, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(90, 570, 181, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 670, 231, 41))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(80, 210, 92, 23))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(280, 210, 92, 23))
        self.checkBox_2.setObjectName("checkBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Blood Alchohol Content calculator"))
        self.lineEdit.setText(_translate("MainWindow", "Enter weight "))
        self.label_2.setText(_translate("MainWindow", "BODY WEIGHT IN POUNDS"))
        self.label_5.setText(_translate("MainWindow", "Beer 12oz"))
        self.label_7.setText(_translate("MainWindow", "Wine 5oz"))
        self.label_9.setText(_translate("MainWindow", "Liquor 1.5oz"))
        self.lineEdit_2.setText(_translate("MainWindow", "   0"))
        self.lineEdit_3.setText(_translate("MainWindow", "   0"))
        self.lineEdit_4.setText(_translate("MainWindow", "   0"))
        self.lineEdit_6.setText(_translate("MainWindow", "   0"))
        self.lineEdit_7.setText(_translate("MainWindow", "   0"))
        self.label_3.setText(_translate("MainWindow", "Hours"))
        self.label_10.setText(_translate("MainWindow", "Minutes"))
        self.label_11.setText(_translate("MainWindow", "Time since first drink"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.checkBox.setText(_translate("MainWindow", "Male"))
        self.checkBox_2.setText(_translate("MainWindow", "Female"))
        self.pushButton.clicked.connect(self.onCheckBox)
        self.pushButton.clicked.connect(self.Alcohol_Concentration)
        
        

    #CALCULATE WATER VOLUME
    def onCheckBox(self):
        if self.checkBox.isChecked():
            
            self.gender_fraction = 0.58
            self.weight = self.lineEdit.text()
            
            self.Volume_water = float(self.gender_fraction) * float(self.weight) * float(1000)
            
            

        else:
            self.gender_fraction = 0.49
            self.weight = self.lineEdit.text()
            
            self.Volume_water = float(self.gender_fraction) * float(self.weight) * float(1000)
            

        



    def Alcohol_Concentration(self):
        #CONCENTRATION OF ALCHOHOL IN BLOOD IN 12OZ BEER, 5Oz WINE AND 1.5OZ LIQUOR
        
        self.beer12oz = self.lineEdit_2.text()
        beer = self.beer12oz
        self.alchol_water = float(beer) * float(0.28*80.6) * 0.5 / float(self.weight) * float(self.gender_fraction)
        

        wine = self.lineEdit_3.text()
        self.alchol_water2 = float(wine) * float(0.1168015*80.6) * 0.12/ float(self.weight) * float(self.gender_fraction)
        

        liquor = self.lineEdit_4.text()
        self.alchol_water3 = float(liquor) * float(0.03504045*80.6) * 0.40/ float(self.weight) * float(self.gender_fraction)
        

        self.hours = self.lineEdit_6.text()


        self.finalConcentration = float(self.alchol_water + self.alchol_water2 + self.alchol_water3) - 0.017 * float(self.hours)
        print(round(self.finalConcentration, 3))


        if self.finalConcentration == 0:
            print("You're sober and in control!")

        elif self.finalConcentration == 0.01:

            print("You may feel relaxed with some mood changes.")

        elif self.finalConcentration >= 0.02 and self.finalConcentration <= 0.04:

            print("You might be experiencing a minor reduction in muscle control and coordination, with some speech, memory, and attention impairment. Your emotions and behaviors may be exaggerated, and you might start to feel drowsy.")

        elif self.finalConcentration >= 0.05 and self.finalConcentration <= 0.09:

            print("Speech, memory, attention, and coordination impairments are probably more noticeable at this point, and you may have difficulty concentrating. It is extremely dangerous for you to operate a vehicle at this point, even if you are still under the legal limit.")

        elif self.finalConcentration >= 0.1 and self.finalConcentration <= 0.20:

            print("You may be feeling nauseous at this point, possibly even vomiting. Your reflexes can be slow, and you're likely staggering and slurring your words. You're probably going to experience impaired sexual functioning and your mental capacities may be clearly reduced.")
        elif self.finalConcentration >= 0.21 and self.finalConcentration <= 0.29:

            print("At this point, may have almost a complete loss of motor control, and there's a good chance you're vomiting or passing out. You're likely having serious memory impairments, and you should seek professional medical care. You should not operate a vehicle under any circumstances.")
        
        elif self.finalConcentration >= 0.3:

            print("You're probably not reading this because there's a good chance that you're unconscious. This BAC indicates alcohol poisoning, and there is a very serious risk of long-term damage or death. If you or someone you're with are at this BAC level, you should seek immediate medical assistance.")
               



 







        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
