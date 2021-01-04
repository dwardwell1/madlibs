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
    
    number = len(request.args)
    if number <= 6:
        text = story.generate(request.args)
    elif number > 6 and number < 10:
        text = story2.generate(request.args)
    else: 
        text = story3.generate(request.args)
    
    return render_template("story.html", template=text)
    


# @app.route("/story")
# def show_story():
#     """Show story result."""
#     prompty = request.args("help_id")
#     text = story.generate(request.args)
   
#     return render_template("story.html", template=text)



# dev questions: how to import story from stories.py
# @app.route('/story')
# def story_result():
#     length = len(story3.prompts)
#     ans = {}
#     for x in range(length):
#         place = request.args.get(story3.prompts[x])
#         ans[story3.prompts[x]] = place
#     finished_story = story3.generate(ans)
#     return render_template('story.html', template = finished_story)
# looking at the answer, I over complicated this code, didnt know I could just do request.args() for all the args but thats okay, took a lot of trial and error to get to this point