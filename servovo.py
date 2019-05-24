from gpiozero import Servo
from time import sleep
s = Servo(14)
while True:
    s.min()
    sleep(0.5)
    print("frame_width: %s | min_pulse_width: %s | pulse_width: %s | max_pulse_width: %s | value: %s" % (s.frame_width,s.min_pulse_width,s.pulse_width,s.max_pulse_width,s.value))
    s.mid()
    sleep(0.75)#This ratio should be kept!
    print("frame_width: %s | min_pulse_width: %s | pulse_width: %s | max_pulse_width: %s | value: %s" % (s.frame_width,s.min_pulse_width,s.pulse_width,s.max_pulse_width,s.value))
    s.value = None
