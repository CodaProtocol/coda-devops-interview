from flask import Flask
import emoji

app = Flask(__name__)

@app.route('/hello')
def helloIndex():
    return emoji.emojize('Hello World! :globe_with_meridians:')

if __name__ == '__main__':
    app.run(
        ssl_context = ('secrets/cert.pem', 'secrets/key.pem'),
        host = '0.0.0.0',
        port = 8000
    )
