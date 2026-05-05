import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Load dataset
df = pd.read_csv("student_data.csv")

# Columns
numeric_cols = [
    "age", "Medu", "Fedu", "traveltime", "studytime",
    "failures", "famrel", "goout", "absences", "G3"
]

# Assign distribution names (you can adjust if needed)
distribution_names = [
    "Normal",        # age
    "Discrete",      # Medu
    "Discrete",      # Fedu
    "Right-Skewed",  # traveltime
    "Right-Skewed",  # studytime
    "Poisson-like",  # failures
    "Uniform-like",  # famrel
    "Normal-like",   # goout
    "Exponential",   # absences
    "Normal"         # G3
]

# Colors
colors = [
    "#378ADD", "#1D9E75", "#D85A30", "#D4537E", "#7F77DD",
    "#639922", "#BA7517", "#3B6D11", "#E24B4A", "#888780"
]

# Create figure
fig, axes = plt.subplots(2, 5, figsize=(20, 8))
fig.suptitle("Student Dataset — Family of Distributions", 
             fontsize=15, fontweight='bold', y=1.02)

for ax, col, dist_name, color in zip(axes.flatten(), numeric_cols, distribution_names, colors):
    values = df[col].dropna()

    # Better bins
    bins = values.nunique() if values.nunique() < 10 else 15

    # Histogram
    ax.hist(values, bins=bins, color=color,
            edgecolor='white', linewidth=0.5, alpha=0.9,
            density=True)

    # Normal curve (optional but good)
    mu, std = norm.fit(values)
    x = np.linspace(values.min(), values.max(), 100)
    y = norm.pdf(x, mu, std)
    ax.plot(x, y, color='black', linewidth=1.2)

    # ✅ TOP = Distribution name
    ax.set_title(f"{dist_name}", fontsize=11, fontweight='bold')

    # ✅ BOTTOM = Column name
    ax.set_xlabel(col, fontsize=9, color='#444')

    ax.set_ylabel("Density", fontsize=8, color='#444')
    ax.tick_params(labelsize=7)

    # Clean look
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig("final_family_distributions.png", dpi=150, bbox_inches='tight')
plt.show()