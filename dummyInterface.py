import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Create the main window
root = tk.Tk()
root.title("Rocket Data Visualization")
root.geometry("800x600")

# Data initialization
time, altitude, velocity, pressure, acceleration, temperature = 0, 2, 500, 390, 0, 0

# Create labels for each piece of data
labels = {
  "Altitude": tk.Label(root, text="Altitude: "),
  "Velocity": tk.Label(root, text="Velocity: "),
  "Pressure": tk.Label(root, text="Pressure: "),
  "Temperature": tk.Label(root, text="Temperature: "),
  "Acceleration": tk.Label(root, text="Acceleration: "),
}
for i, (label_text, label) in enumerate(labels.items()):
  label.grid(row=i // 2 + 1, column=i % 2 * 2, padx=10, pady=5, sticky="w")

# Create a container for the buttons
button_frame = tk.Frame(root)
button_frame.grid(row=4, column=0, columnspan=3, pady=10)

def toggle_pause():
  global is_paused
  is_paused = not is_paused
  pause_button.config(text="Resume" if is_paused else "Pause")

# Add a button to pause/resume updates
is_paused = False
pause_button = tk.Button(button_frame, text="Pause", command=lambda: toggle_pause())
pause_button.pack(side=tk.LEFT, padx=5)

# Initialize a list to store the data
data = {
  "altitude": [],
  "velocity": [],
  "pressure": [],
  "temperature": [],
  "acceleration": [],
  "time": [],
}

# Create subplots and canvases
fig, axs = plt.subplots(2, 3, figsize=(15, 7))
canvas = FigureCanvasTkAgg(fig, master=root)

for i, ax in enumerate(axs.flat):
  if i < len(labels):
    label_text = list(labels.keys())[i]
    ax.set_xlabel('Time (s)')
    ax.set_ylabel(labels[label_text].cget("text").strip().rstrip(":"))

# Adjust margins
fig.subplots_adjust(left=0.2, bottom=0.2)

# Clear the subplots
for ax in axs.flat:
  ax.clear()

# Display canvases
canvas.get_tk_widget().grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Function to toggle pause/resume
# Function to update the data
def update_data():
  try:
    global time, altitude, velocity, pressure, acceleration, temperature

    # Pause updates if the button is pressed
    if is_paused:
      root.after(1000, update_data)
      return

    time += 1
    altitude = time ** 3
    velocity = time ** 2
    pressure = time
    acceleration = time
    temperature = time

    # Update the labels with the new data
    labels["Altitude"].config(text=f"Altitude: {altitude}")
    labels["Velocity"].config(text=f"Velocity: {velocity}")
    labels["Pressure"].config(text=f"Pressure: {pressure}")
    labels["Temperature"].config(text=f"Temperature: {temperature}")
    labels["Acceleration"].config(text=f"Acceleration: {acceleration}")

    # Add the new data to the list
    data["altitude"].append(float(altitude))
    data["velocity"].append(float(velocity))
    data["pressure"].append(float(pressure))
    data["temperature"].append(float(temperature))
    data["acceleration"].append(float(acceleration))
    data["time"].append(time)

    

    # Plot the data
    for ax, (label_text, values) in zip(axs.flat, data.items()):
      ax.plot(data["time"], values,color='green')
      ax.set_title(f"{label_text} vs Time")

    # Redraw the canvas
    canvas.draw()

    # Schedule the next update
    root.after(1000, update_data)
  except Exception as e:
    print(e)
    # Display the error message in a messagebox
    messagebox.showerror("Error", str(e))

# Schedule the first update
root.after(1000, update_data)


# Start the Tkinter main loop
root.mainloop()
