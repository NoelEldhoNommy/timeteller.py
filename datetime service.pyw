import datetime
import pyttsx3
import schedule
import time

def tell_time():
    current_time = datetime.datetime.now()

    # Format the time to display hour and minute in 12 hour format
    formatted_time = current_time.strftime("%I:%M %p")
    engine = pyttsx3.init()
    engine.say("Current time: " + formatted_time)
    engine.runAndWait()

# Schedule the task
for i in range(0, 24):
    for j in range(0, 60, 30):
        schedule.every().day.at(f"{str(i).zfill(2)}:{str(j).zfill(2)}").do(tell_time)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
