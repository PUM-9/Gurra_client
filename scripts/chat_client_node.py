#!/usr/bin/env python

import rospy
from chat_server.msg import Message

name = ""


def chat():
    global name
    name = raw_input("What be your name milord?")
    pub = init()
    rate = rospy.Rate(10) #10 Hz
    while not rospy.is_shutdown():
        chat_str = raw_input(": ")
        message = macros(chat_str)
        pub.publish(sender=name,message= message)
        rate.sleep()

def callback(data):
    global name
    if data.sender != name:
        print('\n' + data.sender + " : " + data.message)

def init():
    pub = rospy.Publisher('chat_in', Message, queue_size=10)
    rospy.init_node('gurra_chat_sub', anonymous=True)
    rospy.Subscriber("chat_out", Message, callback)
    return pub

def macros(text):
    global name
    if text[0] == "/":
        if text[:5] == "/name":
            name = text[5:]
            return ""
        else :
            return text
    else:
        return text


if __name__ == "__main__":
    try:
        chat()
    except rospy.ROSInterruptException:
        pass
