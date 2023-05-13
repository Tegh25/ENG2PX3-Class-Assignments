import numpy as np
from trafficSimulator import *

# Create simulation
sim = Simulation()

# Add multiple roads
sim.create_roads([
    ((-100,0), (0, 0)),
    ((20, 20), (20, 110)),

    *turn_road((0, 0), (20, 20), TURN_RIGHT, 20)
])

sim.create_gen({
    'vehicle_rate': 5,
    'vehicles': [
        [1, {"path": [0, *range(2,22), 1]}]
    ]
})


# Start simulation
win = Window(sim)
win.run(steps_per_update=5)