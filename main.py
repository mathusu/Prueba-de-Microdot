from machine import Pin, I2C
from time import sleep
import BME280
def connect_to(ssid, passwd):

    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(ssid, passwd)
        while not sta_if.isconnected():
            pass
    return sta_if.ifconfig()[0]
        
from microdot import Microdot, send_file


app = Microdot()

@app.route("/")
def index(request):
    
    return send_file("index.html")


@app.route("/assets/<dir>/<file>")
def assets(request, dir, file):
   
    return send_file("/assets/" + dir + "/" + file)

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)

@app.route("/data/update")
def data_update(request):
    bme = BME280.BME280(i2c=i2c)
    press = bme.pressure 
    press = press.replace('hPa', '')
    return { "Pressure" : press }
    
if __name__ == "__main__":
    
    try:
        # Me conecto a internet
        ip = connect_to("Mateo", "contra_prueba")
        # Muestro la direccion de IP
        print("Microdot corriendo en IP/Puerto: " + ip + ":5000")
        # Inicio la aplicacion
        app.run()
    
    except KeyboardInterrupt:
        # Termina el programa con Ctrl + C
        print("Aplicacion terminada")
        
