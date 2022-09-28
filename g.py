# import cv2
#
#         def show_webcam(mirror=False):
#             scale=10
#
#             cam = cv2.VideoCapture(0)
#             while True:
#                 ret_val, image = cam.read()
#                 if mirror:
#                     image = cv2.flip(image, 1)
#
#
#                 #get the webcam size
#                 height, width, channels = image.shape
#
#                 #prepare the crop
#                  centerX,centerY=int(height/2),int(width/2)
#                 radiusX,radiusY= int(scale*height/100),int(scale*width/100)
#
#                 minX,maxX=centerX-radiusX,centerX+radiusX
#                 minY,maxY=centerY-radiusY,centerY+radiusY
#
#                 cropped = image[minX:maxX, minY:maxY]
#                 resized_cropped = cv2.resize(cropped, (width, height))
#
#                 cv2.imshow('my webcam', resized_cropped)
#                 if cv2.waitKey(1) == 27:
#                     break  # esc to quit
#
#                 #add + or - 5 % to zoom
#
#                 if cv2.waitKey(1) == 0:
#                     scale += 5  # +5
#
#                 if cv2.waitKey(1) == 1:
#                     scale = 5  # +5
#
#             cv2.destroyAllWindows()
#
#
#         def main():
#             show_webcam(mirror=True)
#
#
#         if __name__ == '__main__':
#             main()


# !/usr/bin/env python

# WS server that sends messages at random intervals
#
import asyncio
# import datetime
# import random
import websockets
import cv2
import base64

import sys

from io import StringIO

from vidgear.gears import VideoGear
from vidgear.gears import WriteGear
import numpy as np

print("seesfedslesdfesgf")

cam = VideoGear(source=0, stabilize=True).start()
#
# # font
font = cv2.FONT_HERSHEY_SIMPLEX
#
# # org
org = (150, 50)
org2 = (150, 80)
#
# # fontScale
fontScale = 0.8
#
# # Blue color in BGR
color = (255, 0, 0)
#
# # Line thickness of 2 px
thickness = 2
#
#
# # Using cv2.putText() method
#
#
import os
class Server:
    def get_port(self):
        return os.getenv('WS_PORT', '5678')
        #

    def get_host(self):
        return os.getenv('WS_HOST', '192.168.1.12')
        #

    def start(self):
        return websockets.serve(self.handler, self.get_host(), self.get_port())
        #

    async def handler(self, websocket, path):



        while True:

            print("ferslrfr")

            sys.stdout = buffer = StringIO()
            sys.stdout = open('output.txt', 'w')
            zoom_factor = 0
            frame = cam.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            vds = frame.shape[0] // 2
            vhs = frame.shape[1] // 2
    #
            def zoom_center(img, zoom_factor=5.5):
                y_size = img.shape[0]
                x_size = img.shape[1]
    #
    #             # define new boundaries
                x1 = int(0.5 * x_size * (1 - 1 / zoom_factor))
                x2 = int(x_size - 0.5 * x_size * (1 - 1 / zoom_factor))
                y1 = int(0.5 * y_size * (1 - 1 / zoom_factor))
                y2 = int(y_size - 0.5 * y_size * (1 - 1 / zoom_factor))
    #
    #             # first crop image then scale
                img_cropped = img[y1:y2, x1:x2]
                return cv2.resize(img_cropped, None, fx=zoom_factor, fy=zoom_factor)
    #
            gray = zoom_center(gray)
            gray = cv2.putText(gray, 'SCALE: 5.5', org, font, fontScale, color, thickness, cv2.LINE_AA)
            gray = cv2.putText(gray, 'STABILIZATION: ON', org2, font, fontScale, color, thickness, cv2.LINE_AA)
    #
            gray = cv2.line(gray, (0, vds), (vhs - 30, vds), 255, 4)
            gray = cv2.line(gray, (vhs + 30, vds), (gray.shape[1], vds), 255, 4)
            gray = cv2.line(gray, (vhs, 0), (vhs, vds - 30), 255, 4)
            gray = cv2.line(gray, (vhs, gray.shape[0]), (vhs, vds + 30), 255, 4)
    #
            print(gray.shape)
            # gray = cv2.rectangle(gray, (0, 20),(50, 50), (255, 255, 255), 2)
            res, frame = cv2.imencode('.jpg', gray)
            data = base64.b64encode(frame)
            await websocket.send(data)
            print("asdasdaa")
            await asyncio.sleep(0.01)




            # print(message)

        # messagem = await websocket.recv()

        # print('server received :', messagem)

                        # if message ==
            # async for message in websocket:
            #     print('server received :', message)


    #             # if message ==
#
wsxx = Server()
asyncio.get_event_loop().run_until_complete(wsxx.start())
#

# start_server = websockets.serve(Server.time, "127.0.0.1", 5678)
# asyncio.get_event_loop().run_until_complete()


asyncio.get_event_loop().run_forever()

cam.release()
# asyncio.run(hello())