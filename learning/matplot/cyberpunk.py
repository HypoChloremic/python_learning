import matplotlib.pyplot as plt
import mplcyberpunk
plt.style.use("cyberpunk")
plt.plot([1, 3, 9, 5, 2, 1, 1], marker='o')
plt.plot([4, 5, 5, 7, 9, 8, 6], marker='v')
plt.plot([2, 3, 4, 3, 4, 5, 3], marker='s')# Add glow effects-Optional
mplcyberpunk.add_glow_effects()
plt.show()