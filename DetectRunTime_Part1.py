#RunTime Excerise:

#Simple RunTime detection
from datetime import datetime

def inner():
    s = 0

    for i in range(0, 10000000):
        s = s + 1
    print(s)

start = datetime.now()

inner()

end = datetime.now()

print(end - start)


#RunTime detection - Why Numpy?
print("Why numpy part")
import numpy as np
import math

#Amount of entries to analyse:
n = 10000000

entries_np = np.random.random(n)

entries = list(entries_np)

start01 = datetime.now()

out = []
for entry in entries:
    out.append(math.sqrt(entry))

end01 = datetime.now()

print("First example (without listcomprehention")
print(end01 - start01)

start02 = datetime.now()

out = [math.sqrt(entry) for entry in entries]

end02 =datetime.now()

print("Second example (with listcomprehention)")
print(end02 - start02)

start03 = datetime.now()

out = np.sqrt(entries_np)

end03 =datetime.now()

print("Third example (with numpy)")
print(end03 - start03)