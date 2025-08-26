import cv2
import numpy as np

def emptyFunction():
    pass

def main():
    img1 = np.zeros((512, 512, 3), np.uint8)
    windowName = 'OpenCV BGR Color Palette'
    cv2.namedWindow(windowName)

    cv2.createTrackbar('B', windowName, 0, 255, emptyFunction)
    cv2.createTrackbar('G', windowName, 0, 255, emptyFunction)
    cv2.createTrackbar('R', windowName, 0, 255, emptyFunction)

    while(True):
        # Get the current color values from the trackbars
        blue = cv2.getTrackbarPos('B', windowName)
        green = cv2.getTrackbarPos('G', windowName)
        red = cv2.getTrackbarPos('R', windowName)

        img1[:] = [blue, green, red]

        cv2.imshow(windowName, img1)

        intensity = (blue + green + red) / 3
        print("intensity = ", intensity)

        if (blue + green + red) == 0:
            saturation = 0
        else:
            saturation = 1 - 3 * np.min([blue, green, red]) / (blue + green + red)
        print("saaturation = ", saturation)

        if (red - green) == 0 or (red - blue) == 0:
            theta = 0
        else:
            theta = np.arccos(0.5 * ((red - green) + (red - blue)) / np.sqrt((red - green)**2 + (red - blue)*(green - blue)))
            
        if (blue <= green):
            print("theta =", np.degrees(theta))
        else:
            print("theta =", 360 - np.degrees(theta))

        if cv2.waitKey(1) == 27:  
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
