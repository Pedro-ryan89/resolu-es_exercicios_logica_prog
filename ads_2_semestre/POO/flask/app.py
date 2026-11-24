from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('hello_world.html')


@app.route("/perfil")
def perfil():
    return render_template('perfil.html', nome='Ana',idade=20)

if __name__ == "__main__":
    app.run(debug=True)