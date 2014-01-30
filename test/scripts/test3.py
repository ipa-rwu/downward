#! /usr/bin/env python

import rospy
import actionlib
import sys

import downward_msgs.msg

def planner_client(dataD,dataP):

    client = actionlib.SimpleActionClient('planner', downward_msgs.msg.downAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = downward_msgs.msg.downGoal(dataP,dataD)

    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('planner_client')

	if len(sys.argv) == 3:
		x = sys.argv[1]
		y = sys.argv[2]
	else:
		sys.exit(1)


	with open (x, "r") as myfile:
		dataD=myfile.read()
	with open (y, "r") as myfile:
		dataP=myfile.read()
        result = planner_client(dataD,dataP)
        print( result)
    except rospy.ROSInterruptException:
        print "program interrupted before completion"
