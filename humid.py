from sense_hat import SenseHat
import digit, time

sense = SenseHat()
sense.clear()
sense.set_rotation(180)

while True:
    hum = int(round(sense.get_humidity(),0))
    sense.set_pixels(digit.makedigit(hum))
    # Check every minute
    time.sleep(60)
