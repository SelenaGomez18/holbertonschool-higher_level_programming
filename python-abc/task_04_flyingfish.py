#!/usr/bin/env python3

class Fish:
    def swim(self):
        print (f"The fish is swimming")
    def habitat(self):
        print (f"The fish lives in water")

class Bird:
    def fly(self):
        print (f"The bird is flying")
    def habitat(self):
        print (f"The bird lives in the sky")

class FlyingFish(Fish, Bird):
    def __init__(self):
        super().__init__()
    def swim(self):
        print (f"The flying fish is swimming!")
    def fly(self):
        print (f"The flying fish is soaring!")
    def habitat(self):
        print (f"The flying fish lives both in water and the sky!")
