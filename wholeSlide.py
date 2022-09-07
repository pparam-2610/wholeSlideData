# The path can also be read from a config file, etc.
OPENSLIDE_PATH = r'C:\\Users\\ppara\\4thYearMP\\openslide-win64-20220811\\bin'

import os
if hasattr(os, 'add_dll_directory'):
    # Python >= 3.8 on Windows
    with os.add_dll_directory(OPENSLIDE_PATH):
        import openslide
else:
    import openslide



from wholeslidedata.image.wholeslideimage import WholeSlideImage
image = WholeSlideImage('testTiff_1.tiff')
patch = image.get_patch(100, 100, 256, 256, 0.5)
# image.get
print(image.level_count, image.get_slide(8))
print(patch.shape)

import cv2
# img = cv2.imread("third.tif", cv2.IMREAD_COLOR)
cv2.imshow("image", image.get_slide(8))
cv2.waitKey(0)
# patch = image.get_patch(x, y, width, height, spacing)