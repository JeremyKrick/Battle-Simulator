"""
Name: Jeremy Krick
RedID: 819826950
Due: 02/12/2020
Homework 2
"""
import numpy as np
import matplotlib.pyplot as plt

# Initial, final, step size info
ti = 0.0
tf = 2.0
dt = 0.01  # Step size

# Number of steps
N = int((tf-ti)/dt)

# Initialize to zero
x_troops = np.zeros(N)
y_troops = np.zeros(N)
time = np.zeros(N)

# Time starts at zero
time[0] = ti

# Troop starting levels - User defined
x_troops[0] = int(input("Enter x-troop starting level (ex: 1000): "))
y_troops[0] = int(input("Enter y-troop starting level (ex: 800): "))

# Lethality coefficients - User defined
alpha = float(input("Enter alpha lethality coefficient (ex: 0.8): "))
beta = float(input("Enter beta lethality coefficient (ex: 0.9): "))

# Integrate using Euler's method
for i in range(N-1):
    time[i+1] = time[i] + dt
    dxdt = -1 * (beta * y_troops[i])
    dydt = -1 * (alpha * x_troops[i])
    dx = dxdt * dt
    dy = dydt * dt
    # When either x_troops or y_troops reaches zero then there are no further casualties
    if x_troops[i] <= 0:
        x_troops[i] = 0
    else:
        x_troops[i+1] = x_troops[i] + dx
    if y_troops[i] <= 0:
        y_troops[i] = 0
    else:
        y_troops[i+1] = y_troops[i] + dy
    print("%6.2f %6.2f %6.2f" % (time[i], x_troops[i], y_troops[i]))

# Display graph
plt.figure()
plt.step(time, x_troops, '-b', label='x-type')
plt.step(time, y_troops, '-r', label='y-type')
plt.xlabel('Time', weight='bold')
plt.ylabel('Survivors', weight='bold')
plt.legend(loc='best')
plt.title("Lancaster's Law for Aimed Fire - Euler's Method", weight='bold')
plt.show()
