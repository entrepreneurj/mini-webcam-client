#!/usr/bin/env python


import requests
import time
import PIL
from PIL import Image

CAMERA_IP = "192.168.1.40"
r = requests.get("http://"+CAMERA_IP, stream = True)
print r.headers

jpeg_old = None
for i in range(50):
    response = next(r.iter_lines(1))
    if "Content-Length" in response:
        c_length = int(response.split()[1])
        # skip blank line
        next(r.iter_lines(1))
        jpeg = next(r.iter_content(c_length))
        Image.open(BytesIO(jpeg)
        # Needs proper image dectection - this obviously doesn't work
        #if jpeg != jpeg_old:
        #    print "movemtn"
        jpeg_file_name = "{0}.jpeg".format(int(time.time()))
        with open(jpeg_file_name, 'w') as f:
            f.write(jpeg)
        #else: 
        #    print "same"
        #jpeg_old = jpeg
