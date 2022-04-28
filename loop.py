import sys
import serial

def test(rounds):
    counter = 1
    for x in range(rounds):

        print("prikaz" + str(x))
        rounds = rounds - 1
        # increase counter
        counter += 1
        print(str(rounds) + " rounds")


test(5)