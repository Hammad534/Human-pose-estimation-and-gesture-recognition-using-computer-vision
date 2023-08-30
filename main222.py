import cv2
import time
import subprocess

cap = cv2.VideoCapture(0)

pTime = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (50, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    cv2.putText(img, str('choose one option'), (20, 300), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                (255, 0, 0), 1)

    cv2.putText(img, str('Press 1 for pose estimation'), (20, 350), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                (255, 0, 0), 1)
    cv2.putText(img, str('press 2 for finger counting'), (20, 400), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                (255, 0, 0), 1)
    cv2.putText(img, str('press 3 for volume up & down'), (20, 450), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                (255, 0, 0), 1)

    cv2.imshow("Image", img)
    k = cv2.waitKey(1)
    # stop the webcam when we press esc
    if k == 27:
        break
    if k == 49:
        cmd = 'python poseestimation.py'
        p = subprocess.Popen(cmd, shell=True)
        out, err = p.communicate()
    if k == 50:
        cmd = 'python fingercounter.py'
        p = subprocess.Popen(cmd, shell=True)
        out, err = p.communicate()
    if k == 51:
        cmd = 'python volumeupdown.py'
        p = subprocess.Popen(cmd, shell=True)
        out, err = p.communicate()


########
  #  if k == 50:
   #     subprocess.call(['python', 'finger counter.py'])
    #if k == 51:
     #   subprocess.call(['python', 'volume up down.py'])
########