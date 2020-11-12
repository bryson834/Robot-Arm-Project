from __future__ import print_function
import pixy 
from ctypes import *
from pixy import *
import math
import numpy as np
import time
import serial

# Pixy2 Python SWIG get blocks example #

print("Pixy2 Python SWIG Example -- Get Blocks")
print("---------------------------------------")

pixy.init ()
pixy.change_prog ("color_connected_components");

class Blocks (Structure):
  _fields_ = [ ("m_signature", c_uint),
    ("m_x", c_uint),
    ("m_y", c_uint),
    ("m_width", c_uint),
    ("m_height", c_uint),
    ("m_angle", c_uint),
    ("m_index", c_uint),
    ("m_age", c_uint) ]

blocks = BlockArray(100)
initialAngle = 90
arc = 0

ser = serial.Serial('/dev/ttyACM1', 115200, timeout=1)
ser.flush()

count = pixy.ccc_get_blocks (100, blocks)
a = 1
while a:
  for i in range(0, count):
    print("SIG = %3d X = %3d Y = %3d" % (blocks[i].m_signature, blocks[i].m_x, blocks[i].m_y))
     
    x1 = blocks[i].m_x
    y1 = blocks[i].m_y

    if x1 < 157.5:
      dx = (157.5 - x1)
      dy = 207 - y1
      objectAngle = math.atan2(dy, dx) * (180/math.pi)
      moveAngle = objectAngle - initialAngle
      xtest = 157.5 - x1
      ytest = 207-y1

      radius = math.sqrt(np.square(xtest) + np.square(ytest))
      if radius > 55 and radius < 85:
        arc = 1
        print("Arc: %i\n" % arc)
      elif radius > 95 and radius < 125:
        arc = 2
        print("Arc: %i\n" % arc)
      elif radius > 135 and radius < 155:
        arc = 3
        print("Arc: %i\n" % arc)
      
    elif x1 > 157.5:
      dx = x1 - 157.5
      dy = 207 - y1
      objectAngle = (180 - (math.atan2(dy, dx) * (180/math.pi)))
      moveAngle = objectAngle - initialAngle
      xtest = x1 - 157.5
      ytest = 207 - y1

      radius = math.sqrt(np.square(xtest) + np.square(ytest))
      if radius > 55 and radius < 85:
        arc = 1
        print("Arc: %i\n" % arc)
      elif radius > 95 and radius < 125:
        arc = 2
        print("Arc: %i\n" % arc)
      elif radius > 135 and radius < 155:
        arc = 3
        print("Arc: %i\n" % arc)

    else:
      objectAngle = 90
      moveAngle = 0
    
      radius = 207 - y1
      if radius > 55 and radius < 85:
        arc = 1
        print("Arc: %i" % arc)
      elif radius > 95 and radius < 125:
        arc = 2
        print("Arc: %i" % arc)
      elif radius > 135 and radius < 155:
        arc = 3
        print("Arc: %i" % arc)

    print("Object Angle = %f" % objectAngle)
    print("Move Angle = %f" % moveAngle)
          

    sendlist = [str(int(moveAngle)), str(arc)]
    send = ', '.join(sendlist)
    print("Send:", send)
    ser.write(send.encode('utf-8'))
    receive = ser.readline().decode('utf-8', 'replace').rstrip()
    print("Receive: ", receive)
    print("---------------------------------------")
    
    time.sleep(2)




  

      
  
        