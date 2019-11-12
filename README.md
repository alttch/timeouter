# timeouter

Timeout helper tools library for Python

## Examples

### Simple class usage

```python
import timeouter, time

t = timeouter.Timeouter(1)
time.sleep(0.5)
t.has(0.1) # True
t.has(0.6) # False
t.get() # returns remaining time
t.reset() # resets timeout counter
t.check(message=message) # raises TimeoutException if timed out
```

### Custom timeout exception

Exception for the single class

```python
class MyException(Exception): pass
t.set_exception_class(MyException)
```

Default exception
```
class MyException(Exception): pass
timeouter.set_default_exception_class(MyException)
```

### Thread-local usage

```python
# init
timeouter.init(1)
time.sleep(2)
# module methods check, get, has, reset, set_timeout and set_exception_class
# are proxied to thread-local object
timeouter.reset()
timeouter.check()
```
