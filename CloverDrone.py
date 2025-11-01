from cbc import CloverDrone
import Move
import time

if __name__ == '__main__':
    CloverDrone()
    CloverDrone.nto(1)
    time.sleep(3)
    CloverDrone.land()