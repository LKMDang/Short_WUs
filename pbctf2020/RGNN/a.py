from malduck import unhex
from pwn import process
import os

CLUE_ROWS = list(unhex("0104030101040204010202010101010203010101030301010201010403050202010201040505050505050505050505050505050505050505050505050505050505050505050505050505050505050505010303010201010202010103020203010101020102010101030401030201010103010101030101020303010103020105020105050505050505050505050505050505050505050505050505050505050501010101030101020201010602010301010202010301010102030301020101020302010102010101030103030103010105050505050505050505050505050505050505050505050505050505050505050102020101040203010102010301020103020101020103010301010103010201030101020301020103010101020101030202030101010201010103010201050505050505050505050505050505050505010202020202030102010203030101010102030201020301010602010104020101010301010103020505050505050505050505050505050505050505050505050505050505050505050505050505050503010201030202010101030101020102020103020101010202010302020103010104030201020201010103010102020103010104050505050505050505050505050505050505050505050505050505050201030103010201030102010301010103010203020201010301010202010101030101040101030102010101020202050101030101010505050505050505050505050505050505050505050505050505010102010102020201030202030101030201010401030203020201010201010201010301010102020301020305050505050505050505050505050505050505050505050505050505050505050505050501010202030202010301020203010301020103020201010102020101030101010201030102030302010101020201010103010202010103010203050505050505050505050505050505050505050505050201020103020103020103020101020101010201030101020302010201010201010103010101030202010302020101010301020301040505050505050505050505050505050505050505050505050505030202010103020101010304020101020202010103010204010301010302010103010301030102010202010203010505050505050505050505050505050505050505050505050505050505050505050501010201010103030101030302020102020102010302020103020102030302010301020201040301020401010301010102010505050505050505050505050505050505050505050505050505050505050101030102010302030402010301010102010301010502020304010103010102020103020202030101010301010302010505050505050505050505050505050505050505050505050505050505050505010302030302030202020301020101010302020101040306020201010102010202010101030101020505050505050505050505050505050505050505050505050505050505050505050505050505050502010102030303010102010103020102030102010301010102020101030101020301010303010201010103010201020103030505050505050505050505050505050505050505050505050505050505050102020103010101020301040201020101010205020203010201030201010301010102030301020101030201020103020101050505050505050505050505050505050505050505050505050505050505030102020301010302010101020103020103010103020201020201010201020203010103020103010301010103020101020203030101050505050505050505050505050505050505050505050505050502010304010102010101020101010101020201010201010103020201010102010101020301010302010102010101030201010201030102010301010102010201030105050505050505050505050505050204010203010101020403010101020101030104020101040201010103020102020101010201030101010202030101010505050505050505050505050505050505050505050505050505050505050505010102010101030101010301020103010102020201010108030201020204030201020201020101030303010102010505050505050505050505050505050505050505050505050505050505050505050502020302020101010304010203010201010101020202010603010102020101030201010101010203010403010301020105050505050505050505050505050505050505050505050505050505050505050202010102010101020103030201010302010105020201010201010103010101020101010201010202020302020101050301020105050505050505050505050505050505050505050505050505050505030101010101030201010201030101020201030101030201030101010201010103010202030102030301010203030102020201010301050505050505050505050505050505050505050505050505050503020102010101030301020103010101030203010204010103010202010103010302010303010201010102010301020305050505050505050505050505050505050505050505050505050505050505050105020101030203030101020301020301010301010203020201030101010101030101020301020103020103030302010505050505050505050505050505050505050505050505050505050505050505010102010101030202010201020701030202010203010201010102030303020103020103030102010301020105050505050505050505050505050505050505050505050505050505050505050505050502010202010103010201010103010202030201010303030101020201030202020301010202030102030A050505050505050505050505050505050505050505050505050505050505050505050505050502030101030101010302020203010202030101020302010202020302010102010202030102040301030201010201030103020201050505050505050505050505050505050505050505050505050505050201030201010301030102010101010101030202010102040203010203010101020103010201010102010101020101010303030103020101050505050505050505050505050505050505050505050505020103040204030101020202010103010201020101020201010101010303020101010203030202010302020103020505050505050505050505050505050505050505050505050505050505050505050502020101020101010302020201010201030101010202010302030102010102010102020103030101030102030303020402020505050505050505050505050505050505050505050505050505050505050301010102010102010101020201030101040202010102010301010201010201010202010302020101010201030101010203020203010505050505050505050505050505050505050505050505050505010202020102030201020204010102010301020103010103030102010301020103010201010401010201010103030201010103010201010102020101050505050505050505050505050505050505050501020303010102020101030101010101010303020106020101010201010203020201010103010202010201010202010102010102050505050505050505050505050505050505050505050505050505050102030201010301020201010301030101030202010303020101010101010301020103030103010102010101020301010505050505050505050505050505050505050505050505050505050505050505030101010302010201020301020103020201010103010101020201010201030201010203030201010302020103010101020101020301010202020301050505050505050505050505050505050505050501030201010103010205030102010101030301010201030101020204030101010301020101020303020201020201010103020505050505050505050505050505050505050505050505050505050505050301020102010301030102020201030101040201010202010101020601010302020103010303020102010101020203010201050505050505050505050505050505050505050505050505050505050505010103010201010103010201030301010301010402010101030302020301010102010101020101010301020102010102030101020301020101020303050505050505050505050505050505050505050501050301010102030102020103010101030101010202030101010301030202010301010203010205010202010301010102010301020101020505050505050505050505050505050505050505050505050104020103010102020101020201010403010301030301010302020102010302020101060201030103010101050505050505050505050505050505050505050505050505050505050505050505050505010503020201030202010102020103010101030101010201030102030301010202010101010103010201020103010102030101010102030101010302010105050505050505050505050505050505050501040201030102010302020203050301020101010302010103010201030201040301010102010302010105050505050505050505050505050505050505050505050505050505050505050505050505050103010203020201010103020103020201030201030101050301030201010301010102010102020103030102050505050505050505050505050505050505050505050505050505050505050505050505020201040101020103020201020103010102030101010201030201020301010302010304030102030302030405050505050505050505050505050505050505050505050505050505050505050505050503010201010102010102020203010103020103020102030202020307020201010201010103020101030402010301050505050505050505050505050505050505050505050505050505050505050505050101020101020201030501020101030101010201030102020302030102010101030101010301020102010103030101010302030202010301020205050505050505050505050505050505050505050505010102010301020103010201010201020201010203010201020101030301010202010101010102010301010102010102020203010201010102010102020103020505050505050505050505050505050502010201010102050301010202010201030201010301010101010201030202010101030102010301010402040101020101030301020103010505050505050505050505050505050505050505050505050301020101020304030201010302030101010202010202010301010102020102020103020102010203010102030102020301050505050505050505050505050505050505050505050505050505050505"))
CLUE_COLS = list(unhex("01020102030102010102020103010103020101010301020101010202030101020204030101030301010602010301010202010301050505050505050505050505050505050505050505050505050505050105030102020301020103010101010103010204030201010203030102010106030201050204020105050505050505050505050505050505050505050505050505050505050505050505050505050505010202030101020201010201010202010301020101010301010402010301010102010303010102020108030102010505050505050505050505050505050505050505050505050505050505050505050501010301010202010302010103010201030202010101020203010201030202010103020101020203030301010105010102010101020101020505050505050505050505050505050505050505050505050301020103010101030102010302030202010304020102010102010103010201030301030301010102020301010102010101020101030201010105050505050505050505050505050505050505050505010402040301010203010201030101060201030102010301010203010102010102010304010303010201030105050505050505050505050505050505050505050505050505050505050505050505050501040201010103010201010303020201010101010303010202010305030101010301010203010102030102010201030102010301050505050505050505050505050505050505050505050505050505050101020102010301020101010301010203030201010102010304010101010201030102010302010103010202020101010201030101010201030102020301050505050505050505050505050505050505010202020301030101010202030203010202010202010302020101020201010102010101020202020303020203030201030101010201030105050505050505050505050505050505050505050505050502010102020201030201010103030102020103020301010103010201020201050201030102010101030203030101020105050505050505050505050505050505050505050505050505050505050505050201010301010301020103020201030201020203010102010101020103010101020101030301010102020301010202020301010103010302050505050505050505050505050505050505050505050505020201010202020203030202010201010201010303010201020202040301030102020101020202010104030105050505050505050505050505050505050505050505050505050505050505050505050502020101030102010101020201010301010103010201010103010201010103010101020202020101030302010101030102020201010103010101010505050505050505050505050505050505050505050301010102020101020102010301010102010101020103010101030102020102030202010302010402010101030102020101010103020202020105050505050505050505050505050505050505050505010303010201030201010101030201010201010102010101020101030201030101030201010102010102030502010302030101010505050505050505050505050505050505050505050505050505050501010202030302010101020402010301020101010202010101010201030101010201010202030102010102020103030201010303020203010505050505050505050505050505050505050505050505050201030101020301020101010101010601010303020102020102020101010201010403010201010103010105030205050505050505050505050505050505050505050505050505050505050505050505010102010101010303020101020201010201020101050202030201030301010102010302010403010103010103010505050505050505050505050505050505050505050505050505050505050505050501020201020103010101020103010302020101070301020203020201010102020103030101020201010203010201030202010301030105050505050505050505050505050505050505050505050505050101020103010102030101010201010102010301030102020301010102010102020303010201030102020302010102010301020301010201020101010302020101020505050505050505050505050505010103010105030101010201030102010301010202040101020301010301010102010102030101010301020101010203030102010505050505050505050505050505050505050505050505050505050503040102020103040201020203010103020103010201010203010101020102010103030102010103030102010101020301010201050505050505050505050505050505050505050505050505050505050301010103010202010102010201030101030301010301010201030101010101020101010201010203010101030103020201010203030101010105050505050505050505050505050505050505050505030102010101030201010101020101030204010302010101020101010202010103020102020101010201030103010201020103030103050505050505050505050505050505050505050505050505050501020201030101010302010302010103020302010106020101010202010102010101030101020302030303010101020205050505050505050505050505050505050505050505050505050505050505050301010102020101020101020301020103010103030101030101020103020101020102010103030101020301020303020101030101010305050505050505050505050505050505050505050505050505030101010302030101050301010103010203010103010101020101010301010102020101020101010101020403010104030102010101030101010505050505050505050505050505050505050505050503010202030101020203010103010201030103010102030102010301030201030301020102030303020101020301010202010505050505050505050505050505050505050505050505050505050505050107020101020202030302010102030101010301020103030101030101020201020301040301010103030203050505050505050505050505050505050505050505050505050505050505050505050505020103010104020103020303010102020102030102030201010202020102020102020101030102010102010405050505050505050505050505050505050505050505050505050505050505050505050503010103020101010302010102040102020103010202020103020101020103020201010103020101030101010301030101010505050505050505050505050505050505050505050505050505050505050101010103010201030102010302010103020102020401020202030301020301010202030302010102020101020205050505050505050505050505050505050505050505050505050505050505050505010102010101020101010301020103010301010203020201010203020101030102020302010503020101020102010302020202010301050505050505050505050505050505050505050505050505050501010303010103010202030201020201010102010101030202010101020101010201010101010201010203030302020203020101020103010101030105050505050505050505050505050505050505050102030101010201030102010302010203010201010102010103010303010201010103010201010102010101030102010301020403010201030101030301050505050505050505050505050505050505010302010102020103010104020301010301020101020301020301010201030202020301020101010201030201010301020101010201010205050505050505050505050505050505050505050505050503020201010102010102030301010301010102010302010103010205030101020301010103010201030201050505050505050505050505050505050505050505050505050505050505050505050505050302010703020201010102020301010102010301010203010202010102030303020101040302010105050505050505050505050505050505050505050505050505050505050505050505050505050505030201030102030103010101010103020102030201010302010102010302020101010301020101010303010101030302020201010505050505050505050505050505050505050505050505050505050503010301020101010202020203020103020303010101020201010303030102010101030201030301010102020102020201010505050505050505050505050505050505050505050505050505050505050301010102010102020101030301020101030301020101010202010103030301020103010201010303030102010102010302020103010505050505050505050505050505050505050505050505050505020103010201030103030203010103010201030202020102030503030201010102030101020101020301020103010202010105050505050505050505050505050505050505050505050505050505050502010302010202010202020401010202010302020102030501020101020101010301010101010301010205050505050505050505050505050505050505050505050505050505050505050505050505050102030201010201010102040301020203020103020101030301010102020301010302010301010102010103030301010201030105050505050505050505050505050505050505050505050505050505010203010101020302020103020102010106020101020301020102020202030101020201010102020303020101010505050505050505050505050505050505050505050505050505050505050505050501020201030202020102030403010201030101020302030302040103020101010201030403010201010202010505050505050505050505050505050505050505050505050505050505050505050505050103010202010302010101010303020203020301020103010301020101020201010102020101030101010303020101020201050505050505050505050505050505050505050505050505050505050505010403010102020201050303030202010305020102050101030202010302030203010201030105050505050505050505050505050505050505050505050505050505050505050505050505050505050501010201030201010301020201020102020101010302020103010302010103010203010102020301030101010301010103010201030102010505050505050505050505050505050505050505050505050101010102010102020203010202010203010101020302030301020103010201030101030302020103010105030202010303050505050505050505050505050505050505050505050505050505050505"))

# Build pynogram clue file
color_map = {1:'r ', 2:'g ', 3:'b '}
clue  = "[colors]\n"
clue += "r = (red) 1\n"
clue += "g = (green) 2\n"
clue += "b = (blue) 3\n\n"
clue += "[clues]\n"
clue += "rows = "

for i in range(50):
    for j in range(40):
        value = CLUE_ROWS[2*(j+40*i)]
        if value == 5:
            break
        amount = CLUE_ROWS[2*(j+40*i) + 1]
        clue += str(amount) + color_map[value]
    clue += "\n\t"

clue += "\n"
clue += "columns = "
for i in range(50):
    for j in range(40):
        value = CLUE_COLS[2*(j+40*i)]
        if value == 5:
            break
        amount = CLUE_COLS[2*(j+40*i) + 1]
        clue += str(amount) + color_map[value]
    clue += "\n\t"

# Solve & parse nonogram
open("clue.txt", "w").write(clue)
os.system("pynogram -b ./clue.txt > raw.txt")
raw_nngr = open("raw.txt", "r").read()
nngr = ""
for line in raw_nngr.splitlines():
    if "#" in line:
        pass
    else:
        line = (line[66:] + " ").replace("1 ", "1").replace("2 ", "2").replace("3 ", "3").replace("  ", "0").ljust(50, '0')
        nngr += line + "\n"
open("solution.txt", "w").write(nngr)

# Get flag
r = process(["./RGNN", "solution.txt"])
print(r.recvall())
