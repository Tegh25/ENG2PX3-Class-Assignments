import numpy as np
from trafficSimulator import *

# Create simulation
sim = Simulation()

# Add multiple roads
sim.create_roads([
  #Positive Y Part
    #Left North to South
    ((-5, -100), (-5, -10)),    #0
    #Middle North to South
    ((0, -100), (0, -5)),       #1
    #Right South to North
    ((5, -10), (5, -100)),      #2

  #Negative Y Part
    #Left North to South
    ((-5, 10),(-5, 100)),       #3
    #Middle South to North
    ((0, 100), (0, 5)),         #4
    #Right South to North 
    ((5, 100), (5, 10)),        #5

  #Positive X part
    #Top East to West
    ((100, -5), (10, -5)),      #6
    #Middle East to West
    ((100, 0), (5, 0)),         #7
    #Down West to East
    ((10, 5), (100, 5)),        #8

  #Negative X part
    #Top East to West
    ((-10, -5), (-100, -5)),    #9
    #Middle West to East
    ((-100, 0), (-5, 0)),       #10
    #Down West to East
    ((-100, 5), (-10, 5)),      #11


  #Intersection  
   #Straight
    #Negative Y to Positive Y
    ((5, 10), (5, -10)),        #12
    #Postive Y to Negative Y
    ((-5, -10), (-5, 10)),      #13
    #Negative X to Positive X
    ((-10, 5), (10, 5)),        #14
    #Positive X to Negative X
    ((10, -5), (-10, -5)),      #15

   #Turns
    #Negative Y to Positive X Right turn
    *turn_road((5, 10), (10, 5), TURN_RIGHT, 20),       #16
    #Negative Y to Negative X Left turn
    *turn_road((0, 5), (-10, -5), TURN_LEFT, 20),       #16 + n

    #Positive X to Postive Y Right turn
    *turn_road((10, -5), (5, -10), TURN_RIGHT, 20),     #16 + 2n
    #Positive X to Negative Y Left turn
    *turn_road((5, 0), (-5, 10), TURN_LEFT, 20),        #16 + 3n

    #Postive Y to Negative X Right turn
    *turn_road((-5, -10), (-10, -5), TURN_RIGHT, 20),   #16 + 4n
    #Positive Y to Postivie X Left turn
    *turn_road((0, -5), (10, 5), TURN_LEFT, 20),        #16 + 5n

    #Negative X to Negative Y Right turn
    *turn_road((-10, 5), (-5, 10), TURN_RIGHT, 20),     #16 + 6n
    #Negative X to Postivie Y Left turn
    *turn_road((-5, 0), (5, -10), TURN_LEFT, 20),       #16 + 7n

])

def road(a): return range(a, a+20)

sim.create_gen({
'vehicle_rate': 20,
'vehicles':[
    [3, {'path': [5, 12, 2]}],
    [1, {'path': [5, *road(16), 8]}],
    [1, {'path': [4, *road(16 + 20), 9]}],

    [3, {'path': [6, 15, 9]}],
    [1, {'path': [6, *road(16 + 2*20), 2]}],
    [1, {'path': [7, *road(16 + 3*20), 3]}],

    [3, {'path': [0, 13, 3]}],
    [1, {'path': [0, *road(16 + 4*20), 9]}],
    [1, {'path': [1, *road(16 + 5*20), 8]}],

    [3, {'path': [11, 14, 8]}],
    [1, {'path': [11, *road(16 + 6*20), 3]}],
    [1, {'path': [10, *road(16 + 7*20), 2]}],
    
    

]})

# Traffic signal
sim.create_signal([[0, 5, 1, 4,], [6, 11, 7, 10,]])


# Start simulation
win = Window(sim)
win.run(steps_per_update=5)