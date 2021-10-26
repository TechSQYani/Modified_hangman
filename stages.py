from sense_hat import SenseHat
import time

sense = SenseHat()

sense.set_rotation(90)
sense.low_light = True

X = [200, 190, 0]  # Red
O = [170, 170, 170]  # White

#Define hangman "pieces"
head = [
O, O, O, X, O, O, O, O,
O, O, X, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

torso = [
O, O, O, X, O, O, O, O,
O, O, X, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]


arm1 = [
O, O, O, X, O, O, O, O,
O, O, X, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, X, X, X, O, O, O, O,
O, X, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

arm2 = [
O, O, O, X, O, O, O, O,
O, O, X, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, X, X, X, X, X, O, O,
O, X, O, X, O, X, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

leg1 = [
O, O, O, X, O, O, O, O,
O, O, X, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, X, X, X, X, X, O, O,
O, X, O, X, O, X, O, O,
O, O, O, X, O, O, O, O,
O, O, X, O, O, O, O, O,
O, O, X, O, O, O, O, O
]

leg2 = [
O, O, O, X, O, O, O, O,
O, O, X, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, X, X, X, X, X, O, O,
O, X, O, X, O, X, O, O,
O, O, O, X, O, O, O, O,
O, O, X, O, X, O, O, O,
O, O, X, O, X, O, O, O
]

#Display each hangman state, with a two second delay between each.
sense.set_pixels(head)
time.sleep(1)

sense.set_pixels(torso)
time.sleep(1)

sense.set_pixels(arm1)
time.sleep(1)

sense.set_pixels(arm2)
time.sleep(1)

sense.set_pixels(leg1)
time.sleep(1)

sense.set_pixels(leg2)
time.sleep(1)

sense.show_message(" ")

quit()
