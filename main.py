from tkinter import *
import subprocess

root = Tk()
root.title("Human Pose Estimation And Gesture Recognition")
root.geometry('400x400')
root.configure(background='blue')


def pose():
    cmd = 'python poseestimation.py'
    p = subprocess.Popen(cmd, shell=True)
    out, err = p.communicate()


def finger():
    cmd = 'python fingercounter.py'
    p = subprocess.Popen(cmd, shell=True)
    out, err = p.communicate()


def volume():
    cmd = 'python volumeupdown.py'
    p = subprocess.Popen(cmd, shell=True)
    out, err = p.communicate()


lab1 = Label(root, text="Pose Estimation and Gesture Recognition").grid(row=0, column=0, padx=10, pady=10)
btn1 = Button(root, text="Pose Estimation", font='Times 20 bold', command=pose)
btn1.grid(row=1, column=0, padx=30, pady=30)
btn2 = Button(root, text="Finger Counting", font='Times 20 bold', command=finger)
btn2.grid(row=2, column=0,  padx=30, pady=30)
btn3 = Button(root, text="Gesture Volume Up & Down", font='Times 20 bold', command=volume)
btn3.grid(row=3, column=0,  padx=30, pady=30)

root.mainloop()
