from stories import Story, story, story2, story3
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

stories = [story, story2, story3]
story_list = ["Generic", "Phone Call", "Cute Zoo Story"]
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/madprompt')
def prompt():
    select = int(request.args.get('stories_selection'))
    story_list = ["Generic", "Phone Call", "Cute Zoo Story"]
    return render_template('madlib.html', prompt = stories[select].prompts, title = story_list[select], help_id = select)    
    # the <select> variable does not allow .prompts to be used, says its just a string, why is that?
    





@app.route("/story")
def show_story():
    """Show story result."""
    prompty = int(request.args.get("help_id"))
    text = stories[prompty].generate(request.args)
   
    return render_template("story.html", template=text)



