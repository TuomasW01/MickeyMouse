"""Module for initializing the task."""
import yaml
import pyautogui
import time
from pywinauto.application import Application
from art_robot.helper_functions import get_canvas_information


def read_config() -> dict:
    """Read process_variables.yaml and return a config dictionary."""
    config_path = '.\process_variables.yaml'
    
    try:
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
        
        # Check if config is a dictionary
        if not isinstance(config, dict):
            raise ValueError("The YAML file does not contain a valid dictionary.")
        
        return config
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file: {e}")

def init_paint(config: dict) -> tuple:
    """Open Paint application, connect with pywinauto, ensure full screen canvas and return the Application."""
    # Open the Run dialog
    pyautogui.hotkey('win', 'r')
    time.sleep(0.5)  # Wait for the Run dialog to open

    # Type 'mspaint' and press Enter
    pyautogui.write('mspaint')
    pyautogui.press('enter')
    time.sleep(2)  # Wait for Paint to open
    
    # Connect with Paint
    app = Application(backend="uia").connect(title="Untitled - Paint", timeout=5)
    
    # Maximize the window
    app.top_window().maximize()

    # Get canvas information
    canvas_information = get_canvas_information(app)
    
    # Add canvas information to config
    config["canvas"] = canvas_information
    
    # Set canvas image properties to canvas width and height
    # Click File -> Properties
    file_field = (
        app.top_window()
        .child_window(title="File", control_type="MenuItem")
        .wait("visible", timeout=5)
    )
    file_field.invoke()

    image_properties = (
        app.top_window()
        .child_window(title="Image properties", control_type="MenuItem")
        .wait("visible", timeout=5)
    )
    
    file_field.invoke()
    image_properties.invoke()
    
    # Set default canvas size
    default_button = (
        app.top_window()
        .child_window(title="Image properties", control_type="Window")
        .child_window(title="Default", control_type="Button")
        .wait("visible", timeout=5)
    )
    default_button.click()

    # Click OK
    ok_button = (
        app.top_window()
        .child_window(title="Image properties", control_type="Window")
        .child_window(title="OK", control_type="Button")
        .wait("visible", timeout=5)
    )
    ok_button.click()
    return (app, config)

def init_task() -> tuple:
    """Initialize the task.
    Returns:
        tuple: The Application object and the config dictionary.
    """
    config = read_config()
    return init_paint(config)