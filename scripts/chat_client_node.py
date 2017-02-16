#!/usr/bin/env python

import rospy
from chat_server.msg import Message

def chat():
    pub = init()
    #rospy.init_node('gurra_chat_pub')
    rate = rospy.Rate(10) #10 Hz
    while not rospy.is_shutdown() :
        message = raw_input(": ")
        #message = "test"
        chat_str = message + ":" #+ str(rospy.get_time())
        pub.publish(sender="Gurra",message= chat_str)
        rate.sleep()

def callback(data):
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
