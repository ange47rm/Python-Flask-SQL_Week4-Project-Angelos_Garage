from flask import Flask, render_template
from controllers.controller import garage_blueprint

app = Flask (__name__)

app.register_blueprint(garage_blueprint)

@app.route ('/')
def home ():
    return render_template ('landing.html')

if __name__ == '__main__':
    app.run(debug=True)