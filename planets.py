import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.offsetbox import OffsetImage, AnnotationBbox

paths = ['merkury.png', 'wenus.png', 'ziemia.png', 'mars.png', 'saturn.png', 'jowisz.png', 'uran.png', 'neptun.png']

def getImage(path, zoom=0.05):
    return OffsetImage(plt.imread(path), zoom=zoom)

data = {
    "Semi-major ax r [AU]": [0.3870321, 0.7232620, 1.0000000, 1.5233957, 5.2045455, 9.5822193, 19.2012032, 30.0474599],
    "Orbital period T [years]": [0.2409639, 0.6152793, 1.0000000, 1.8811610, 11.8592552, 29.4277108, 83.7595838, 163.7458927]
}
df = pd.DataFrame(data)
df

x = []
y = []
for i in range(8):
    a = df.loc[i]['Semi-major ax r [AU]']
    b = df.loc[i]['Orbital period T [years]']
    x.append(a)
    y.append(b)
x

plt.style.use('dark_background')
fig = plt.figure(figsize = (15, 10))
ax = fig.add_subplot()


ax.scatter(x, y)
ax.plot(x,y, 'white', linewidth = 1)
for x0, y0, path in zip(x, y,paths):
    ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
    ax.add_artist(ab)
    
ax.set_ylim(1/10, 1000)
ax.set_yscale('log')
ax.set_xlim(1/10, 100)
ax.set_xscale('log')

plt.xlabel('Semi-major ax - r [AU]', fontsize=12)
plt.ylabel('Orbital period - T [years]', fontsize=12)

ax.text(30, 1, r"$\frac{T^2}{r^2}=const$", fontsize = 15)

plt.savefig('planets.pdf', dpi=100)
plt.show()