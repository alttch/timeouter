# timeouter

Timeout helper tools library for Python

## Install

```python
pip3 install timeouter
```

## Examples

### Simple class usage

```python
import timeouter, time

t = timeouter.Timer(1)
time.sleep(0.5)
t.has(0.1) # True
t.has(0.6) # False
t.get() # returns remaining time
t.get(laps=3) # returns remaining time, split into 3 equal laps
t.reset() # resets timeout counter

# raises TimeoutError if timer has expired, message is optional
t.check(message=message)

# get remaining time, raise TimeoutError if expired, message is optional
t.get(check=True, check_message=message)
```

### Custom timeout exception

Exception for the single timer object

```python
class MyException(Exception): pass

t.set_exception_class(MyException)
```

Default exception for all new timers

```python
class MyException(Exception): pass

timeouter.set_default_exception_class(MyException)
```

### Thread-local usage

```python
import timeouter as to

# init for the current thread
to.init(1)
time.sleep(2)
# module methods check, get, has, reset, set_timeout and set_exception_class
# are proxied to thread-local object
to.check()
```
