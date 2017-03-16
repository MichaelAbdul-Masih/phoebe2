"""
"""

import phoebe
from phoebe import u
import numpy as np
import matplotlib.pyplot as plt
import os

phoebe.devel_on()
phoebe.interactive_off()

def test_binary(plot=False):
    dir = os.path.dirname(os.path.realpath(__file__))

    b = phoebe.Bundle.from_legacy(os.path.join(dir, 'kic12004834.phoebe'))
    # this phoebe legacy file uses extern_planckint and with albedos to 0
    # and exptime already defined
    b.set_value_all('atm', 'blackbody')
    b.set_value('irrad_method', 'none')

    times = b.to_time(np.linspace(-0.5, 0.5, 25)) # hardcoded to length of files
    b.set_value('times', times)

    b.run_compute(fti_method='none')
    fluxes_legacy = np.loadtxt(os.path.join(dir, 'kic12004834.nofti.data'), unpack=True, usecols=(1,))
    fluxes = b.get_value('fluxes', context='model')


    if plot:
        print "fti off"
        print abs(fluxes_legacy-fluxes).max()
        plt.plot(times, fluxes_legacy, 'k-')
        b.plot()
        plt.legend()
        plt.show()
    assert(np.allclose(fluxes, fluxes_legacy, rtol=0, atol=1e-2))


    b.run_compute(fti_method='oversample', fti_oversample=5)
    fluxes_legacy = np.loadtxt(os.path.join(dir, 'kic12004834.fti.data'), unpack=True, usecols=(1,))
    fluxes = b.get_value('fluxes', context='model')

    if plot:
        print "fti on"
        print abs(fluxes_legacy-fluxes).max()
        plt.plot(times, fluxes_legacy, 'k-')
        b.plot()
        b.plot()
        plt.legend()
        plt.show()
    assert(np.allclose(fluxes, fluxes_legacy, rtol=0, atol=1e-2))





    return b

if __name__ == '__main__':
    logger = phoebe.logger(clevel='INFO')


    b = test_binary(plot=True)