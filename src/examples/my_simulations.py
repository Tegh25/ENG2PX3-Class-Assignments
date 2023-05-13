import numpy as np
from trafficSimulator import *

sim = Simulation()


# Add multiple roads
sim.create_roads([
    # South To North 
    ((-2, -50), (-2, 0)),
    ((-2, 0), (-2, 50)),

    # North To South
    ((2, 50), (2, 0)),
    ((2, 0), (2, -50)),

    # East to West
    ((50, -2),(0, -2)),
    ((0, -2),(-50, -2)),

    # West to East
    ((-50, 2),(0, 2)),
    ((0, 2),(50, 2)),
])

sim.create_gen({
    'vehicle_rate': 5,
    'vehicles': [
        [1, {"path": [0, 1]}],
        [1, {"path": [2, 3]}],
    ]
})

sim.create_signal([[0, 2]])

# Start simulation
win = Window(sim)
win.zoom = 10
win.run(steps_per_update = 5)
