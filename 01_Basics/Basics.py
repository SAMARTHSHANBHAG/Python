print("Hello world")
# This is a comment

# Multiline print
print(''' Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky. ''')


import os

# Specify the directory path
directory_path = "your_directory_path_here"  # Replace with your directory path

# List the contents of the directory
contents = os.listdir('/')

# Print the contents
for item in contents:
    print(item)

    
# TEXT TO AUDIO
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()