## Singleton of parameters
import numpy as np
import meep as mp

class SimParams:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance._init_parameters()
        return cls._instance
    
    def _init_parameters(self):

        # Geometry
        self.xyz_cell = [16, 8, 0]
        self.xyz_wg = [mp.inf, 1, mp.inf]
        self.center = mp.Vector3()
        self.material = mp.Medium(epsilon=12)
        
        # Source
        self.freq = 0.15
        self.component = mp.Ez
        self.xyz_src = [-7,0,0]
        
        ## Simulation settings
        self.pml = 1.0
        self.resolution = 10
        self.sim_time = 200

    def reset_to_defaults(self):
        self._init_parameters()
        
    def showParams(self):
        print("\n\n#################################\nSimulation and System Parameters:\n")
        for k, v in self.__dict__.items():
            if not k.startswith('_'):
                if not isinstance(v, (list, dict, tuple, np.ndarray)): #
                    print(f"{k} = {v}")
                else:
                    print(f"{k} = {v[:5]}")
        print("#################################\n\n")