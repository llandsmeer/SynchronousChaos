# https://aip.scitation.org/doi/full/10.1063/1.4917383

import numpy as np
import matplotlib.pyplot as plt

N = 100

with plt.style.context('Solarize_Light2'):

    fig, ax = plt.subplots(ncols=2, sharey=True)


    for a in np.linspace(-2, 2, 20):

        #a = 1
        b = 1

        x, y, z = np.random.random(3)

        out = np.empty((N, 4))

        for i in range(N):
            x, y, z = (
                    a * x * ( 1 - x ),
                    b * x * ( 1 - y ),
                    b * x * ( 1 - z )
                    )
            d = np.log(abs(z - y)) if z != y else float('nan')
            out[i] = (x, y, z, d)

        ax[0].plot(out[:,3])

    for b in np.linspace(-2, 2, 20):

        a = 1
        #b = 1

        x, y, z = np.random.random(3)

        out = np.empty((N, 4))

        for i in range(N):
            x, y, z = (
                    a * x * ( 1 - x ),
                    b * x * ( 1 - y ),
                    b * x * ( 1 - z )
                    )
            d = np.log(abs(z - y))
            out[i] = (x, y, z, d)

        ax[1].plot(out[:,3])

    ax[0].set_title(r'Param sweep $\alpha \in \left[-2, 2\right]$')
    ax[1].set_title(r'Param sweep $\beta \in \left[-2, 2\right]$')
    ax[0].set_xlabel(r'Iteration')
    ax[0].set_ylabel(r'$\log\left(\left|y-z\right|\right)$')
    ax[1].set_ylabel(r'$\log\left(\left|y-z\right|\right)$')
    plt.show()


