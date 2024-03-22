import math
import pyautogui
from time import sleep

# y=r×sin(θ) # Formel zur x & y berechnung
# x=r×cos(θ)

mitte_x = 960 # Mitte also der weiße Kreis in der Mitte
mitte_y = 520
radius = 520 # größtmöglicher Radius, da iwi neal.fun größere Kreise als besser bewertet
maus_positions = []

sleep(5) # bissl Zeit geben um Fenster zu öffnen

pyautogui.mouseDown(button='left') # Linksklick drücken

for winkel_grad in range(0, 360, 6): # in 6er schritten von 0 zu 360 durchgehen, 6 weil kleiner ist too slow
    # Umwandlung von Grad in Bogenmaß
    winkel_bogenmass = math.radians(winkel_grad) # von grad in bogenmaß, weil python will bogenmaß

    x = mitte_x + radius * math.cos(winkel_bogenmass)  # Formel anwenden
    y = mitte_y + radius * math.sin(winkel_bogenmass)
    maus_positions.append((x, y))  # zu Liste hinzufügen

for position in maus_positions: # Liste durchgehen
    pyautogui.moveTo(position, duration=0) # dann eben immer direkt ohne duration durchgehen

pyautogui.mouseUp(button='left')  # Maus nicht mehr drücken

# Bestes Ergebnis: 99,9% (das beste was geht denke ich)