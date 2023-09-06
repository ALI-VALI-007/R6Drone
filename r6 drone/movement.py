#Importing stuff, Pin is pins for the raspberry, UART and PWM is fequencey stuff for bluetooth
from machine import pin,UART,PWM
import time



#Uart channel and Baud rate
uart=UART(0,9600)

#left Motor variables
In1=Pin(6,Pin.OUT) 
In2=Pin(7,Pin.OUT)  
EN_A=PWM(Pin(8))

#Right Motor variables
In3=Pin(4,Pin.OUT)  
In4=Pin(3,Pin.OUT)  
EN_B=PWM(Pin(2))

#In1 and 3 are forward, In2 and 4 are backward, EN is power/speed of motor
#Sets the speed to high.
EN_A.high()
EN_B.high()

#Sets feq for the pins
EN_A.freq(1500)
EN_B.freq(1500)

#Sets duty cycle for max speed
EN_A.duty_u16(65025)
EN_B.duty_u16(65025)


#functions for movement
def forward():
    In1.high()
    In3.high()
    In2.low()
    In4.low()

def backward():
    In1.low()
    In3.low()
    In2.high()
    In4.high()

def turnleft():
    In1.high()
    In3.low()
    In2.low()
    In4.high()

def turnright():
    In1.low()
    In3.high()
    In2.high()
    In4.low()

def stop():
    In1.low()
    In3.low()
    In2.low()
    In4.low()


# all this is for the bluetooth, honestly it just says sees if data is being sent.
# Then it makes it into a string if the string matches the function it does it
while True:
    if uart.any():
        raw=uart.read()
        command=str(raw)
        if ('forward' == command):
            forward()
        elif ('backward' == command):
            backward()
        elif ('turnleft' == command):
            turnleft()
        elif ('turnright' == command):
            turnright()
        else:
            stop()
