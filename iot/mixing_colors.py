#mixing_colors.py

from tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

pwmRed = GPIO.PWM(18, 500)
pwmRed.start(100)

pwmGreen = GPIO.PWM(23, 500)
pwmGreen.start(100)

pwmBlue = GPIO.PWM(24, 500)
pwmBlue.start(100)

class App:

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()

		Label(frame, text='Red').grid(row=0, column=0)
		Label(frame, text='Green').grid(row=1, column=0)
		Label(frame, text='Blue').grid(row=2, column=0)

		ScaleRed = Scale(frame, from_=0, to=100, orient=HORIZONTAL, command=self.updateRed)
		ScaleRed.grid(row=0, column=1)
		ScaleGreen = Scale(frame, from_=0, to=100, orient=HORIZONTAL, command=self.updateGreen)
		ScaleGreen.grid(row=1, column=1)
		ScaleBlue = Scale(frame, from_=0, to=100, orient=HORIZONTAL, command=self.updateBlue)
		ScaleBlue.grid(row=2, column=1)

	def updateRed(self, duty):
		pwmRed.ChangeDutyCycle(float(duty))

	def updateGreen(self, duty):
	        pwmGreen.ChangeDutyCycle(float(duty))

	def updateBlue(self, duty):
        	pwmBlue.ChangeDutyCycle(float(duty))

root = Tk()
root.wm_title('RGB LED Control')
app = App(root)
root.geometry("200x150+0+0")

try:
	root.mainloop()
finally:
	print("Cleaning up")
	GPIO.cleanup()





