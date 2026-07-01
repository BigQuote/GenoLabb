from flask import Flask, render_template

app = Flask(__name__)

# =========================
# Página Inicial
# =========================
@app.route("/")
def index():
    return render_template("index.html")


# =========================
# Quem Somos
# =========================
@app.route("/quem-somos")
def quem_somos():
    return render_template("quem_somos.html")


# =========================
# Exames
# =========================
@app.route("/exames")
def exames():
    return render_template("exames.html")


# =========================
# Especialidade
# =========================
@app.route("/especialidade")
def especialidade():
    return render_template("especialidade.html")


# =========================
# Blog
# =========================
@app.route("/blog")
def blog():
    return render_template("blog.html")


# =========================
# Contato
# =========================
@app.route("/contato")
def contato():
    return render_template("contato.html")


if __name__ == "__main__":
    app.run(debug=True)
