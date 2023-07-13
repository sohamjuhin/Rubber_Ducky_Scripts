# Rubber_Ducky_Scripts
Rubber_Ducky_Scripts
Rubber Ducky is a popular USB device that emulates a keyboard and can be used for various purposes,
including automation and penetration testing. While it typically uses a specialized scripting language, 
you can write Python scripts that emulate Rubber Ducky-like behavior on a regular keyboard

In this code, we use the keyboard library in Python to simulate keystrokes. 
The type_keystrokes() function takes a list of keystrokes as input and emulates typing them out one by one, with a small delay between each keystroke.

The code keystrokes include regular text ("Hello, world!","This is a test") and a special command ("DELAY 1") that introduces a delay of 1 second between keystrokes.
You can customize the keystrokes according to your specific requirements.

#To run this script, make sure you have the keyboard library installed. You can install it using the following command:
pip install keyboard

#Save the script to a file, such as rubber_ducky.py, and then run it using Python
python rubber_ducky.py

The script will emulate the specified keystrokes, typing them out with the specified delays.
Please note that this is a simplified example, and Rubber Ducky devices often offer more advanced functionality and features.
