# A very simple Flask Hello World app for you to get started with...
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<p><b>Hello from Flask!</b></p><table><tr><td><b>Aluno:</b></td><td>Enzo da Silva Pelegrini</td></tr><tr><td><b>Prontuário:</b></td><td>PT3022277</td></tr></table>'
