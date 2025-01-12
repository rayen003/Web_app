"""
Modern Web Application with Flask
--------------------------------
A clean, containerized Flask application demonstrating modern web development practices.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('animation.html', title='Modern Web App')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
