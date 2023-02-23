import base64
import json
import cv2
import numpy as np


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


def is_same_character(img_a: cv2.Mat, img_b: cv2.Mat) -> bool:
    hist_a = calc_hist(img_a)
    hist_b = calc_hist(img_b)
    similarity = compare_hist(hist_a, hist_b)
    return similarity > 0.5


def decode_image(img_base64: str) -> cv2.Mat:
    np_data = np.frombuffer(base64.b64decode(img_base64), np.uint8)
    return cv2.imdecode(np_data, cv2.IMREAD_UNCHANGED)


def is_same_character_base64(img_a_base64: str, img_b_base64: str) -> bool:
    img_a = decode_image(img_a_base64)
    img_b = decode_image(img_b_base64)
    return is_same_character(img_a, img_b)


def lambda_handler(event, context):
    print(event)
    body = json.loads(event['body'])
    target_character_base64 = body['target']
    images_base64 = body['images']
    same_image_indices = []
    for i, image_base64 in enumerate(images_base64):
        if is_same_character_base64(target_character_base64, image_base64):
            same_image_indices.append(i)
    return {
        'statusCode': 200,
        'body': same_image_indices
    }


if __name__ == "__main__":
    hist_a = calc_hist(cv2.imread("images/blue.png"))
    hist_b = calc_hist(cv2.imread("images/blue2.png"))
    print(compare_hist(hist_a, hist_b))
