#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd2in13_V3
import time
from PIL import Image,ImageDraw,ImageFont

try:
    epd = epd2in13_V3.EPD()
    epd.init()
    epd.Clear(0xFF)

    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
    draw = ImageDraw.Draw(image)
    
    draw.rectangle([(0,0),(50,50)],outline = 0)
    draw.rectangle([(55,0),(100,50)],fill = 0)
    
    epd.sleep()
        
except IOError as e:
    print(e)
    
except KeyboardInterrupt:
    epd2in13_V3.epdconfig.module_exit(cleanup=True)
    exit()
