# Neal.fun - Perfect Circle Hack
Dieses programm generiert automatisch einen 99,9% Kreis bei dem Spiel [Perfect Circle auf neal.fun](https://neal.fun/perfect-circle/). 

## Technische Umsetzung
Die Zeilen `x = mitte_x + radius * math.cos(winkel_bogenmass)` und `y = mitte_y + radius * math.sin(winkel_bogenmass)` berechnen den nächste Punkt auf dem Kreis und diese werden anschließend zu einer Liste hinzugefügt.
Diese Liste wird iteriert und die Maus fährt die Positionen ab. 

## Hinweis
Das Programm ist darauf ausgelegt, den Browser im Vollbildmodus zu verwenden, um den größtmöglichen Radius zu ermöglichen. 
[Neal.fun](Neal.fun) scheint einem größeren Radius einer höhere Genaugkeit zuzuschreiben, was einer bessere Prozentzahl bedeutet.

## Achtung! 
Während das Programm läuft, kann man selber nicht mehr die Maus bewegen.
Dementsprechend wartet man ein paar Sekunden, dann ist die Maus auch wieder frei bewegbar.
Auch kann die Geschwindigkeit, in der der Kreis gezeichnet wird je nach Rechenleistung variieren, auch bis dahin, dass der Kreis für die Webiste zu langsam gezeichnet wird. 
In diesem Fall sollte man die Schritte in der for-Schleife (hier: 6) erhöhen.

***
<img src="https://i.ibb.co/rM220vy/perfect-circle.png" alt="99,9% perfect circle" width="384" height="216">
