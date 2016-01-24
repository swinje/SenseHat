from sense_hat import SenseHat
import digit, time

sense = SenseHat()
sense.clear()
sense.set_rotation(180)

while True:
    temp = int(round(sense.get_temperature(),0))
    # "Calibrate"
    temp -= 10
    print(temp)
    sense.set_pixels(digit.makedigit(temp))
    # Check every minute
    time.sleep(60)
