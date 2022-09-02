import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys

bridge = Cybridge() //constructor

def image_callback(ros_image):
	print(“Got an image”)
	global bridge

try:
	cv_image = bridge.imgmsg_to_cv2(ros_image, “bgr8”)
except CvBridgeError as e:
	print(e)
(rows, cols, channels)=cv_image.shape

def main(args):
	rospy.init_node(‘image_converter’, anonymous=True)
	image_sub=rospy.Subscriber(“/usb_cam/image_raw”,Image, image_callback)
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print(“Shutting down”)
