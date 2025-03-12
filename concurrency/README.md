# Python Concurrency

## Multiprocessing

__Multiprocessing__ package spawn multiple processes in the system.
Offers local and remote concurrency.

### [Pool](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool)
Control __pool__ of workers to which jobs can be dispatched. The jobs can be dispatched to:
 - *apply* or *apply_async*
 - *map* or *map_async*
 - *imap* or *imap_async*
 - *starmap* or *starmap_async*

The *apply* and *map* blocks the main thread until all processes are finished. The *async*
counterparts start a process and returns immediately with a *AsyncResult* object. This object has
*get*, *wait*, *ready* and *successful* methods that can be used to fetch the results when process
completes.

*imap* is lazy itertable version of *map*. And the *starmap* passes arguments as itertable of itertable.

These methods use *start*, *close*, *terminate* and *join*.

### Process


### Pipe


### Lock


### Value or Array
