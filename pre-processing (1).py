import os
import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt


# Function to rename multiple files


def main():
    path = "E:/New folder (2)/new"
    i = 0
    for filename in glob.glob(path + '/*.JPG'):
        image = cv2.imread(filename)
        height = image.shape[0]
        width = image.shape[1]
        # Cut the image in half
        width_cutoff = width // 2
        image_crop_1 = image[:, :width_cutoff]
        image_crop_2 = image[:, width_cutoff:]
        imgs = [image_crop_1, image_crop_2]
        print("I value is", i)
        for n, img in enumerate(imgs):
            print(n)
            fltr = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            # Applying cv2.filter2D function on our Logo image
            img_edge_enhancement = cv2.filter2D(img, -1, fltr)

            # blur images

            new_blur_img = cv2.medianBlur(img_edge_enhancement, 5)

            my_dest = str(n) + '_' + str(i) + '_' + "_sample_" + ".jpg"
            # print(new_blur_img)
            plt.imshow(new_blur_img)
            plt.show()
            os.chdir(r"E:/New folder (2)/new/save/")
            cv2.imwrite(my_dest, new_blur_img)
            i = i + 1


if __name__ == '__main__':
    # Calling main() function
    main()
