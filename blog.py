from flask import Flask
import os
import re
import glob
import mistune
app = Flask(__name__)
from flask import render_template, request


def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)', text) ]

def get_posts():
    markdowns = [os.path.basename(x) for x in glob.glob("./posts/*.md")]
    markdowns.sort(key=natural_keys, reverse=True)
    return markdowns

@app.route('/')
def hello_world():
    posts = []
    for post in get_posts():
        p = os.path.join('./posts/', post)
        f = open(p, 'r')
        raw = f.read().decode('utf-8')
        rendered = mistune.markdown(raw)
        posts.append(rendered)
        f.close()

    return render_template('blog.html', posts=posts)

if __name__ == '__main__':
    from flask_frozen import Freezer
    app.debug=True
    app.testing = True
    app.config['FREEZER_DESTINATION'] = "out/blog"
    freezer = Freezer(app)
    freezer.freeze()
