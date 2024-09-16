"""Main module for the application."""
from art_robot.art_robot import draw_head, draw_ears, draw_face
from art_robot.init_task import init_task

def main():
    """Main logic."""
    (app, config) = init_task()
    canvas = config["canvas"]
    draw_head(app, canvas, config["head_radius"])
    draw_ears(app, canvas, config["head_radius"], config["ear_radius"])
    draw_face(app, canvas, config["nose_width"], config["nose_height"], config["eye_width"], config["eye_height"], config["mouth_radius"])

if __name__ == "__main__":
    main()