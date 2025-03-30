import string as st
import time
import numpy as np

target = 'hello world'
a = ''
s = list(st.ascii_lowercase + ' ')
n, c = 0, 1
while a != target:
    j = np.random.choice(s)
    if j == target[n]:
        a += j
        n += 1
        print(a)
    c += 1
    time.sleep(.005)

print(f'{c}) {a}')