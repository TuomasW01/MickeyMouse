## ART ROBOT
### Process description
This robot opens Paint and draws the smiling face of Mickey Mouse.
### Used technologies
-- Windows 11
-- python version 3.12.6
-- pyautogui version 0.9.54
-- pywinauto version 0.6.8
### How to run
In process_variables.yaml, input values for the bodypart variables
In the project directory run command 'python main.py'
## Test Coverage
Tests can be run with "pytest tests\test.py" and cover testing initializing the task and drawing a white and black body part and the mouth.
### Example run video
https://youtu.be/AMrsrHT6fpg
### Issues
In windows 11 paint some elements have incorrect control types when inspected through Accessibility Insights for Windows.
Thus the oval button needs to be pressed using pyautogui instead of the more convinient way of using pywinauto. 
