import time

def explain_installation():
    # Step 1: Explain the purpose of the program
    print("Step 1: This program will guide you through installing the required libraries for automating a task that clicks an image on the screen.")

    # Step 2: Explain how to install pip if not installed
    print("\nStep 2: First, make sure you have pip installed, which is Python's package manager.")
    print("To check if pip is installed, run this command in your terminal or command prompt:")
    print("    python -m ensurepip --upgrade")
    
    # Pause for 3 seconds before continuing
    time.sleep(3)

    # Step 3: Explain how to install required libraries
    print("\nStep 3: Now, you'll need to install the required libraries: 'pyautogui' and 'opencv-python'.")
    print("You can install them by running the following command:")
    print("    pip install pyautogui opencv-python")
    
    # Pause for 3 seconds before continuing
    time.sleep(3)

    # Step 4: Explain how to verify installation
    print("\nStep 4: To verify that the libraries were installed correctly, you can run:")
    print("    pip show pyautogui")
    print("    pip show opencv-python")
    print("These commands will display details about the installed libraries.")
    
    # Pause for 3 seconds before continuing
    time.sleep(3)

    # Step 5: Explain where to place the image file
    print("\nStep 5: Make sure you have an image file saved on your computer.")
    print("For example, save the image as 'image.png' in the same folder where your Python script is located.")
    
    # Pause for 3 seconds before continuing
    time.sleep(3)

    # Step 6: Explain how to run the Python script
    print("\nStep 6: Now you are ready to run the Python script that searches for the image and clicks it!")
    print("In your terminal or command prompt, run the script using:")
    print("    python your_script_name.py")
    
    # Pause for 3 seconds before ending
    time.sleep(3)

    print("\nThat's it! You're all set to automate the task of clicking an image when it appears on the screen.")

# Run the installation guide function
explain_installation()
