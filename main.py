import math
import pyautogui
from time import sleep

mitte_x = 960
mitte_y = 520
radius = 520 # größtmöglicher Radius
maus_positions = []

sleep(5)

pyautogui.mouseDown(button='left')

for winkel_grad in range(0, 360, 6): # in 6er schritten von 0 zu 360 durchgehen. 6, weil kleiner ist "too slow"
    # Umwandlung von Grad in Bogenmaß
    winkel_bogenmass = math.radians(winkel_grad)

    x = mitte_x + radius * math.cos(winkel_bogenmass)  # Punkte berechnen
    y = mitte_y + radius * math.sin(winkel_bogenmass)
    maus_positions.append((x, y))  # zu Liste hinzufügen

for position in maus_positions: # Liste durchgehen
    pyautogui.moveTo(position, duration=0) # Punkte abfahren

pyautogui.mouseUp(button='left')
