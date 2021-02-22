# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math


def distance_between_two_circle(circle1x, circle1y, circle2x, circle2y):
  # Calculate the distance between the two circles
  distance = math.sqrt((circle1x-circle2x)**2 + (circle1y - circle2y)**2)
  print('distance', distance)


def vector_length(xa, ya, xb, yb):
  # calcualte the length of vector AB vector which is a vector between A and B points.
  length = math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))
  print('length', length)


if __name__ == "__main__":
    distance_between_two_circle(4, 4.25, 53, -5.35)
    vector_length(-36, 97, .34, .91)
