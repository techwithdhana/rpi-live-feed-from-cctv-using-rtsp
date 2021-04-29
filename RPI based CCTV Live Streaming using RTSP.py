# import depententies
import cv2
import cvui

# enter DVR username & password
rtsp_username = "enter_username"
rtsp_password = "enter_password"
width = 800
height = 480
cam_no = 1

# camera init
def create_camera (channel):
    rtsp = "rtsp://" + rtsp_username + ":" + rtsp_password + "@192.168.11.110:554/Streaming/channels/" + channel + "02" #change the IP to suit yours
    cap = cv2.VideoCapture()
    cap.open(rtsp)
    cap.set(3, 640)  # ID number for width is 3
    cap.set(4, 480)  # ID number for height is 480
    cap.set(10, 100)  # ID number for brightness is 10qq
    return cap
cam = create_camera(str(cam_no))
cvui.init('screen')
while True:
    success, current_cam = cam.read()
    dim = (width, height)
    Full_frame = cv2.resize(current_cam, dim, interpolation=cv2.INTER_AREA)
    cv2.namedWindow('screen', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('screen', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # next button parameters
    if (cvui.button(Full_frame, width - 100, height - 40, "Next") and cvui.mouse(cvui.CLICK)):
        print("Next Button Pressed")
        cvui.init('screen')
        cam_no = cam_no+1
        if (cam_no>4):
            cam_no=1
        del cam
        cam = create_camera(str(cam_no))

    # previous button parameters
    if (cvui.button(Full_frame, width - 200, height - 40, "Previous") and cvui.mouse(cvui.CLICK)):
        print("Previous Button Pressed")
        cvui.init('screen')
        cam_no = cam_no - 1
        if (cam_no<1):
            cam_no=4
        del cam
        cam = create_camera(str(cam_no))

    # display the video
    cv2.imshow('screen', Full_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
