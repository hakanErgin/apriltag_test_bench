print("hs")
import rosbag
bag = rosbag.Bag("/home/uware/rosbags/2022-02-17-15-33-21.bag")
for topic, msg, t in bag.read_messages(topics=['tag_detections', 'tf']):
    print("topic-- ", topic)
    print("t-- ", t.to_sec())
    # print("message-- ", msg)
bag.close()