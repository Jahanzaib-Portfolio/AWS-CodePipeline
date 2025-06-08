from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Jahanzaib Khan- Cloud Enthusiast</title>
            <style>
                body {
                    background: linear-gradient(to right, #00c6ff, #0072ff);
                    color: white;
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-size: 2em;
                }
            </style>
        </head>
        <body>
            Jahanzaib — Cloud Enthusiast
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
