#!/usr/bin/env python
import rospy
import angus
from sensor_msgs.msg import Image
from pprint import pprint


conn = angus.connect()
service = conn.services.get_service("scene_analysis", version=1)
service.enable_session()

def callback(data):
    job = service.process({"image": open("/home/ros/test.jpg", 'rb'),
                           "timestamp" : "2016-10-26T16:21:01.136287+00:00",
                           "camera_position": "ceiling",
                           "sensitivity": {
                                        "appearance": 0.7,
                                        "disappearance": 0.7,
                                        "age_estimated": 0.4,
                                        "gender_estimated": 0.5,
                                        "focus_locked": 0.9,
                                        "emotion_detected": 0.4,
                                        "direction_estimated" : 0.8
                                      }
                      })
    pprint(job.result)

def scene_analysis():
    rospy.init_node('scene_analysis', anonymous=False)
    rospy.Subscriber("image", Image, callback)
    rospy.spin()

if __name__ == '__main__':
    scene_analysis()
    service.disable_session()


