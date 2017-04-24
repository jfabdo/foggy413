from gpiozero import Motor
from math import radians,sin,cos,pi

sidemotor = Motor(17,18)
fbmotor = Motor(1,2)

"""Omni: input the speed as a percentage of full speed, aka 98, 75... Input the angle in degrees"""
def omnigo(speed,angle):
   aspd = speed/100.
   rangle  = radians(angle%360)
   
   if if angle == 270 or angle == 90:
      sidemotor.stop()
   elif angle > 270 or angle < 90:
      sidemotor.forward(aspd*cos(rangle))
   else:
      sidemotor.backward(aspd*cos(pi-rangle))
   
   if angle == 180 or angle == 360:
      fbmotor.stop()
   elif angle < 180:
      fbmotor.forward(aspd*sin(rangle))
   else:
      fbmotor.backward(aspd*sin(pi-rangle))
   
