import cv2,os,shutil

def compress_jpeg(img_path):
    suf = os.path.splitext(img_path)[-1]
    assert suf in ['.jpg', '.jpeg']

    def run(q, src, dest):
        img = cv2.imread(src)
        cv2.imwrite(dest, img, [cv2.IMWRITE_JPEG_QUALITY, q])

        img_size = os.stat(dest).st_size / 1000 / 1000
        print(q, img_size)
        return img_size

    tmp_img_path = os.path.splitext(img_path)[0] + f'_tmp{suf}'
    # run(100, img_path, tmp_img_path)
    shutil.copy(img_path, tmp_img_path)

    l, r = 0, 100
    while l < r:
        m = l + r >> 1
        if run(m, tmp_img_path, img_path) > 0.1:
            r = m - 1
        else:
            l = m + 1

    os.remove(tmp_img_path)

def compress_png(img_path):
    suf = os.path.splitext(img_path)[-1]
    assert suf == '.png'

    def run(q, src, dest):
        img = cv2.imread(src)
        cv2.imwrite(dest, img, [cv2.IMWRITE_PNG_COMPRESSION, q])

        img_size = os.stat(dest).st_size / 1000 / 1000
        print(q, img_size)
        return img_size

    tmp_img_path = os.path.splitext(img_path)[0] + f'_tmp{suf}'
    # run(0, img_path, tmp_img_path)
    shutil.copy(img_path, tmp_img_path)

    l, r = 0, 9
    while l < r:
        m = l + r >> 1
        if run(m, tmp_img_path, img_path) < 0.1:
            r = m - 1
        else:
            l = m + 1

    os.remove(tmp_img_path)

