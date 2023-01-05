import pyautogui
import time
import datetime

def track_activity():
    # Initialize variables to store activity data
    mouse_clicks = 0
    key_presses = 0
    previous_mouse_position = (0, 0)
    previous_keyboard_activity_time = datetime.datetime.now()

    while True:
        # Check for mouse activity
        current_mouse_position = pyautogui.position()
        if current_mouse_position != previous_mouse_position:
            # Update mouse click count
            mouse_clicks += 1
            previous_mouse_position = current_mouse_position

        # Check for keyboard activity
        current_keyboard_activity_time = datetime.datetime.now()
        if current_keyboard_activity_time != previous_keyboard_activity_time:
            # Update key press count
            key_presses += 1
            previous_keyboard_activity_time = current_keyboard_activity_time

        # Sleep for 1 second before checking for activity again
        time.sleep(1)

        # Check if it's time to save activity data to the database
        current_time = datetime.datetime.now()
        if (current_time - previous_keyboard_activity_time).total_seconds() >= 1800:
            # Save data to database
            save_to_database(mouse_clicks, key_presses)

            # Reset activity counters
            mouse_clicks = 0
            key_presses = 0

def save_to_database(mouse_clicks, key_presses):
    # Connect to database
    conn = sqlite3.connect('activity_tracker.db')

    # Save data to database
    c = conn.cursor()
    c.execute("INSERT INTO activity_tracker (mouse_clicks, key_presses) VALUES (?, ?)", (mouse_clicks, key_presses))
    conn.commit()

    # Close database connection
    conn.close()

if __name__ == '__main__':
    track_activity()
