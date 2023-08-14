import matplotlib.pyplot as plt

# Data
labels = ['Circle 1', 'Circle 2']
diameters = [1, 2.7]  # Diameter of the second circle is 2.7 times bigger

# Create a figure and axis
fig, ax = plt.subplots()

# Add circles to the plot
for label, diameter in zip(labels, diameters):
    circle = plt.Circle((diameter / 2, 0.5), diameter / 2, color='blue' if label == 'Circle 1' else 'orange', alpha=0.5)
    ax.add_patch(circle)

# Set aspect ratio to equal, remove axes, and set title
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Two Circles with Different Diameters')

# Show the plot
plt.show()
