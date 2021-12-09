from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello,world'

if __name__ == "__main__":
    print('hello')
    app.run(debug=True)
