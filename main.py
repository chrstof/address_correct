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


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        # Input
        self.line1 = QtWidgets.QLineEdit(self)
        self.line1.setPlaceholderText('ERRONEOUS ADDRESS')
        self.line1.move(5, 5)
        self.line1.setAlignment(Qt.AlignRight)
        self.line1.resize(400, 25)

        # Output
        self.line = QtWidgets.QLineEdit(self)
        self.line.setPlaceholderText('CORRECTED ADDRESS')
        self.line.move(5, 35)
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        self.line.resize(400, 25)

        # CORRECT button
        korregieren = QtWidgets.QPushButton("CORRECT", self)
        korregieren.move(305, 65)
        korregieren.resize(100, 30)
        korregieren.clicked.connect(self.Operator)

        # QUIT button
        quit = QtWidgets.QPushButton("QUIT", self)
        quit.clicked.connect(QCoreApplication.instance().quit)
        quit.move(200, 65)
        quit.resize(100, 30)

        # Window setting
        self.setGeometry(300, 300, 410, 120)
        self.setWindowTitle("ADDRESS CORRECTION")
        self.setFixedSize(410, 100)
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()

    def Operator(self):
        self.line.setText(self.ad_complete(self.line1.text()))

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
        url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + adresse + "&language=de"
        r = urllib.request.urlopen(url)

        # Parse and read json file
        data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))

        # extract formated address [additional informations e.g. geo coordinates ]
        formatierte_adresse = data['results'][0]['formatted_address']
        return formatierte_adresse


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()