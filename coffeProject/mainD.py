import os
from cvzone.HandTrackingModule import HandDetector
import cv2
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
imgBackground = cv2.imread("Resources/Background.png")
while True:
    success, img = cap.read()
    imgBackground[139:139 + 480, 50:50 + 640] = img
    # cv2.imshow('İmage',img) bunu kaldırdık çünkü gerek kalmadı
    cv2.imshow('Background', imgBackground)
    cv2.waitKey(1)

# # importing all the mode images to a list
# folderPathModes = "Resources/Modes"
# listImgModesPath = os.listdir(folderPathModes)
# listImgModes = []
# for imgModePath in listImgModesPath:
#     listImgModes.append(cv2.imread(os.path.join(folderPathModes, imgModePath)))
# print(listImgModes)
# # importing all the icons to a list
# folderPathIcons = "Resources/Icons"
# listImgIconsPath = os.listdir(folderPathIcons)
# listImgIcons = []
# for imgIconsPath in listImgIconsPath:
#     listImgIcons.append(cv2.imread(os.path.join(folderPathIcons, imgIconsPath)))
# modeType = 0  # for changing selection mode
# selection = -1
# counter = 0
# selectionSpeed = 7
# detector = HandDetector(detectionCon=0.8, maxHands=1)
# modePositions = [(1136, 196), (1000, 384), (1136, 581)]
# counterPause = 0
# selectionList = [-1, -1, -1]