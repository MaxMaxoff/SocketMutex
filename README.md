# SocketMutex #

**SocketMutex** python3 module for realize locking mechanism using sockets

## Requirements
* socket (build-in)
* sys (build-in)

## Details ##
### Preparations

Install Mutex using pip:

```bash
$ pip install [--user] socketmutex
```

### Usage
Import module:

```python
from SocketMutex import Mutex
```

Example 1
```python
# import module
import os  # just to determine script name
from SocketMutex import Mutex

# create killer
mutex = Mutex(f"{os.path.basename(__file__)}")  # using script name as market for mutex for python 3.6 or above
mutex = Mutex('{}'.format(os.path.basename(__file__)))  # using script name as market for mutex for python 3.5 and older

# try to set lock and continue, otherwise do something else
if mutex.set_lock():
    # do stuff
else:
    # do another stuff

# try to release lock and continue, otherwise do something else
if mutex.release_lock():
    # do stuff
else:
    # do another stuff


```