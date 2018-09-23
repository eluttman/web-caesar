from ceasar import rotate_string
from flask import Flask, request


app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin-top: 10px;
                width: 100%;
                height: 90px;
                margin-bottom: 10px;
            }}
        </style>
    </head>
    <body>
        
        <form action="/" method="POST">
            <div>
                Rot:
                <input type="text" name="rot" value="0">
            </div>
            
            <div>
                <textarea name="text" >{0}</textarea>
            </div>

            <div>
                <input type="submit" value="Submit">
            </div>
        </form>
    </body>
</html>"""

@app.route("/", methods=['POST'])
def encrypt():
    rot_num = int(request.form["rot"])
    text = request.form["text"]
    encrypted_message = rotate_string(text,rot_num)
    print("lolololol")
    return form.format(encrypted_message)

@app.route("/")
def index():
    return form.format("")
app.run()