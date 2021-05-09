from cane import Cane
from animali import *

cani = [ Cane("Phil", 12, colore='bianco'), Cane("Roger", 4) ]

print(" printo i cani: ")
for cane in cani:
    print(cane)



print("\nprinto gli altri animali domestici: ")

i_miei_animali_domestici = [
    Mammuth("rick"),
    Cocorita("chop")
]

for animale in i_miei_animali_domestici:
    print(animale, end=" ")
    print(animale.zanne())
