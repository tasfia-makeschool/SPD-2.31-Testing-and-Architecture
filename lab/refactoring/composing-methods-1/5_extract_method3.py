# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

def get_distance(xc1, yc1, xc2, yc2):
    # Calculate the distance between the two circle
    return math.sqrt((xc1-xc2)**2 + (yc1 - yc2)**2)

def get_length(xa, ya, xb, yb):
    # Calculate the length of vector AB vector which is a vector between A and B points.
    return math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))

xc1, yc1 = 4, 4.25
xc2, yc2 = 53, -5.35
print('distance', get_distance(xc1, yc1, xc2, yc2))

xa, ya = -36, 97
xb, yb = .34, .91
print('length', get_length(xa, ya, xb, yb))
