# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 13:22:35 2025

@author: HamnaHasan
"""
## My name is Hamna and I love water. I’m happiest when I’m near water, whether it's a lab constructed channel or a flowing stream of water running down my stairs after a rain. 

## With my Civil engineering background, I haven't really done coding/programming and this code is one of my first attempts in learning my way around these.
## This code takes on assumed values to plot an Energy Depth curve for water flowing in an open rectangular channel


import numpy as np
import matplotlib.pyplot as plt

g = 9.81 #acceleration due to gravity in m/s2 

## q is discharge per unit width of an open channel measured in m3/s per m of channel

def E(y, q):             #Specific Energy of moving fluid measured in m
    return y + q**2 / (2 * g * y**2)


def yc(q):               #Critical depth of water where water has minimum Specific Energy E (measured in m)
    return (q**2 / g)**(1/3)

def Emin(q):            #Minimum Specific Energy when flow is critical
    return 1.5 * yc(q)


#creating array for depth y
y = np.linspace(0.05, 5, 500)

#assuming q
q = [1, 2, 3]

##plotting E–y curves at fixed q:
    
plt.figure(figsize=(8,6))
for q in q:
    E_vals = E(y, q)
    plt.plot(y, E_vals)
    plt.scatter(yc(q), Emin(q), label=f"q={q}")
    plt.annotate(f"yc={yc(q):.2f}\nEmin={Emin(q):.2f}",
                 xy=(yc(q), Emin(q)), xytext=(5, 8),
                 textcoords='offset points', fontsize=3.5)
    
plt.xlabel("Depth y (m)")
plt.ylabel("Specific Energy E (m) ")
plt.title("E vs y for different q values")
plt.legend()   # show legend
plt.show()


q_sel = 2.0
E_vals = E(y, q_sel)


## Visual identification of alternate depths:
    
q_sel = 2.0
E_vals = E(y, q_sel)

plt.figure(figsize=(8,6))
plt.plot(y, E_vals, label=f"q = {q_sel} m²/s")
plt.axhline(Emin(q_sel)+0.5, linestyle="--", label="E* line")

plt.xlabel("Depth y (m)")
plt.ylabel("Specific Energy E (m) ")
plt.title("E vs y")
plt.legend()   # show legend
plt.show()
