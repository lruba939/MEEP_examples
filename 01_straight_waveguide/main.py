import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.taskManager import *
from utils.sys_utils import *

def main():
    #### Task 1
    print_task(1, "Making medium - a straight waveguide.")
    wg = task_1(plot=True)

    print_task(2, "Calculations of the scalar electric field Ez as result of continuous source radiation.")
    task_2(wg, plot=True)

    
if __name__ == "__main__":
    main()
