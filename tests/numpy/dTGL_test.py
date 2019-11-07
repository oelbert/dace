import dace
import numpy as np

# Declaration of symbolic variables
N, BS = (dace.symbol(name) for name in ['N', 'BS'])


@dace.program
def dTGL_test(HD: dace.complex128[N, BS, BS], HE: dace.complex128[N, BS, BS],
              dTGL: dace.complex128[N]):

    for n in range(1, N - 1):
        trace_tmp = HD[n] @ HE[n]
        for i in dace.map[0:BS]:
            dTGL[n] += trace_tmp[i, i]


if __name__ == '__main__':

    dTGL_test.compile()
