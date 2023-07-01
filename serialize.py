#!/usr/bin/env python3

from pytdigest import TDigest
import numpy as np
import pandas as pd


def main():
    rng = np.random.default_rng(12354)
    n = 100_000
    x = rng.normal(loc=0, scale=10, size=n)
    w = rng.exponential(scale=1, size=n)

    td = TDigest.compute(x, w, compression=1_000)
    


if __name__ == '__main__':
    main()
