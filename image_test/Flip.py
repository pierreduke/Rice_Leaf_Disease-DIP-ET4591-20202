import cv2
import glob

list_rice1 = glob.glob("F:/20k_img/rice_leaf_disease/Bacterialleafblight/*.*")
count1 =80
for path1 in list_rice1:
    count1+=1
    image1 = cv2.imread(path1)
    flip1 = cv2.flip(image1, -1)
    cv2.imwrite("F:/Rot_Img/Bacterial leaf blight/"+"Bacterial"+str(count1)+".jpg", flip1)
list_rice2 = glob.glob("F:/20k_img/rice_leaf_disease/Brownspot/*.*")
count2 =80
for path2 in list_rice2:
    count2+=1
    image2 = cv2.imread(path2)
    flip2 = cv2.flip(image2, -1)
    cv2.imwrite("F:/Rot_Img/Brown spot/"+"Brown"+str(count2)+".jpg", flip2)
list_rice3 = glob.glob("F:/20k_img/rice_leaf_disease/Leafsmut/*.*")
count3 =80
for path3 in list_rice3:
    count3+=1
    image3 = cv2.imread(path3)
    flip3 = cv2.flip(image3, -1)
    cv2.imwrite("F:/Rot_Img/Leaf smut/"+"Smut"+str(count3)+".jpg", flip3)