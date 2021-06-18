from keras_preprocessing.image import ImageDataGenerator, img_to_array, array_to_img, load_img
import glob
import cv2
import matplotlib.pyplot as plt
datagen = ImageDataGenerator(
                             brightness_range=[0.2, 1.5],
                             width_shift_range=0.2,
                             height_shift_range=0.2,
                             shear_range=30,
                             fill_mode='nearest',
                             )
list_img = glob.glob("F:/Rot_Img/test/Bacterial leaf blight/*.*")
for path in list_img:
    img = plt.imread(path)
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)
    count = 1
    for batch in datagen.flow(x, batch_size=1, save_to_dir='F:/Rot_Img/test2/Bacterial leaf blight', save_prefix='rice', save_format='jpg'):
        count += 1
        if count > 5:
             break
list_img = glob.glob("F:/Rot_Img/test/Brown spot/*.*")
for path in list_img:
    img = plt.imread(path)
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)
    count = 1
    for batch in datagen.flow(x, batch_size=1, save_to_dir='F:/Rot_Img/test2/Brown spot', save_prefix='rice', save_format='jpg'):
        count += 1
        if count > 5:
             break
list_img = glob.glob("F:/Rot_Img/test/Leaf smut/*.*")
for path in list_img:
    img = plt.imread(path)
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)
    count = 1
    for batch in datagen.flow(x, batch_size=1, save_to_dir='F:/Rot_Img/test2/Leaf smut', save_prefix='rice', save_format='jpg'):
        count += 1
        if count > 5:
             break