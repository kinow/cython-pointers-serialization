#!/usr/bin/env python3

from pytdigest import TDigest
import numpy as np
import pandas as pd

import io
import pickle


class PicklableTDigest:

    def __init__(self, tdigest: TDigest) -> None:
        self.tdigest = tdigest

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return getattr(self, attr)
        return getattr(self.tdigest, attr)

    def __getstate__(self):
        """Here we select what we want to serializable from TDigest.

        We will pick only the necessary to re-create a new TDigest.
        """
        state = {
            'centroids': self.tdigest.get_centroids(),
            'compression': self.tdigest.compression
        }
        return state

    def __setstate__(self, state):
        """Then here we use the data we serialized to deserialize it.

        We use that data to create a new instance of TDigest. It has
        some static functions to re-create or combine TDigest's.

        Here ``of_centroids`` is used to demonstrate how it works.
        """
        self.tdigest = TDigest.of_centroids(
            centroids=state['centroids'],
            compression=state['compression']
        )

    def __repr__(self):
        return repr(self.tdigest)


def main():
    rng = np.random.default_rng(12354)
    n = 100_000
    x = rng.normal(loc=0, scale=10, size=n)
    w = rng.exponential(scale=1, size=n)

    td = TDigest.compute(x, w, compression=1_000)
    print(td)

    # ValueError: ctypes objects containing pointers cannot be pickled
    # data = pickle.dumps(td)

    # Instead, let's make a wrapper object, that likes pickles.
    td = PicklableTDigest(td)
    print(td)

    data = pickle.dumps(td, protocol=0)
    print(data)

    deserialized_td = pickle.loads(data)
    print(deserialized_td)

if __name__ == '__main__':
    main()
