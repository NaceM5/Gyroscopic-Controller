######################################### CLIENT SIDE CODE/IPHONE CODE ######################################################
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
import socket
from pyobjus import autoclass  # Specific to iOS

# Client using iPhone and kivy

import time
from kivy.uix.textinput import TextInput


# Python 2 Client Code
class Client(App):
    counter = 0
    def build(self):
        # Specific to iOS
        Bridge = autoclass('bridge')
        self.br = Bridge.alloc().init()
        self.br.motionManager.setAccelerometerUpdateInterval_(0.1)
        self.br.startAccelerometer()
        self.br.startGyroscope()

        # ip found using socket.gethostbyname(socket.gethostname()) on the server (your computer)
        g = GridLayout(cols=1)
        b = Button(on_release=self.go)
        self.l = Label()
        self.host = TextInput(text='192.168.0.6')
        g.add_widget(b)
        g.add_widget(self.host)
        g.add_widget(self.l)
        return g

    def go(self, *args):
        HOST = '192.168.0.6'  # The server's hostname or IP address (Not needed),(Random IP address)
        HOST = self.host.text
        PORT = 65436  # The port used by the server
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PORT))

        while True:
            time.sleep(.25)
            self.send_msg()

    def send_msg(self, *args):
        self.counter += 1
        data = self.br.gy_x, self.br.gy_y, self.br.gy_z, self.br.ac_x, self.br.ac_y, self.br.ac_z # sends gyroscope data and accelerometer data in a term that looks like (gyx, gyy, ect)
        
        self.s.sendall(str(data)) # sends sensor data to server as binary. Server side converts binary to UTF-8

    # stops everything when application is closed
    def on_stop(self):
        self.s.close()

Client().run()