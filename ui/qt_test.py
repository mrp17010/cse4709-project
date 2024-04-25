import sys
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import uic
import paho.mqtt.publish as publish

class CarPilot(QMainWindow):
    def __init__(self):
        super(CarPilot, self).__init__()
        self.setWindowTitle("car pilot")
        uic.loadUi("carpilot.ui", self)
        self.show()
        

#    def move_forward(topic):
#        publish.single(topic, 1, hostname="")

#    def move_backward(topic):
#        publish.single(topic, 2, hostname="")

#    def move_stop(topic):
#        publish.single(topic, 0, hostname="")

def main():
    app = QApplication([])
    window = CarPilot()
    app.exec_()

if __name__ == '__main__':
    main()