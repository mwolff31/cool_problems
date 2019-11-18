import numpy as np
import matplotlib.pyplot as plt

def f(l):
	return (1/4) * (768 * l - l**3)

def update(l, alpha):
	return l + alpha * (1/4) * (768 - 3*l**2)

def optimize(l, alpha):
	volumes = []
	ls = []
	steps = 0
	old_l = l
	new_l = update(l, alpha)
	while np.abs(f(old_l) - f(new_l)) > 1e-50:
		old_l = new_l
		new_l = update(old_l, alpha)
		volume_i = f(new_l)
		print('volume:', volume_i, ' ', 'l:', new_l)
		volumes.append(volume_i)
		ls.append(new_l)
		steps+=1
	return new_l, volume_i, steps, np.asarray(volumes), np.asarray(ls)

l = np.random.uniform(0., 24.)
l, final_volume, num_steps, volumes, ls = optimize(l, alpha=1e-5)
print('final volume:', final_volume, ' ', 'final l:', l, ' ', 'number of steps:', num_steps)
print('h:', (768-l**2)/(4*l))

fig1 = plt.figure(1)
plt.scatter(np.arange(num_steps), volumes, s=4.)
plt.ylabel('Volume')
plt.xlabel('Steps')
plt.title('Volume vs. Gradient Descent Steps')

x0 = np.arange(0,24)
x = np.append(x0, ls)
y = f(x)

colors = ['blue']*x0.shape[0] + ['red']*ls.shape[0]
s = [10.]*x0.shape[0] + [0.05] * ls.shape[0]

fig2 = plt.figure(2)
plt.scatter(x, y, color=colors, s =s)
plt.ylabel('Volume')
plt.xlabel('$l$')
plt.title('Volume vs $l$')
plt.show()
