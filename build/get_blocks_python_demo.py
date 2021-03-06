from __future__ import print_function
from ctypes import *
from pixy import *
import numpy as np
import math, pixy, time, serial

print("Pixy2 Camera Python Get Blocks Demo")
print("---------------------------------------")

# Initialize Pixy2 Camera connection
pixy.init ()
pixy.change_prog ("color_connected_components");

# Create class that stores Pixy2 output data
class Blocks (Structure):
  _fields_ = [ ("m_signature", c_uint), #Signature/Color-Code number
    ("m_x", c_uint),        #X location
    ("m_y", c_uint),        #Y Location
    ("m_width", c_uint),    #Width of block data
    ("m_height", c_uint),   #Height of block data
    ("m_angle", c_uint),    #Angle of color code in degrees
    ("m_index", c_uint),    #Tracking index of block data
    ("m_age", c_uint) ]     #Number of frames given block has tracked

blocks = BlockArray(100)  # Create 'blocks' array based on Pixy2 data
initialAngle = 90   #Initial Angle of arm (90 degrees)
arc = 0   #initialize arc #

# Create serial connection between Raspberry Pi & Arduino 
ser = serial.Serial('/dev/ttyACM2', 115200, timeout=1)
ser.flush()

# Count of the # of blocks captured
count = pixy.ccc_get_blocks (100, blocks)

#run loop continuously
a = 1
while a:
      
  # Print out each object that was detected
  for i in range(0, count):
    if blocks[i].m_signature == 1:
      print("Red Cup Detected!")
    elif blocks[i].m_signature == 5:
      print("Blue Die Detected!")

    # Print signature #, and x,y coordinates
    print("SIG = %3d X = %3d Y = %3d" % (blocks[i].m_signature, blocks[i].m_x, blocks[i].m_y))
     
    # Establish x,y coordinate data that will be manipulated in 
    # order to determine location for arm to know where to move
    x1 = blocks[i].m_x
    y1 = blocks[i].m_y
    sig = blocks[i].m_signature

    # If on the Left side of the arm
    if x1 < 157.5:
      dx = (157.5 - x1)
      dy = 207 - y1
      objectAngle = math.atan2(dy, dx) * (180/math.pi)
      moveAngle = objectAngle - initialAngle
      xtest = 157.5 - x1
      ytest = 207-y1

      # Determine which arc object is on
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
    
    # If on the Right side of the arm 
    elif x1 > 157.5:
      dx = x1 - 157.5
      dy = 207 - y1
      objectAngle = (180 - (math.atan2(dy, dx) * (180/math.pi)))
      moveAngle = objectAngle - initialAngle
      xtest = x1 - 157.5
      ytest = 207 - y1

      # Determine which arc object is on
      radius = math.sqrt(np.square(xtest) + np.square(ytest))
      if radius > 55 and radius < 85:
        arc = 1
        print("\nArc: %i" % arc)
      elif radius > 95 and radius < 125:
        arc = 2
        print("\nArc: %i" % arc)
      elif radius > 135 and radius < 155:
        arc = 3
        print("\nArc: %i" % arc)

    # If directly at 90 degrees (middle, in front of arm)
    else:
      objectAngle = 90
      moveAngle = 0

      # Determine which arc object is on
      radius = 207 - y1
      if radius > 55 and radius < 85:
        arc = 1
        print("\nArc: %i" % arc)
      elif radius > 95 and radius < 125:
        arc = 2
        print("\nArc: %i" % arc)
      elif radius > 135 and radius < 155:
        arc = 3
        print("\nArc: %i" % arc)

    # Print object angle and move angle for arm
    print("Object Angle = %f" % objectAngle)
    print("Move Angle = %f" % moveAngle)
          
    # Create array of data that will be sent 'serially' to Arduino
    sendlist = [str(sig), str(int(objectAngle)), str(arc), str(count)]
    send = ', '.join(sendlist)
    time.sleep(1)
    #if (ser.inWaiting):
    ser.write(send.encode('utf-8'))
    print("Send:", send)
    time.sleep(2)
    receive = ser.readline().decode('utf-8', 'replace').rstrip()
    print("Receive: ", receive)
    print("---------------------------------------")
    
    time.sleep(1)
  
  a = 0




  

      
  
        