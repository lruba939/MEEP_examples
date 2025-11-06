from . import params
from . import simulation

import meep as mp
import matplotlib.pyplot as plt
import numpy as np

# inicialize singleton of all parameters
p = params.SimParams()

# TASK 1 -------------------------------

def task_1(plot=False):
    sim = simulation.make_sim()    
    simulation.start_calc(sim)
    
    eps_data = sim.get_array(center=mp.Vector3(), size=p.xyz_cell, component=mp.Dielectric)
    
    if plot:
        plt.figure()
        plt.imshow(eps_data.transpose(), interpolation="spline36", cmap="binary")
        plt.axis("off")
        plt.show()

    return eps_data