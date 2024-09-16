from art_robot.art_robot import draw_head, draw_ears, draw_mouth
from art_robot.init_task import init_task
import pyautogui

def test_art_robot():
    (app, config) = init_task()
    assert(app != None) 
    assert('canvas' in config)
    canvas = config["canvas"]
    test_head_radius = 100
    draw_head(app, canvas, test_head_radius)
    test_ear_radius = 70
    draw_ears(app, canvas, test_head_radius, test_ear_radius)
    identified_heads = len(list( pyautogui.locateAllOnScreen('test_head.png', confidence=0.98) ))
    assert(identified_heads == 1)
    test_mouth_radius = 60
    draw_mouth(app, canvas, test_mouth_radius)
    identified_mouths = len(list( pyautogui.locateAllOnScreen('test_mouth.png', confidence=0.98) ))
    assert(identified_mouths == 1)