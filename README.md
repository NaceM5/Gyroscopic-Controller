The function of this program is to send the gyroscope and accelerometer data on board the iphone to a Wi-Fi connected computer to control the mouse pointer based of the movement of the iphone
This program uses Kivy for the IOS front end and pyautogui to control the mouse on the server/computer

CLIENT.py:
- This is the code that will run on the iphone and sends the gyroscope and accelerometer data to the server
- Displays a simple GUI with a textbox to enter the local IP of the target computer.
- In order to run this code on iphone, you need to know how to use the kivy framework
  - https://youtu.be/6gLGyrlgqCU?si=clxWUm902HCDYRts this is a good video that includes how to run Kivy code

SERVER.py
- This is the code that will run on your computer
- This code should be running before you attempt to connect with the ios application
