from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():

    data = {
        'name':謝承晏',
        'age': 20,
        'city': '台北'
    }


    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run()
