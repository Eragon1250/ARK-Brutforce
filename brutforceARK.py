from pynput.keyboard import Key, Controller
import keyboard as key
import time
import sys
import os

script_ordner = os.path.dirname(os.path.abspath(__file__))
speicherdatei = os.path.join(script_ordner, "letzte_zahl.txt")
#speicherdatei = "c:\Visual Studio Code\ARK\letzte_zahl.txt"
keyboard = Controller()
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if key.is_pressed('*'):
	os.remove("c:\Visual Studio Code\ARK\letzte_zahl.txt")

def speichere_letzte_zahl(zahl):
    with open(speicherdatei, "w") as file:
        file.write(str(zahl))

def lade_letzte_zahl():
    if not os.path.exists(speicherdatei):
        speichere_letzte_zahl(0)
        return 0
    with open(speicherdatei, "r") as file:
        return int(file.read().strip())

bisherigezahl = lade_letzte_zahl()

time.sleep(10)

for i in list:
    for j in list:
        for k in list:
            for l in list:
                zahl = int(f"{i}{j}{k}{l}")
                if zahl > bisherigezahl:
                    keyboard.press(str(i))
                    keyboard.release(str(i))
                    keyboard.press(str(j))
                    keyboard.release(str(j))
                    keyboard.press(str(k))
                    keyboard.release(str(k))
                    keyboard.press(str(l))
                    keyboard.release(str(l))
                    print(i, j, k, l)
                    speichere_letzte_zahl(zahl)
                    if key.is_pressed('*'):
                        print("Programm geschlossen")
                        sys.exit()
                    time.sleep(0.6)
                    keyboard.press('e')
                    time.sleep(0.2)
                    keyboard.release('e')
                    time.sleep(2)
                    time.sleep(0.000001)
                    
print("Programm zuende!")


#Die Bildschirmkoordinaten der Tastenfelder
#(Weicht bei anderen Geräten vieleicht ab)

#The screen coordinates of the keypads 
#(may vary on other devices)					

# 0 = (892, 728)
# 1 = (891, 524)
# 2 = (961, 522)
# 3 = (1027, 523)
# 4 = (885, 592)
# 5 = (960, 596)
# 6 = (1031, 589)
# 7 = (892, 663)
# 8 = (959, 661)
# 9 = (1027, 658)
