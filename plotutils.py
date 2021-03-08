from matplotlib import pyplot as plt
import cv2 as cv


def cv_show(name, array, shape):
    max_size = 1000
    length = shape[0]
    width = shape[1]

    if length > max_size or width > max_size:
        if length > width:
            temp = length
            length = max_size
            width = int(width * length / temp)
        elif width > length:
            temp = width
            width = max_size
            length = int(length * width / temp)
        else:
            length = max_size
            width = max_size
    thumbnail = cv.resize(array, (length, width), interpolation=cv.INTER_AREA)

    cv.imshow(name, thumbnail)
    cv.waitKey(0)
    cv.destroyAllWindows()

def plt_show(name, array, fsize):
    plt.figure(figsize=(fsize, fsize))
    plt.imshow(cv.cvtColor(array, cv.COLOR_BGR2RGB))
    plt.title(name)
    plt.show()
    
def show(name, array, fsize, shape):
    cv_show(name, array, shape)
    plt_show(name, array, fsize)
