#!/usr/bin/python3
import rospy
import tf2_msgs.msg
import tf
import numpy as np

def callback(data):

    rotation_quat = data.transforms[0].transform.rotation
    pitch, yaw, roll = tf.transformations.euler_from_quaternion([rotation_quat.x,rotation_quat.y,rotation_quat.z,rotation_quat.w], axes='rxyz')
    rotation_euler = (np.degrees(pitch), np.degrees(yaw), np.degrees(roll))

    translation = data.transforms[0].transform.translation

    # rospy.loginfo(rospy.get_caller_id())
    rospy.loginfo(translation)
    rospy.loginfo(rotation_euler)
    

def listener():
    rospy.init_node('quat_to_euler')
    rospy.Subscriber("/tf", tf2_msgs.msg.TFMessage, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()