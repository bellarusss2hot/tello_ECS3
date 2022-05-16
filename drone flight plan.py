from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()
print(drone.get_battery())
drone.takeoff()
# drone will move up 130 cm from the additional 80 cm giving a total of 210 cm high
drone.move_up(130)
# drone will sleep for 0.5 after every action besides lift off
sleep(.5)
# drone will move 500 cm forward to cross the halfway point of the room
drone.move_forward(500)
# drone will rotate 90 degrees to adjust for the next action
drone.rotate_counter_clockwise(90)
# drone will move forward 310 cm in order to cross the halfway point of the room
drone.move_forward(310)
# drone will rotate another 90 degrees in order to adjust for its next movement
drone.rotate_counter_clockwise(90)
# drone will move 500 cm forward for the return path
drone.move_forward(500)
# drone will rotate 90 degrees for the final movement path
drone.rotate_counter_clockwise(90)
# drone will move forward 310 to come back to the starting position
drone.move_forward(310)
# drone will land and complete the route
drone.land()
