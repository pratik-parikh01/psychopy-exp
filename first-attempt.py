from psychopy import visual, core, event, data, gui
import random
import os

# Experiment Setup
experiment_info = {"Participant": ""}
dlg = gui.DlgFromDict(experiment_info)
if not dlg.OK:
    core.quit()

# Directory to save the data
data_dir = "/Users/pratik/Desktop/anjana/data/"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Create a data file for logging responses
data_file = open(data_dir + f"Experiment2_data_{experiment_info['Participant']}.csv", "w")
data_file.write("trial,picture,choice,choice_time,arousal_rating\n")

# Window setup
win = visual.Window(fullscr=True, color="black", units="height")

# List of image stimuli (update with actual image paths)
image_dir = "/Users/pratik/Desktop/anjana/images/"
stimuli = ["image1.jpg", "image2.jpg"]  # Replace with actual filenames
stimuli = [os.path.join(image_dir, img) for img in stimuli]

# Choice and rating setup
choice_text = visual.TextStim(win, text="Choose a strategy:\n1: Use Distraction\n2: Use Reappraisal", color="white", height=0.05)
arousal_slider = visual.Slider(win, ticks=(1, 9), labels=["No Arousal", "High Arousal"], pos=(0, -0.3), size=(1.0, 0.05), style="rating")

# Trial Loop
for trial_num, stimulus in enumerate(stimuli, start=1):
    # Preview Image
    img = visual.ImageStim(win, image=stimulus, size=(1.5, 1.5))
    img.draw()
    win.flip()
    core.wait(0.5)

    # Choice Screen
    choice_text.draw()
    win.flip()
    choice_made = False
    choice = None
    choice_start = core.getTime()

    # Wait for a valid choice
    while not choice_made:
        keys = event.getKeys(keyList=["1", "2", "escape"])
        if "escape" in keys:
            data_file.close()
            win.close()
            core.quit()
        elif "1" in keys:
            choice = "Distraction"
            choice_made = True
        elif "2" in keys:
            choice = "Reappraisal"
            choice_made = True
    choice_time = core.getTime() - choice_start

    # Strategy Implementation (display the image for 5s)
    img.draw()
    win.flip()
    core.wait(5)

    # Collect Arousal Rating
    arousal_slider.reset()  # Reset the slider for each trial
    while arousal_slider.rating is None:
        arousal_slider.draw()
        win.flip()
    arousal_rating = arousal_slider.rating

    # Log data
    data_file.write(f"{trial_num},{stimulus},{choice},{choice_time:.2f},{arousal_rating}\n")

# Close the experiment
data_file.close()
thanks = visual.TextStim(win, text="Thank you for participating!", color="white")
thanks.draw()
win.flip()
core.wait(2)
win.close()
core.quit()

