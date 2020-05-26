from dronekit import connect

# Connect to the Vehicle (in this case a UDP endpoint)
vehicle = connect('/dev/ttyAMA0', wait_ready=True, baud=57600)

print("Mode: {0}".format(vehicle.mode.name))