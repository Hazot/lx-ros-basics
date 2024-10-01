#!/usr/bin/env python3

import os
import json
import rospy
from sensor_msgs.msg import Joy
from duckietown_msgs.msg import WheelsCmdStamped


class DTJoystickDemoNode:
    def __init__(self):
        self.veh_name = os.environ.get("VEHICLE_NAME", "agent")
        self.sub_joy = rospy.Subscriber(f"/{self.veh_name}/joy", Joy, self.process_joy)
        self.pub_wheels_cmds = rospy.Publisher(
            f"/{self.veh_name}/wheels_driver_node/wheels_cmd", WheelsCmdStamped
        )

    def process_joy(self, msg):
        cmd_to_publish = WheelsCmdStamped()

        # header contains some meta information, good practice to copy it
        cmd_to_publish.header = msg.header

        # assign the velocity from the joystick to the wheels, no movement
        cmd_to_publish.vel_right = 0
        cmd_to_publish.vel_left = 0

        v = 0.5

        if msg.axes[1] == 1.0:
            # go forward
            cmd_to_publish.vel_right = v
            cmd_to_publish.vel_left = v

        if msg.axes[1] == -1.0:
            # go backward
            cmd_to_publish.vel_right = -v
            cmd_to_publish.vel_left = -v

        if msg.axes[3] == -1.0:
            # turn left
            cmd_to_publish.vel_right = -v
            cmd_to_publish.vel_left = v

        if msg.axes[3] == 1.0:
            # turn right
            cmd_to_publish.vel_right = v
            cmd_to_publish.vel_left = -v

        # publish the message
        self.pub_wheels_cmds.publish(cmd_to_publish)


if __name__ == "__main__":
    # Initialize the node
    node = DTJoystickDemoNode()
    rospy.init_node("dt-joystick-demo-node")

    # Keep it spinning
    rospy.spin()
