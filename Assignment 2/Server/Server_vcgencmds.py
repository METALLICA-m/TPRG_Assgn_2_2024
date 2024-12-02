# Chamath Kulathilaka (100889193)
# TPRG 2131
# November 29, 2024
# This program is strictly my own work. Any material
# beyong course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to original author (s).
# This server runs on Pi, sends Pi's your 4 arguments from the vcgencmds, sent as Json object.
# details of the Pi's vcgencmds - https://www.tomshardware.com/how-to/raspberry-pi-benchmark-vcgencmd
# more vcgens on Pi 4, https://forums.raspberrypi.com/viewtopic.php?t=245733
# more of these at https://www.nicm.dev/vcgencmd/
import socket
import json, time
import os



s = socket.socket()
port = 5000
host = "192.168.2.54" # local host

s.bind((host, port))
s.listen(5)

print('Socket is listening')

v = os.popen('vcgencmd measure_volts ain1').readline() # gets from the os, using vcgencmd - the core-voltage
core = os.popen('vcgencmd measure_temp').readline() # gets from the os, using vcgencmd - the core-temperature
mem = os.popen('vcgencmd get_mem gpu').readline() # gets memory split for GPU
arm = os.popen('vcgencmd get_mem arm').readline() # gets memory split for arm CPU
clock = os.popen('vcgencmd measure_clock arm').readline() # gets arm CPU core speed
# starting json object string
jsonResult = {"volts":v, "temp-core":core, "Memory":mem, "arm-memory":arm, "core-speed":clock}
# converting string to json
jsonResult = json.dumps(jsonResult)


while True:
    c, addr = s.accept()
    print ('Got connection from',addr)
    res = bytes(str(jsonResult), "UTF-8") # needs to be a byte

    c.send(res) # sends data as a byte type
    time.sleep(5)
    c.close()

