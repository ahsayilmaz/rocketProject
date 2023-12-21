import tkinter as tk
from matplotlib.figure import Figure
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import socket

# Create the main window
root = tk.Tk()
root.title("Rocket Data Visualization")
root.geometry("800x600")

# Create a socket object
s = socket.socket()

# Define the host and the port on which you expect to receive data
host = 'localhost'  # replace with your host
port = 12345  # replace with your port

# Bind to the port
s.bind((host, port))

# Wait for client connection
s.listen(5)
c, addr = s.accept()

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


# Create a Figure and a Canvas to display a graph
fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Create a subplot in the Figure
ax = fig.add_subplot(111)

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

def update_data():
    # Receive data from the LoRa module
    raw_data, _ = c.recvfrom(1024)
    time +=1
    # Decode and split the data into the different pieces
    # This depends on how your data is formatted
    altitude, velocity, pressure, temperature, acceleration = raw_data.decode().split(',')

    # Pause updates if the button is pressed
    if is_paused:
      root.after(1000, update_data)
      return

    # Update the labels with the new data
    acceleration = 9.8  # Assign a value to the "acceleration" variable

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

    # Redraw the Canvas
    canvas.draw()

    # Schedule the next update
    root.after(1000, update_data)

# Schedule the first update
root.after(1000, update_data)

# Start the main loop
root.mainloop()
