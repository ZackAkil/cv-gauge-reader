from SimpleCV import *
import time
import numpy as np


def gauge(frame):
	nums = frame.getNumpy()
	slice = (nums[:,230:250,0] > 1)
	return slice

frame_bar = np.array(range(640))

def get_avg_x(view_slice):
	count = view_slice.sum()
	avg = (view_slice.sum(axis=1)*frame_bar).sum()/count
	return avg

def draw_box(img, pos):
    overlay = DrawingLayer((img.width, img.height))
    overlay.centeredRectangle((pos,240),(50,50), color=Color.GREEN, filled=True)
    img.addDrawingLayer(overlay)
    img.applyLayers()

def draw_bar(img):
    overlay = DrawingLayer((img.width, img.height))
    overlay.rectangle((0,230),(img.width,20), color=Color.RED, width=3)
    img.addDrawingLayer(overlay)
    img.applyLayers()



cam = Camera()

for i in range(80):
	frame = cam.getImage().grayscale().binarize(45)
	gauge(frame)
	draw_bar(frame)
	draw_box(frame, get_avg_x(gauge(frame)))
	win = frame.show()
	time.sleep(0.05)

win.quit()
