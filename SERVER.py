######################################### Server side code/Computer ######################################################

def listen_once():
    
    import socket
    import pyautogui as mouse

    screen_width, screen_height = mouse.size()

    # Calculate the coordinates of the center of the screen
    center_x = screen_width / 2
    center_y = screen_height / 2

    # Move the mouse to the center of the screen
    mouse.moveTo(center_x, center_y)

    # Get host from Wireless LAN adapter wi-fi ipv4.
    HOST = socket.gethostbyname(socket.gethostname())  # Standard loopback interface address (localhost)
    PORT = 65436  # Port to listen on (non-privileged ports are > 1023)
    print("Listening on " + str(HOST) + ":" + str(PORT))

    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        
        with conn:
            print('Connected by client with ip address: ', addr)
            while True:
                data = conn.recv(1024)
                if data.decode() != "":
                    data = data.decode('utf-8')
                    print(data)
                    gy_x, gy_y, gy_z, ac_x, ac_y, ac_z = data
                    gy_x = float(gy_x)
                    gy_y = float(gy_y)
                    gy_z = float(gy_z)
                    ac_x = float(ac_x)
                    ac_y = float(ac_y)
                    ac_z = float(ac_z)
                    Sensor_x = ac_x + (-1 * gy_z)
                    Sensor_y = ac_z + gy_x
                    if gy_x != 0 or gy_y != 0 or gy_z != 0 or ac_x != 0 or ac_y != 0 or ac_z != 0:
                        mouse.moveRel(Sensor_x, Sensor_y) # Moves the mouse on the screen relative to the mouses current position, based off the sensor data

if __name__ == "__main__":
    listen_once()