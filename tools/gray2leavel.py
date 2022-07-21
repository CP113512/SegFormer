import cv2
from pathlib import Path

gray_root = Path(r'show_dir')
real_root = Path(r'E:\data\ricedata_v3.0\cp\SegmentationClass')
gray_list = [path for path in gray_root.iterdir()]
whichnum = [0,0]
# leavelnum= [0,0,0,0,0,0]
class_name = dict(class_bs = {'sum': 0, 'leavelnum': [0,0,0,0,0,0]},
                  class_b = {'sum': 0, 'leavelnum': [0,0,0,0,0,0]},
                  class_bb = {'sum': 0, 'leavelnum': [0,0,0,0,0,0]}
)
real_class_name = dict(class_bs = {'sum': 0, 'leavelnum': [0,0,0,0,0,0]},
                  class_b = {'sum': 0, 'leavelnum': [0,0,0,0,0,0]},
                  class_bb = {'sum': 0, 'leavelnum': [0,0,0,0,0,0]}
)
metric_list = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
class_metric_list = dict(
    class_bs = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
],
    class_bb = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
],
    class_b = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]
)

def get_info(img_path):
    class_num = {'class_bs': 0, 'class_b': 0, 'class_bb': 0}
    image = cv2.imread(str(img_path), 0)
    height = image.shape[0]
    width = image.shape[1]
    k = 0
    m = 0

    # {'background': 0, 'leaf': 1, 'brownspot': 2, 'blast': 3, 'bacterialblight': 4, 'tungro': 5, 'Healthy': 6}
    # 计算各颜色像素面积
    for i in range(height):
        for j in range(width):
            if (image[i, j] == 0):
                continue
            elif (image[i, j] == 1 or image[i, j] == 106):
                m = m + 1
            elif (image[i, j] == 2 or image[i, j] == 76):
                k = k + 1
                class_num['class_bs'] += 1
            elif (image[i, j] == 3 or image[i, j] == 179):
                k = k + 1
                class_num['class_b'] += 1
            elif (image[i, j] == 4 or image[i, j] == 149):
                k = k + 1
                class_num['class_bb'] += 1
    tmp = zip(class_num.values(), class_num.keys())
    # real_tmp = zip(class_num.values(), class_num.keys())

    final_class = max(tmp)
    # real_final_class = max(tmp)
    # class_name[final_class[1]]['sum'] += 1

    n = 0
    a = 0
    b = 0
    # 按面积比例划分病变等级
    if (k == 0):
        a = 0
    elif (k / (m + k) <= 0.1):
        a = 1
    elif (k / (m + k) > 0.1 and k / (m + k) <= 0.25):
        a = 2
    elif (k / (m + k) > 0.25 and k / (m + k) <= 0.45):
        a = 3
    elif (k / (m + k) > 0.45 and k / (m + k) <= 0.65):
        a = 4
    elif (k / (m + k) > 0.65):
        a = 5
    else:
        pass
    # image = cv2.imread(str(path_mask), 0)

    h = image.shape[0]
    w = image.shape[1]
    for i in range(h):
        for j in range(w):
            if (image[i, j] == 1):
                image[i, j] = 0
            elif (image[i, j] != 0):
                image[i, j] = 225
    # 轮廓发现

    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(contours, hierarchy)
    # 在图片上显示信息 并画框
    dn = len(contours[0])
    if dn >= 1 and dn <= 5:
        b = 1
    elif dn > 5 and dn <= 10:
        b = 2
    elif dn > 10 and dn <= 15:
        b = 3
    elif dn > 15 and dn <= 20:
        b = 4
    elif dn > 20:
        b = 5
    else:
        b = 0
    c = 0
    if (a >= b):
        c = a
        whichnum[0] += 1
    else:
        c = b
        whichnum[1] += 1
    print(a, b, c, k, m, dn)
    # class_name[final_class[1]]['leavelnum'][c] += 1
    return final_class, c

def main():
    class_num = {'class_bs': 0, 'class_b': 0, 'class_bb': 0}
    rclass_num = {'class_bs': 0, 'class_b': 0, 'class_bb': 0}
    for i, name in enumerate(gray_list):
        real_name = real_root / ('DSC_0306_1' + '.png')
        class_num = {'class_bs': 0, 'class_b': 0, 'class_bb': 0}
        rclass_num = {'class_bs': 0, 'class_b': 0, 'class_bb': 0}
        print(name, '{} / {}'.format(i, len(gray_list)))


        # class_name[final_class[1]]['leavelnum'][c] += 1


        # image = cv2.imread(str(path_mask), 0)


        # if rfinal_class[1] != final_class[1] or abs(rc - c) > 1:
        #     print('出错了')
        # class_metric_list[final_class[1]][rc][c] += 1

        # print('真实：', rfinal_class, rc, '\n预测：', final_class, c)
    print(class_metric_list)
    print(class_name)


if __name__ == '__main__':
    root_path = Path(r'E:\data\ricedata_v3.0\BrownSpot_150_3\SegmentationClass\DSC_0306_1.png')
    final, leavel = get_info(root_path)
    print(final, leavel)
