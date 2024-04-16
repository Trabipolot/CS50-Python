import numpy as np
from force import Force

force=Force(100,0)


print(force.angle)
print(-np.sin(force.angle))
