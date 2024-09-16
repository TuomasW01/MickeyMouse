"""Function to draw any oval shape based body part."""
import pyautogui
from pywinauto.application import Application

def draw_body_part(app: Application, canvas: dict, width: int, height: int, color: str, top_left_coordinates: tuple) -> None:
    """Draw a body part with height and width starting from the top_left_coordinates and fill it with Color 1 if color is black."""
    # Check if the body part fits to the canvas
    top_left_x = top_left_coordinates[0]
    top_left_y = top_left_coordinates[1]

    if (top_left_x < canvas['left'] or
        top_left_y < canvas['top'] or
        top_left_x + width > canvas["right"] or
        top_left_y + height > canvas['bottom']):
        raise ValueError("The body part does not fit to the canvas.")

    # Select oval shape from Shapes
    oval_button = (
        app.top_window()
        .child_window(title="Shapes", control_type="Group")
        .child_window(title="Oval", control_type="ListItem")
        .child_window(title="Oval", control_type="Button")
        .wait("visible", timeout=5)
    )

    rect = oval_button.rectangle()

    # Move the mouse to the center of the Oval button and click
    x = (rect.left + rect.right) / 2
    y = (rect.top + rect.bottom) / 2
    pyautogui.moveTo(x, y)
    pyautogui.doubleClick()
    pyautogui.sleep(1)

    # Move to the top_left_coordinates and draw the oval to the canvas
    pyautogui.moveTo(top_left_x, top_left_y)
    pyautogui.mouseDown(button='left')
    pyautogui.dragRel(width, height, duration=1)
    pyautogui.mouseUp(button='left')

    # Fill the body part with color only if color is black. Assumption: Color 1 is black (default).
    if(color != "black"):
        return
    
    # Select Fill with color from Tools
    fill_button = (
        app.top_window()
        .child_window(title="Tools", control_type="Group")
        .child_window(title="Fill", control_type="Button")
        .wait("visible", timeout=5)
    )
    fill_button.click_input()
    pyautogui.sleep(1)
    # Move to the middle point of the body part and click to fill with color
    middle_point_coordinates = (top_left_x + (width/2), top_left_y + (height/2))
    pyautogui.moveTo(middle_point_coordinates)
    pyautogui.doubleClick()