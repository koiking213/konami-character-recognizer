import cv2
from main import is_same_character

def test() -> None:
    rui = cv2.imread('images/rui.png')
    rui2 = cv2.imread('images/rui2.png')
    shiro = cv2.imread('images/shiro.png')
    robo = cv2.imread('images/robo.png')
    pink_girl = cv2.imread('images/pink_girl.png')
    assert(is_same_character(rui, rui2))
    assert(not is_same_character(rui, shiro))
    assert(not is_same_character(rui, robo))
    assert(not is_same_character(rui, pink_girl))