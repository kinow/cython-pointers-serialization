# Serialize Cython pointers

Using pointers in Cython objects and trying to serialize these
objects results in errors such as:

```bash
Traceback (most recent call last):
  File "/home/kinow/Development/python/workspace/serialize-cython-pointers/serialize.py", line 25, in <module>
    main()
  File "/home/kinow/Development/python/workspace/serialize-cython-pointers/serialize.py", line 19, in main
    data = pickle.dumps(td)
ValueError: ctypes objects containing pointers cannot be pickled
```

The example library used here is [`pytdigest`](https://pypi.org/project/pytdigest/),
written with Python and Cython (using pointers). It has a constructor with a
property to define the compression, but no other parameters for the data and
other properties that are calculated when data is given to the object.

This means we are not able to use Python's [`Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler)
and [`Unpickler`](https://docs.python.org/3/library/pickle.html#pickle.Unpickler).
