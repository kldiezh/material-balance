import matplotlib.pyplot as plt
import numpy as np
from Undersaturated_reservoir import *
from Saturated_reservoir import *

# Data for Undersaturated and saturated period

t = np.concatenate((t_UR, t_SR)) * 12 # time, months

Np = np.concatenate((Np_UR, Np_SR)) * 1000000 # Np, STB

qo = np.concatenate((qo_UR, qo_SR)) # Oil rate, STB/D

# Data visualization

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
fig.suptitle('Production Data Analysis', fontsize=14, fontweight='bold')

ax1.plot(t, Np, color='orange', label='Np')
ax1.set_xlabel('Time (months)', fontsize=10, fontweight='bold')
ax1.set_ylabel('Np (STB)', fontsize=10, fontweight='bold')
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
ax1.set_title('Cumulative oil production', fontsize=10)

ax2.plot(t, qo, color='purple', label='qo', marker="*", markerfacecolor="cyan")
ax2.set_xlabel('Time (months)', fontsize=10, fontweight='bold')
ax2.set_ylabel('qo (STB/D)', fontsize=10, fontweight='bold')
ax2.grid(True, which='both', linestyle='--', linewidth=0.5)
ax2.set_title('Oil production rate', fontsize=10)

plt.tight_layout()

plt.show()


