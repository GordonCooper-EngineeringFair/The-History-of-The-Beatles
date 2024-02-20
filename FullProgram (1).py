# Define the pins, leds, motor, speaker, and buttons.

from machine import Pin, PWM
from wavePlayer import wavePlayer
from myPWM import myPWM
from time import sleep

player=wavePlayer
led1=Pin(1,Pin.OUT)
led2=Pin(3,Pin.OUT)
led3=Pin(4,Pin.OUT)
led4=Pin(5,Pin.OUT)
led5=Pin(6,Pin.OUT)
led6=Pin(7,Pin.OUT)
led7=Pin(8,Pin.OUT)
led8=Pin(9,Pin.OUT)
led9=Pin(10,Pin.OUT)
led10=Pin(11,Pin.OUT)
led11=Pin(12,Pin.OUT)
led12=Pin(14,Pin.OUT)
led13=Pin(15,Pin.OUT)
motor1a=Pin(16,Pin.OUT)
motor1b=Pin(17,Pin.OUT)
speaker=Pin(20,Pin.OUT)
but1StateOld=1
but1StateNow=0
button1=Pin(18,Pin.IN, Pin.PULL_UP)
but2StateOld=1
but2StateNow=0
button2=Pin(19,Pin.IN, Pin.PULL_UP)
pausePlay=False
intro= False
sec1=False
sec2=False
sec3=False
sec4=False
sec5=False
sec6=False
sec7=False
sec8=False
sec9=False
sec10=False
sec11=False
sec12=False
sec13=False
outro=False
motor1=False
motor2=False
motor3=False
motor4=False


# Set the program to start when you press the button
while True:
    but1StateNow=button1.value()
    if pausePlay=False and but1StateNow=1:
        pausePlay=True
    if pausePlay=True and but1StateNow=1
        pausePlay=False
# Play the intro with no lights for 10 seconds
# Play the lights and audio.
while True:
    if pausePlay==True and intro==False:
        player.play('BeatlesAudio1')
        sleep(7.9)
        intro=True
while True:
    if pausePlay==True and intro==True and sec1==False:
        led1.value(1)
        print(led1)
        player.play('BeatlesAudio2')
        sleep(8.0)
        led1.value(0)
        print(led1)
        sec1=True
        
while True:
    if pausePlay==True and sec1==True and sec2==False:
        led2.value(1)
        print(led2)
        player.play('BeatlesAudio3')
        sleep(16.0)
        led2.value(0)
        print(led2)
        sec2=True

while True:
    if pausePlay==True and sec2==True and sec3==False:
        led3.value(1)
        print(led3)
        player.play('BeatlesAudio4')
        sleep(18.2)
        led3.value(0)
        print(led3)
        sec3=True
    
# Spin the motor 90 degrees, then repeat the last section.
while True:
    if pausePlay==True and sec3==True and motor1==False:
        motor1a.high
        motor1b.low
        sleep(3)
        motor1a.low
        motor1b.low
        motor1=True

while True:
    if pausePlay==True and motor1==True and sec4==False:
        led4.value(1)
        print(led4)
        player.play('BeatlesAudio5')
        sleep(20.7)
        led4.value(0)
        print(led4)
        sec4=True
    
while True:
    if pausePlay==True and sec4==True and sec5==False:    
        led5.value(1)
        print(led5)
        player.play('BeatlesAudio6')
        sleep(18.7)
        led5.value(0)
        print(led5)
        sec5=True
    
while True:
    if pausePlay==True and sec5==True and sec6==False:    
        led6.value(1)
        print(led6)
        player.play('BeatlesAudio7')
        sleep(19.7)
        led6.value(0)
        print(led6)
        sec6=True
    
# Spin the motor 90 degrees, then repeat the last section.
while True:
    if pausePlay==True and sec6==True and motor2==False:
        motor1a.high
        motor1b.low
        sleep(3)
        motor1a.low
        motor1b.low
        motor2=True
        
while True:
    if pausePlay==True and motor2==True and sec7==False:
        led7.value(1)
        print(led7)
        player.play('BeatlesAudio8')
        sleep(17.5)
        led7.value(0)
        print(led7)
        sec7=True

while True:
    if pausePlay==True and sec7==True and sec8==False:
        led8.value(1)
        print(led8)
        player.play('BeatlesAudio9')
        sleep(32.1)
        led8.value(0)
        print(led8)
        sec8=True

while True:
    if pausePlay==True and sec8==True and sec9==False:
        led9.value(1)
        print(led9)
        player.play('BeatlesAudio10')
        sleep(22.1)
        led9.value(0)
        print(led9)
        sec9=True

# Spin the motor 90 degrees, then repeat the last section.
while True:
    if pausePlay==True and sec9==True and motor3==False:
        motor1a.high
        motor1b.low
        sleep(3)
        motor1a.low
        motor1b.low
        motor3=True
    
while True:
    if pausePlay==True and motor3==True and sec10==False:    
        led10.value(1)
        print(led10)
        player.play('BeatlesAudio11')
        sleep(20.4)
        led10.value(0)
        print(led10)
        sec10=True
    
while True:
    if pausePlay==True and sec10==True and sec11==False:    
        led11.value(1)
        print(led11)
        player.play('BeatlesAudio12')
        sleep(19.9)
        led11.value(0)
        print(led11)
        sec11=True
    
while True:
    if pausePlay==True and sec11==True and sec12==False:
        led12.value(1)
        print(led12)
        player.play('BeatlesAudio13')
        sleep(11)
        led12.value(0)
        print(led12)
        sec12=True

while True:
    if pausePlay==True and sec12==True and sec13==False:
        led13.value(1)
        print(led13)
        player.play('BeatlesAudio14')
        sleep(14)
        led13.value(0)
        print(led13)
        sec13=True
        
        
while True:
    if pausePlay==True and sec13==True and outro==False:
        player.play('BeatlesAudio15')
        outro=True
    
# Spin the motor one more time, then the program ends.
while True:
    if pausePlay==True and outro==True and motor4==False:
        motor1a.high
        motor1b.low
        sleep(3)
        motor1a.low
        motor1b.low
        motor4=True
    but1StateOld=but1StateNow
    
if button2.value():
    quit()