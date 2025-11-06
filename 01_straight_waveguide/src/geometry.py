from . import params
import meep as mp

# inicialize singleton of all parameters
p = params.SimParams()

# cell is the whole sim box
def make_cell():
    cell = mp.Vector3(p.xyz_cell[0], p.xyz_cell[1], p.xyz_cell[2])
    return cell

# waveguide geometry
def make_medium():
    geometry = [
        mp.Block(
            mp.Vector3(p.xyz_wg[0], p.xyz_wg[1], p.xyz_wg[2]),
            center = p.center,
            material = p.material,
        )
    ]
    return geometry