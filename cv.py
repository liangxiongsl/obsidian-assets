import cv2,os

def compress(img_path):
    def run(q):
        img_path1 = os.path.splitext(img_path)[0] + '_compression.jpg'

        img = cv2.imread(img_path)
        cv2.imwrite(img_path1, img, [cv2.IMWRITE_JPEG_QUALITY, q])
        img_size = os.stat(img_path1).st_size / 1000 / 1000
        print(q, img_size)
        return img_size

    l, r = 0, 100
    while l < r:
        m = l + r >> 1
        if run(m) > 0.1:
            r = m - 1
        else:
            l = m + 1

compress('sd.png')