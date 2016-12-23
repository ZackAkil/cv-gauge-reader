from SimpleCV import *
import time
import numpy as np

frame_spec = [160, 120]
frame_bar = np.array(range(frame_spec[0]))
bar_height = 10
frame_roof = (frame_spec[1]/2) - bar_height
frame_floor = (frame_spec[1]/2) + bar_height

def gauge(frame):
	nums = frame.getNumpy()
	slice = (nums[:,frame_roof:frame_floor,0] > 1)
	return slice

def get_avg_x(view_slice):
	count = view_slice.sum()
	avg = (view_slice.sum(axis=1)*frame_bar).sum()/count
	return avg

def draw_box(img, pos):
    overlay = DrawingLayer((img.width, img.height))
    overlay.centeredRectangle((pos,frame_spec[0]/2),(50,50), color=Color.GREEN, filled=True)
    img.addDrawingLayer(overlay)
    img.applyLayers()

def draw_bar(img):
    overlay = DrawingLayer((img.width, img.height))
    overlay.rectangle((0,frame_floor),(img.width,bar_height), color=Color.RED, width=3)
    img.addDrawingLayer(overlay)
    img.applyLayers()

cam = Camera()

for i in range(150):
	frame = cam.getImage().scale(frame_spec[0], frame_spec[1]).grayscale().binarize(45)
	gauge(frame)
	draw_bar(frame)
	draw_box(frame, get_avg_x(gauge(frame)))
	win = frame.show()
	time.sleep(0.05)

win.quit()
