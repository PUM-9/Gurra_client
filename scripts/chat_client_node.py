#!/usr/bin/env python

import rospy
from chat_server.msg import Message

def chat():
    pub = rospy.Publisher('chat_in', Message, queue_size=10)
    rospy.init_node('gurra_chat_pub')
    rate = rospy.Rate(10) #10 Hz
    while not rospy.is_shutdown() :
        message = raw_input(": ")
        #message = "test"
        chat_str = message + ":" + str(rospy.get_time())
        pub.publish(sender="Gurra",message= chat_str)
        rate.sleep()

def hey_listen():
    rospy.init_node('gurra_chat_sub', anonymous=True)
    rospy.Subscriber("chat_out", Message, callback)
    rospy.spin()

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.sender + data.message)

if __name__ == "__main__":
    try:
        hey_listen()
    except rospy.ROSInterruptException:
        pass
