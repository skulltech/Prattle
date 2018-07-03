import cv2 as cv


def display():
    cap = cv.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv.imshow('Live Web-Cam Feed', frame)

        key = cv.waitKey(1)
        if key in [27, 81, 113]:
            break

    cap.release()
    cv.destroyAllWindows()


if __name__=='__main__':
	display()
