"print('Hello world')"


from flask import Flask, render_template

app = Flask(__name__)



"""to run app.py: python -m flask run
for python scripts: python filename.py
for testing in the interactive terminal: python 
from filename import function1, function2
"""
#function decorator = says what the function is about
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "A Typical Workday"
    
    text = """It is your first day as a security guard at an old toy factory. You haven't met your employer in person due to covid restrictions, but they seemed nice during your zoom interview.
    You successfully turn on all surveillance cameras and sip your coffee. Suddenly, you notice some weird blurry figure moving on one camera. """

    choices = [
        ('go_to',"Go and check the room where movement happened"),
        ('continue_watching',"Continue to watch the movement")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/movement")
def go_to():
    title = "You decide to learn what happened"
    
    text = """You grab your flashlight and keys and go to the room. The corridors are dark and unusually quiet. Finally, you reach the room, which seems to be some kind of 
    warehouse for defective products. You hear loud noise, as if someone was scratching the door from the other side"""

    choices = [
        ('open_door',"Open the door"),
        ('run_away',"Turn back and run away")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/escape")
def run_away():
    title = "You run away!"
    
    text = """You quickly turn back and run as fast as you can. Finally, after reaching your room, you make sure to close the doors and cautiously look at the cameras.
    You don't see anything weird in the warehouse. You decide not to think about the incident for the time being, but you'll definitely ask your employer some questions about it. The rest of the night was quiet and peaceful."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/watch")
def continue_watching():
    title = "You decide to observe the figure"
    
    text = """As you continue watching the cameras, your eyesight adjusts to the darkness. The figure seems to be still. Apparently, it's just a bunch of boxes.
    Well, it probably was due to a lack of sleep. You quickly forget about the incident, and the rest of workday was quiet and peaceful."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)


@app.route("/warehouse")
def open_door():
    title = "You open the door"
    
    text = """At first, you don't see anything. But they can see you. 
    Ugly defective toys jump at you, their sharp claws digging into your body. 
    The last thing you see are their empty eyes filled with void."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)
