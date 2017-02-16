#!/usr/bin/env python

import rospy
from chat_server.msg import Message

def chat():
    pub = init()
    rate = rospy.Rate(10) #10 Hz
    while not rospy.is_shutdown():
        chat_str = raw_input(": ")
        pub.publish(sender="Gurra",message= chat_str)
        rate.sleep()

def callback(data):
    if data.sender is not "Gurra":
        print('\n' + data.sender + " : " + data.message)

def init():
    pub = rospy.Publisher('chat_in', Message, queue_size=10)
    rospy.init_node('gurra_chat_sub', anonymous=True)
    rospy.Subscriber("chat_out", Message, callback)
    return pub

if __name__ == "__main__":
    try:
        chat()
    except rospy.ROSInterruptException:
        pass
