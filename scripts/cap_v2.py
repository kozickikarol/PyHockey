import cv2
import numpy as np

camWindow = 'cam'
helpWindow = 'help'

cap = cv2.VideoCapture(0)
cv2.namedWindow(camWindow, cv2.CV_WINDOW_AUTOSIZE)
cv2.namedWindow(helpWindow)
light = None

term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)


def getFrame(cap):
    _, frame = cap.read()
    return cv2.resize(cv2.flip(frame, 1), (800, 600))


def findPlayers(cap):
    """
    Finds players on the cam

    :rtype : tuple of Circles (x, y, radius)
    :param cap: cv2.VideoCapture
    :param draw: Bool whether to draw frames in the procces
    :param windowsNames: tuple of window names
    """

    initMinDist = 40
    fgbg = cv2.BackgroundSubtractorMOG()
    while True:
        minDist = initMinDist
        frame = getFrame(cap)

        # if light == None:
        #     light = findLight(frame)

        frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame2 = cv2.GaussianBlur(frame2, (0, 0), 2.0, cv2.CV_8U)
        _, thr = cv2.threshold(frame2, 235, 255, cv2.THRESH_BINARY)
        fgmask = fgbg.apply(thr)
        thr = thr & fgmask

        thr = cv2.GaussianBlur(thr, (0, 0), 10.0, cv2.CV_8U)

        _, thr = cv2.threshold(thr, 70, 255, cv2.THRESH_BINARY)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

        circles = cv2.HoughCircles(thr, cv2.cv.CV_HOUGH_GRADIENT, 1, minDist,
                                   param1=30,
                                   param2=15,
                                   minRadius=30,
                                   maxRadius=0)

        if circles is not None:
            circles = circles[0]

            circles[circles[:, 2].argsort()]

            thr = cv2.cvtColor(thr, cv2.COLOR_GRAY2RGB)

            for circle in circles[0:2, :]:
                # cv2.circle(frame, (circle[0], circle[1]), circle[2], [255, 0, 0], 5)
                cv2.circle(thr, (circle[0], circle[1]), circle[2], [255, 0, 0], 5)

            print circles[0:2, :]
            print

            if circles[0:2, :].shape[0] == 2:
                cv2.imshow(helpWindow, thr)
                return circles[0:2, :], frame

        else:
            minDist = initMinDist

        cv2.imshow(camWindow, frame)
        cv2.imshow(helpWindow, thr)


# circles = findPlayers(cap)

def findPlayers2(cap):
    while True:
        frame = getFrame(cap)

        # draw two circles for players
        r = 30

        x = 200
        y = 200

        z1 = (x, y)
        z2 = (x + 200, y)

        cv2.circle(frame, z1, r, [255, 0, 0], 5)
        cv2.circle(frame, z2, r, [0, 255, 0], 5)

        key = cv2.waitKey(10) & 0xFF

        if key == ord('q'):
            break
        if key == ord('o'):
            return [(z1 + (r,)), (z2 + (r,))], getFrame(cap)

        cv2.imshow(camWindow, frame)




def parsePlayers(circles, frame):
    players = []

    i = 0
    for c in circles:
        square = (int(c[0] - c[2]), int(c[1] - c[2]), int(2 * c[2]), int(2 * c[2]))
        roi = frame[square[0]:square[0] + square[2], square[1]:square[1] + square[3], :]
        hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        color = [0, 0, 0]
        color[i] = 255
        i += 1
        players.append([
            square,
            cv2.calcHist([hsv_roi], [0], None, [180], [0, 180]),
            color
        ])

    # print players[:, 0]
    return players


res = findPlayers2(cap)

if res is not None:
    print 'Found players!'
    circles, frame = res
    players = parsePlayers(circles, frame)

    while True:
        frame = getFrame(cap)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        for p in players:
        # p = players[0]
            print p[0]

            if p[0].count(0) != len(p[0]):
                dst = cv2.calcBackProject([hsv], [0], p[1], [0, 180], 1)
                r, p[0] = cv2.meanShift(dst, p[0], term_crit)
                x, y, w, h = p[0]
                cv2.rectangle(frame, (x, y), (x + w, y + h), p[2], 2)
                # pts = np.int0(cv2.cv.BoxPoints(r))
                # cv2.polylines(frame, [pts], True, p[2], 2)
            else:
                x, y, w, h = p[0]
                cv2.rectangle(frame, (x, y), (x + w, y + h), p[2], 2)
                #
                #pts = cv2.cv.BoxPoints(p[0])
                # points = np.int32([[910, 641], [206, 632], [696, 488], [458, 485]])
                # cv2.polylines(frame, points, True, (255,255,255))
                # cv2.polylines(frame, np.int32(pts), True, p[2], 2)

        # for circle in circles[0:2, :]:
        #     # cv2.circle(frame, (circle[0], circle[1]), circle[2], [255, 0, 0], 5)
        #     cv2.circle(frame, (circle[0], circle[1]), circle[2], [255, 0, 0], 5)

        cv2.imshow(camWindow, frame)
        key = cv2.waitKey(10) & 0xFF

        if key == ord('q'):
            break
        if key == ord('r'):
            res = findPlayers2(cap)
            if res is None:
                break
            circles, frame = res
            players = parsePlayers(circles, frame)

        if key == ord('f'):
            res = findPlayers(cap)
            if res is None:
                break
            circles, frame = res
            players = parsePlayers(circles, frame)



            # while not (cv2.waitKey(10) & 0xFF == ord('q')):
            #     pass

cap.release()
cv2.destroyAllWindows()
