from PyQt5.QtWidgets import *
from tablodeneme import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow

import requests
from bs4 import BeautifulSoup

class main(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.tablom = Ui_MainWindow()
        self.tablom.setupUi(self)

        r = requests.get("https://bigpara.hurriyet.com.tr/borsa/canli-borsa/")
        soup = BeautifulSoup(r.content, "html.parser")
        borsa = soup.find("div", attrs={"class": "tBody ui-unsortable"})
        satırlar = borsa.find_all("ul")

        veriler = []

        for satır in satırlar:
            data = {}

            data["son"] = satır.find("li", attrs={"class": "cell048 node-c"}).text
            data["alis"] = satır.find("li", attrs={"class": "cell048 node-f"}).text
            data["satis"] = satır.find("li", attrs={"class": "cell048 node-g"}).text
            data["yuksek"] = satır.find("li", attrs={"class": "cell048 node-h"}).text
            data["dusuk"] = satır.find("li", attrs={"class": "cell048 node-i"}).text
            data["yuzde"] = satır.find("li", attrs={"class": "cell048 node-e"}).text
            data["hacim"] = satır.find("li", attrs={"class": "cell064 node-k"}).text
            data["son_islem"] = satır.find("li", attrs={"class": "cell064 node-s"}).text.replace(" ", "")

            veriler.append(data)

        self.listele(veriler)

    def listele(self, veriler):
        self.tablom.tableWidget.setRowCount(len(veriler))
        satır = 0
        for veri in veriler:
            self.tablom.tableWidget.setItem(int(satır), 0, QTableWidgetItem(veri["son"]))
            self.tablom.tableWidget.setItem(int(satır), 1, QTableWidgetItem(veri["alis"]))
            self.tablom.tableWidget.setItem(int(satır), 2, QTableWidgetItem(veri["satis"]))
            self.tablom.tableWidget.setItem(int(satır), 3, QTableWidgetItem(veri["yuksek"]))
            self.tablom.tableWidget.setItem(int(satır), 4, QTableWidgetItem(veri["dusuk"]))
            self.tablom.tableWidget.setItem(int(satır), 5, QTableWidgetItem(veri["yuzde"]))
            self.tablom.tableWidget.setItem(int(satır), 6, QTableWidgetItem(veri["hacim"]))
            self.tablom.tableWidget.setItem(int(satır), 7, QTableWidgetItem(veri["son_islem"]))

            satır += 1


app = QApplication([])
pencere = main()
pencere.show()
app.exec()