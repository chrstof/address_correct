__author__ = 'christof petrick'

# This Program auto completes or auto corrects erroneous addresses using google maps. Thus any erroneous address that is
# corrected by google maps will be corrected by this program.
#


## Use conda to set up your environment
#
# conda create -n addresscorrect python=3.5
#
## installing pyqt5
# conda install -c https://conda.anaconda.org/mmcauliffe pyqt5
# you can run the following code in your environment "addresscorrect" using "python main.py"
#

import sys, json, urllib.request
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt, QCoreApplication

from PyQt5.QtWidgets import QComboBox

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        # Input
        self.input_line = QtWidgets.QLineEdit(self)
        self.input_line.setPlaceholderText('ERRONEOUS ADDRESS')
        self.input_line.move(5, 5)
        self.input_line.setAlignment(Qt.AlignRight)
        self.input_line.resize(400, 25)

        # Output
        self.output_line = QtWidgets.QLineEdit(self)
        self.output_line.setPlaceholderText('CORRECTED ADDRESS')
        self.output_line.move(5, 35)
        self.output_line.setReadOnly(True)
        self.output_line.setAlignment(Qt.AlignRight)
        self.output_line.resize(400, 25)

        self.combo = QComboBox(self)
        self.combo.addItem("en")
        self.combo.addItem("de")
        self.combo.addItem("fr")
        self.combo.addItem("es")
        self.combo.addItem("ru")
        self.combo.move(5, 65)


        # CORRECT button
        correct_button = QtWidgets.QPushButton("CORRECT", self)
        correct_button.move(305, 65)
        correct_button.resize(100, 30)
        correct_button.clicked.connect(self.Operator)

        # QUIT button
        quit_button = QtWidgets.QPushButton("QUIT", self)
        quit_button.clicked.connect(QCoreApplication.instance().quit)
        quit_button.move(200, 65)
        quit_button.resize(100, 30)

        # Window setting
        self.setGeometry(300, 300, 410, 120)
        self.setWindowTitle("ADDRESS CORRECTION")
        self.setFixedSize(410, 100)
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()

    def Operator(self):
        self.output_line.setText(self.ad_complete(self.input_line.text()))

    def ad_format(self, adresse):
        # for all the german users, this function will replace all "Umlaute", i.e. ö,ä,ü and ß
        adresse = adresse.replace(' ', ',')
        adresse = adresse.replace('ü', 'ue')
        adresse = adresse.replace('ö', 'oe')
        adresse = adresse.replace('ä', 'ae')
        adresse = adresse.replace('ß', 'ss')
        return adresse

    def ad_complete(self, adresse):
        adresse = self.ad_format(adresse)

        # Insert addresses into url
        url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + adresse + "&language="+str(self.combo.currentText()) #de"
        r = urllib.request.urlopen(url)

        # Parse and read json file
        data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))

        try:
            # extract formated address [additional informations e.g. geo coordinates ]
            formatierte_adresse = data['results'][0]['formatted_address']
        except:
            formatierte_adresse = 'Error'

        return formatierte_adresse


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
