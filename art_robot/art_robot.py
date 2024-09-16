"""Functionality for the art robot."""

import math
import pyautogui
from pywinauto.application import Application
from art_robot.helper_functions import get_ear_coordinates
from art_robot.draw_body_part import draw_body_part

def draw_head(app: Application, canvas: dict, head_radius: int) -> None:
    """Draw the head with white so that its centre is at the middle point of the canvas."""
    head_width = 2*head_radius
    head_height = 2*head_radius

    # Calculate the top-left coordinates of the head
    canvas_middle = canvas['mid_point']
    head_top_left_x = canvas_middle[0] - head_radius
    head_top_left_y = canvas_middle[1] - head_radius
    head_coordinates = (head_top_left_x, head_top_left_y)
    
    # Set the head dimensions
    head_width = 2 * head_radius
    head_height = 2 * head_radius
    
    # Draw the head using draw_body_part
    draw_body_part(app, canvas, head_width, head_height, "white", head_coordinates)

def draw_ears(app: Application, canvas: dict, head_radius: int, ear_radius: int) -> None:
    """Draw two black ears with radius ear_radius to the head."""
    ear_coordinates = get_ear_coordinates(canvas['mid_point'], head_radius, ear_radius)
    ear_width = 2*ear_radius
    ear_height = 2*ear_radius
    
    # Draw the left ear
    draw_body_part(app, canvas, ear_width, ear_height, "black", ear_coordinates['left'])
    
    # Draw the right ear
    draw_body_part(app, canvas, ear_width, ear_height, "black", ear_coordinates['right'])

def draw_nose(app: Application, canvas: dict, nose_width: int, nose_height: int) -> None:
    """Draw the nose to the middle of the head."""
    canvas_middle = canvas["mid_point"]
    nose_coordinates = (canvas_middle[0] - 0.5*nose_width, canvas_middle[1] - 0.5*nose_height)
    draw_body_part(app, canvas, nose_width, nose_height, 'black', nose_coordinates)

def draw_eyes(app: Application, canvas: dict, eye_width: int, eye_height: int, nose_height: int) -> None:
    """Draw two eyes to the head with width eye_width and height eye_height."""
    canvas_middle = canvas["mid_point"]

    # Eye coordinates can be fine tuned if needed
    left_eye_coordinates = (canvas_middle[0] - 1.25*eye_width, canvas_middle[1] - (eye_height + 0.75*nose_height))
    right_eye_coordinates = (canvas_middle[0] + 0.25*eye_width, canvas_middle[1] - (eye_height + 0.75*nose_height))

    # Draw the left eye
    draw_body_part(app, canvas, eye_width, eye_height, 'black', left_eye_coordinates)
    # Draw the right eye
    draw_body_part(app, canvas, eye_width, eye_height, 'black', right_eye_coordinates)

def draw_mouth(app: Application, canvas: dict, mouth_radius: int) -> None:
    """Draw a lower circumference of a circle with mouth_radius as a smiling mouth to the head."""
    # Select Pencil from Tools
    brush_button = (
        app.top_window()
        .child_window(title="Brushes", control_type="Group")
        .child_window(title="Brushes", control_type="RadioButton")
        .wait("visible", timeout=5)
    )
    brush_button.click()

    # Move to the starting point (rightmost point of the circle)
    center_x = canvas['mid_point'][0]
    center_y = canvas['mid_point'][1]
   
    num_points = 75  # Number of points to draw for smooth curve

    # Move to the starting point (rightmost point of the circle)
    pyautogui.moveTo(center_x + mouth_radius, center_y)
    
    # Press the left mouse button
    pyautogui.mouseDown()
     
    # Draw a half circle to the head below the nose with pyautogui
    for i in range(num_points + 1):
        angle = math.pi * i / num_points  # Angle goes from 0 to pi (lower half)
        x = center_x + mouth_radius * math.cos(angle)
        y = center_y + mouth_radius * math.sin(angle)
        pyautogui.dragTo(x, y)
        pyautogui.sleep(0.01)  # Small delay to slow down the drawing
    
    # Release the mouse button
    pyautogui.mouseUp()

def draw_face(app: Application, canvas: dict, nose_width: int, nose_height: int, eye_width: int, eye_height: int, mouth_radius: int) -> None:
    """Draw a face with a nose, two eyes and a mouth to the head."""
    draw_nose(app, canvas, nose_width, nose_height)
    draw_eyes(app, canvas, eye_width, eye_height, nose_height)
    draw_mouth(app, canvas, mouth_radius)