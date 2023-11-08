import cv2

class Process():
    def __init__(self, img):
        self.img = img
        # cv2.imshow("OpenCV/Numpy normal", img)
        # pass
        # print(img)
        # crop image by top left
        top = 190
        left = 70

        # crop image by bottom right
        right = img.shape[1] - 168
        bot = img.shape[0] - 120

        # crop image
        img = img[top:bot, left:right]
        
        #save
        cv2.imwrite("cropped.png", img)

        # divide by 10 x 17
        width = img.shape[1] // 17
        height = img.shape[0] // 10
        for x in range(1, 17):
            for y in range(1, 10):
                # crop image by top left
                top = (y - 1) * height
                left = (x - 1) * width

                # crop image by bottom right
                right = x * width
                bot = y * height

                # crop image
                apples = img[top:bot, left:right]

                #save
                cv2.imwrite("./apples/" + str(x) +'_'+ str(y) + ".png", apples)
        

if __name__ == "__main__":
    # read test.png
    img = cv2.imread("test.png")
    Process(img)