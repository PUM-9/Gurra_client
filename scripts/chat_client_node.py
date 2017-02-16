#!/usr/bin/env python


import rospy
from chat_server.msg import Message

def chat():
    pub = rospy.Publisher('chat_in', Message, queue_size=10)
    rospy.init_node('gurra_chat_pub')
    rate = rospy.Rate(10) #10 Hz
    while not rospy.is_shutdown() :
        message = str(input("..."))
        chat_str = message + ":" + rospy.get_time()
        pub.publish("Gurra", chat_str)
        rate.sleep()

def hey_listen():
    rospy.init_node('gurra_chat_sub', anonymous=True)
    rospy.Subscriber("chat_out", Message, callback)

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.message)

if __name__ == "__main__":
    try:
        chat()
    except rospy.ROSInterruptException:
        pass
