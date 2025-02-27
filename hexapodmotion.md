import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 1)
ax.set_title("Sazid's  Hexapod Walking Motion Simulation")

# Define initial hexapod leg positions
legs = {
    "LF": [-1, 0.5],  # Left Front
    "LM": [-1, 0],  # Left Middle
    "LR": [-1, -0.5],  # Left Rear
    "RF": [1, 0.5],  # Right Front
    "RM": [1, 0],  # Right Middle
    "RR": [1, -0.5]  # Right Rear
}

# Create scatter plot for legs
points, = ax.plot([], [], 'ro', markersize=10)

# Define gait cycle phases (Forward and Backward)
gait_cycle = [
    {"lift": ["RF", "LM", "RR"], "move": ["RF", "LM", "RR"], "lower": ["RF", "LM", "RR"], "push": ["LF", "RM", "LR"]},
    {"lift": ["LF", "RM", "LR"], "move": ["LF", "RM", "LR"], "lower": ["LF", "RM", "LR"], "push": ["RF", "LM", "RR"]}
]

# Convert legs dictionary to array for easy updating
leg_names = list(legs.keys())
leg_positions = np.array(list(legs.values()))


# Animation update function
def update(frame):
    phase = frame % len(gait_cycle)
    cycle = gait_cycle[phase]

    # Adjust leg positions for each phase
    for leg in cycle["lift"]:
        leg_positions[leg_names.index(leg)][1] += 0.2  # Lift leg

    for leg in cycle["move"]:
        leg_positions[leg_names.index(leg)][0] -= 0.2  # Move leg forward

    for leg in cycle["lower"]:
        leg_positions[leg_names.index(leg)][1] -= 0.2  # Lower leg

    for leg in cycle["push"]:
        leg_positions[leg_names.index(leg)][0] += 0.2  # Push body forward

    # Update plot data
    points.set_data(leg_positions[:, 0], leg_positions[:, 1])
    return points,


# Create animation
ani = animation.FuncAnimation(fig, update, frames=10, interval=500, blit=True)

# Show animation
plt.show()
