import base64
import json
import cv2
from app import is_same_character, is_same_character_base64


def test() -> None:
    rui = cv2.imread("images/rui.png")
    rui2 = cv2.imread("images/rui2.png")
    shiro = cv2.imread("images/shiro.png")
    robo = cv2.imread("images/robo.png")
    pink_girl = cv2.imread("images/pink_girl.png")
    assert is_same_character(rui, rui2)
    assert not is_same_character(rui, shiro)
    assert not is_same_character(rui, robo)
    assert not is_same_character(rui, pink_girl)


def test_base64() -> None:
    with open("images/rui.png", "rb") as f:
        rui_base64 = base64.b64encode(f.read()).decode()
    with open("images/rui2.png", "rb") as f:
        rui2_base64 = base64.b64encode(f.read()).decode()
    with open("images/shiro.png", "rb") as f:
        shiro_base64 = base64.b64encode(f.read()).decode()
    assert is_same_character_base64(rui_base64, rui2_base64)
    assert not is_same_character_base64(rui_base64, shiro_base64)
