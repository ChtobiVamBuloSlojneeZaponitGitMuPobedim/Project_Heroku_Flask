from flask import Flask, render_template, redirect
import os

app = Flask(__name__)

@app.route("/")
@app.route('/index')
def index():
    return 'hello world'
  
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
