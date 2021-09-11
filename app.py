import requests
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/teste/')
def wallpaper():
    resposta = requests.get('https://randomfox.ca/floof/')
    wallpaper = resposta.json()['image']


    return render_template('simulado.html', wallpaper=wallpaper)

if __name__ == '__main__':
    app.run()
