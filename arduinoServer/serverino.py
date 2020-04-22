# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:56:09 2020

@author: Diogo Alves
"""

from tornado import websocket, web, ioloop
import json
import threading
import numpy
import serial
import asyncio

#device = serial.Serial('COM6',9600,timeout=5)

def tostring(data):
    dtype=type(data).__name__
    if dtype=='ndarray':
        if numpy.shape(data)!=(): data=data.tolist()
        else: data='"'+data.tostring()+'"'
    elif dtype=='dict' or dtype=='tuple':
        try: data=json.dumps(data)
        except: pass
    elif dtype=='NoneType':
        data=''
    elif dtype=='str' or dtype=='unicode':
        data=json.dumps(data)
    
    return str(data)

cl = []

class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in cl:
            cl.append(self)
        print("CONNECTED")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        if self in cl:
            cl.remove(self)
        print("DISCONNECTED")
        
def Arduino_handler():
    
    asyncio.set_event_loop(asyncio.new_event_loop())
    button = []
    try:
        device = serial.Serial('COM6',9600,timeout=5)
        dataButton = []
        cicle = 1
        start = numpy.array(cicle)
        start = numpy.mean(start)
        while start == 1:
            buttonLine = device.readline().strip()
            buttonLine = buttonLine.decode('utf-8','ignore').split()
            value1 =  [int(i) for i in buttonLine]
            dataButton += [value1]
            button = numpy.array(dataButton) 
            
            start = numpy.mean(button)
            print(start)
            
            
    finally:
        device.close()
        print("CLOSE")
        
app = web.Application([(r'/', SocketHandler)])        

if __name__ == '__main__':                   
    print('LISTENING')
    port=9000
    app.listen(port)
    
    ard = threading.Thread(name='arduino', target=Arduino_handler)
    ard.start()
    
    print('CONNECTING')
    mainLoop = ioloop.IOLoop.instance().start()