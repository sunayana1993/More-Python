import gc
#enable garbage collector
gc.enable()
gc.disable()
#Python includes cyclic garbage collector to handle refernce cycles.Reference cycle occurs when object
#reference each other, preventing reference count to be 0
print(gc.collect())
#gives output of unreachable object.
print(gc.get_stats())
print(gc.garbage)
