import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Set up figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 15)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Traffic Light Simulation", fontsize=14, fontweight='bold')

# Define traffic light properties
light_states = ["Red", "Green", "Yellow"]
light_colors = {"Red": "red", "Green": "green", "Yellow": "yellow"}
light_timing = {"Red": 40, "Green": 30, "Yellow": 10}  # Frame counts for each state

# Initial light state
current_light = "Red"
frame_count = 0

# Car properties
cars = []
lane_positions = [2, 5, 8]  # Three lanes


# Car class for movement
class Car:
    def __init__(self, lane):
        self.lane = lane
        self.y = 0 if current_light == "Red" else random.randint(2, 6)  # Random start position
        self.speed = 0 if current_light == "Red" else random.uniform(0.1, 0.3)  # Speed based on light
        self.rect = plt.Rectangle((self.lane, self.y), 1.5, 1, facecolor="blue", edgecolor="black")

    def move(self):
        if current_light == "Green":
            self.speed = random.uniform(0.2, 0.5)  # Move faster when green
        elif current_light == "Yellow":
            self.speed = random.uniform(0.1, 0.2)  # Slow down in yellow
        else:
            self.speed = 0  # Stop in red

        self.y += self.speed

    def draw(self):
        ax.add_patch(self.rect)


# Function to update simulation
def update(frame):
    global frame_count, current_light, cars

    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 15)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"Traffic Light: {current_light}", fontsize=14, fontweight='bold')

    # Change traffic light state based on frame count
    frame_count += 1
    if frame_count >= light_timing[current_light]:
        frame_count = 0
        current_light = light_states[(light_states.index(current_light) + 1) % 3]

    # Draw traffic light
    traffic_light = plt.Rectangle((4.5, 13), 1.5, 2, facecolor=light_colors[current_light])
    ax.add_patch(traffic_light)

    # Add new cars at random intervals
    if random.random() < 0.3:  # 30% chance to spawn a car each frame
        new_car = Car(random.choice(lane_positions))
        cars.append(new_car)

    # Move and draw cars
    for car in cars:
        car.move()
        car.rect.set_xy((car.lane, car.y))
        car.draw()

    # Remove cars that exit the screen
    cars = [car for car in cars if car.y < 15]


# Run animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=100)
plt.show()
