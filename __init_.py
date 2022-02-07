import os
import html
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def content(): 
        with open('/root/flask_project/textfile.txt', 'r') as f: 
                return render_template('index.html', text=f.read())

if __name__ == '__main__':
   app.run()

