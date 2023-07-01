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
