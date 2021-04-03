from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    f=open('./data/data.txt','r')
    return f.read()

if __name__ == '__main__':
    app.run(debug=True)

