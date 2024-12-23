from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)

VAGAS = [{
    'id': 1,
    'titulo': 'Desenvolvedor Python Jr',
    'localidade': 'Recife, PE',
    'salario': 'R$ 4.000,00'
}, {
    'id': 2,
    'titulo': 'Analista de Sustentação Jr',
    'localidade': 'João Pessoa, PB',
    'salario': 'R$ 2.500,00'
}, {
    'id': 3,
    'titulo': 'Scrum Master',
    'localidade': 'Caruaru, PE',
    'salario': 'R$ 5.000,00'
}, {
    'id': 4,
    'titulo': 'Desenvolvedor Frontend',
    'localidade': 'Acaraju, SE',
    'salario': 'R$ 4.000,00'
}, {
    'id': 5,
    'titulo': 'Desenvolvedor Python Pl',
    'localidade': 'Feira de Santana, BA',
    'salario': 'R$ 6.000,00'
}]


@app.route('/')
def hello():
  return render_template("home.html", vagas=VAGAS)


@app.route('/vagas')
def lista_vagas():
  return jsonify(VAGAS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
