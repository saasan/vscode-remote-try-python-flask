from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def main():
    return render_template(
        'main.html',
        title='vscode-remote-try-python-flask',
        message='ほげふが')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
