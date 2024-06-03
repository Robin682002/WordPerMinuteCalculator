'''import  pyttsx3
from PyPDF2 import PdfReader
import threading
import keyboard  # Import the keyboard library

pdf = None
stop_thread = False  # Variable to signal stopping the playback


def play(pdfReader):
    global pdf
    global stop_thread

    speaker = pyttsx3.init()

    for page_num in range(len(pdfReader.pages)):
        if stop_thread:
            break  # Exit the loop if stop_thread is True
        text = pdfReader.pages[page_num].extract_text()
        speaker.say(text)
        speaker.runAndWait()

    speaker.stop()


def stop_playback():
    global stop_thread
    input("Press Enter to stop playback...")
    stop_thread = True  # Set the flag to stop playback


file = input("Enter your PDF file name: ")

while True:
    try:
        pdf = PdfReader(file)
        break
    except Exception as e:
        print("An error occurred:\n", e)
        print("\nEnter the file name again:\n")
        file = input("Enter your PDF file name: ")

# Create a separate thread for playback
playback_thread = threading.Thread(target=play, args=(pdf,))
playback_thread.start()

# Start a thread for stopping playback with keyboard input
keyboard.add_hotkey("q", lambda: stop_playback())
keyboard.wait()  # Wait for the hotkey event

# Wait for the playback to finish
playback_thread.join()'''


import time
from essential_generators import DocumentGenerator

def typing_speed():

    # Generating a random sentence
    gen = DocumentGenerator()
    String = gen.sentence()
    wordcount=len(String.split())

    # Typing Speed Calculation
    print(String)
    print("----------------------------------------")
    startTime=time.time()
    textInput=str(input("Type the sentence: " ))
    endTime=time.time()
    accuracy= len(set(textInput.split())&set(String.split()))
    accuracy=accuracy/wordcount*100
    timeTaken=round(endTime-startTime,2)
    wpm=round((wordcount/timeTaken)*60)
    print("----------------------------------------")

    # Showing the results
    print ("Your accuracy is: ", accuracy)
    print ("Time taken: ", timeTaken, "seconds")
    print("Your typing speed is: ",wpm,"words per minute")

    if accuracy < 50 or wpm < 30:
        print("You need to practice typing more!")
    elif accuracy < 80 or wpm < 60:
        print("You are doing great!")
    elif accuracy <= 100 or wpm <= 100:
        print("You are a pro in typing!")
    else:
        print("You are a typing machine!")


if __name__ == "__main__":
    print("Let's Start")
    typing_speed()

    while True :
        if input("Do you want to try again? (y/n): ")=="y":
            print("\n")
            typing_speed()
        else:
            break

