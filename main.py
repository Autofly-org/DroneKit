from dronekit import connect
import time
# diffrent modes:
    # 5: Loiter
    # 6: RTL
    # 7: Circle
    # 9: Land
# Connect to the Vehicle (in this case a UDP endpoint)
vehicle = connect('/dev/ttyUSB0', wait_ready=True, baud=57600)

#call for vehicle mode
@vehicle.on_attribute('mode')
def mode_callback(self,attr,msg):
    print("Mode Callback: ",msg)

@vehicle.on_attribute('battery')
def mode_callback(self,attr,msg):
    print("Battery Callback: ",msg)

try:
    while True:
        # vehicle.mode
        # getting system status
        # action = input("1:Change Mode \n 2:Incomming")
        # if(int(action) == 1):
        #     action = input("change Mode to: \n 0: stabilize 5: Loiter")
        #     vehicle.mode = int(action)
         
        # print("System: ".format(vehicle.system_status))
        
        # # getting mode
        # print("Mode: {0}".format(vehicle.mode.name))

        # # getting the attitude
        # print("vehicle attitude: {0}".format(vehicle.attitude)) 

        # getting the battery
        print("home location: {0}".format(vehicle.location.local_frame))
        vehicle.
        
       # print("hello".format(vehicle._voltage))

       # vehicle.add_attribute_listener('mode',mode_callback)
     
        time.sleep(4)
except KeyboardInterrupt:
    print("exited the program")
    vehicle.close()