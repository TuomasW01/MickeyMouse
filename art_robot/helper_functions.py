"""Helper functions for the ART robot."""
from math import sqrt
from pywinauto.application import Application

def get_canvas_information(app: Application) -> dict:
    """Return the borders and middle point of the canvas."""    
    canvas_field = (
        app.top_window()
        .child_window(title="Using Brush tool on Canvas", control_type="Group")
        .wait("visible", timeout=5)
    )

    rect = canvas_field.rectangle()
    
    # Calculate left, right, top and bottom coordinates for the rectangle
    left = rect.left
    right = rect.right
    top = rect.top
    bottom = rect.bottom
    mid_point = (rect.mid_point().x, rect.mid_point().y)

    return {"left": left, "right": right, "top": top, "bottom": bottom, "mid_point": mid_point}

def get_ear_coordinates(canvas_middle: tuple, head_radius: int, ear_radius: int) -> dict:
    """
    Return the top left coordinates of the ears based on the canvas_middle and head_radius.
    
    The ears and head overlap perfectly if the middle_point coordinates of the ears are calculated as follows:
        x_mid = canvas_middle[0] +- sqrt((head_radius + ear_radius)^2 - (ear_radius)^2) 
        y_mid = canvas_middle[1] + ear_radius
    This is pure mathematics and geometry using Pythagoras theorem.
    
    Thus the top left coordinates of the ears are:
        x_top_left = x_mid - ear_radius
        y_top_left = y_mid - ear_radius
        
    Returns:
        dict: The top left coordinates of the ears with keys 'left' and 'right'
    """
    
    # Calculate the x-coordinate offset from the canvas middle to the ear middle
    x_offset = sqrt((head_radius + ear_radius)**2 - ear_radius**2)
    
    # Calculate the middle coordinates of the ears
    left_ear_mid_x = canvas_middle[0] - x_offset
    right_ear_mid_x = canvas_middle[0] + x_offset
    ear_mid_y = canvas_middle[1] - ear_radius  # Note: subtracted ear_radius instead of adding
    
    # Calculate the top left coordinates of the ears
    ear_x_left = left_ear_mid_x - ear_radius
    ear_x_right = right_ear_mid_x - ear_radius
    ear_y = ear_mid_y - ear_radius
    
    return {"left": (ear_x_left, ear_y), "right": (ear_x_right, ear_y)}