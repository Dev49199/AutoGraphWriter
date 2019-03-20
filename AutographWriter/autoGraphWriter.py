import numpy as np 
import cv2

name = 'App'

class App:
	'''This is app'''
	def __init__(self):
		'''This is the constructor
		which is defing the
		-> Canvas size
		->radius of the circle
		->initial color
		->mouse event status (pressed or not)'''
		self.canvas = np.ones([500,500,3])*255
		self.radius = 3
		self.color =(0,255,0)
		self.pressed = False

	def callback(self,event,x,y,flags,params):
		'''This is the callback function which
		is assosciated with the canvas for mouse event
		->It gets three parameters callback(event,(x,y),flags,params)
		-.All three obtained automatically'''
		if event == cv2.EVENT_LBUTTONDOWN:
			self.pressed = True
			cv2.circle(self.canvas,(x,y),self.radius,self.color,-1)
		elif event == cv2.EVENT_MOUSEMOVE and self.pressed:
			cv2.circle(self.canvas,(x,y),self.radius,self.color,-1)
		elif event == cv2.EVENT_LBUTTONUP:
			self.pressed = False


	def generate(self):
		'''This is the generate funtion
		This function generate the whole canvas and control all the activities are being
		performed on it'''
		cv2.namedWindow("CANVAS")
		cv2.setMouseCallback("CANVAS",self.callback)
		while True:
			cv2.imshow("CANVAS",self.canvas)

			ch = cv2.waitKey(1)

			if ch & 0xFF == ord('q'):
				break
			elif ch & 0xFF == ord('g'):
				self.color =(0,255,0)
			elif ch & 0xFF == ord('b'):
				self.color=(255,0,0)

		cv2.destroyAllWindows()




if __name__ == '__main__':
	app = App()
	app.generate()