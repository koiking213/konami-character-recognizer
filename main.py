import cv2


def calc_hist(img: cv2.Mat) -> cv2.Mat:
    # 画像をRGBからHSVに変換
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, _s, _v = cv2.split(hsv)
    # 色相(H)のヒストグラムを計算
    hist = cv2.calcHist([h], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
    # 白を無視
    hist[0] = 0
    # ヒストグラムを正規化
    cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
    return hist


def compare_hist(hist1: cv2.Mat, hist2: cv2.Mat) -> float:
    similarity: float = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    return similarity


img_a = cv2.imread("a.png")
hist_a = calc_hist(img_a)


for image in ["b.png", "c.png", "d.png", "e.png", "f.png", "g.png"]:
    print(image)
    img_b = cv2.imread(image)
    hist_b = calc_hist(img_b)
    # print(hist_b)

    similarity = compare_hist(hist_a, hist_b)
    # print("Similarity: ", similarity)
