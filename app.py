from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eventos.db'
db = SQLAlchemy(app)

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data = db.Column(db.String(50), nullable=False)
    local = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)

@app.route('/')
def index():
    eventos = Evento.query.all()
    return render_template('index.html', eventos=eventos)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        novo_evento = Evento(
            nome=request.form['nome'],
            data=request.form['data'],
            local=request.form['local'],
            descricao=request.form['descricao']
        )
        db.session.add(novo_evento)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('adicionar.html')

@app.route('/buscar', methods=['GET'])
def buscar():
    termo = request.args.get('termo', '')
    resultados = Evento.query.filter(Evento.nome.contains(termo)).all()
    return render_template('buscar.html', resultados=resultados)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    evento = Evento.query.get_or_404(id)
    if request.method == 'POST':
        evento.nome = request.form['nome']
        evento.data = request.form['data']
        evento.local = request.form['local']
        evento.descricao = request.form['descricao']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editar.html', evento=evento)

@app.route('/remover/<int:id>', methods=['GET', 'POST'])
def remover(id):
    evento = Evento.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(evento)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('remover.html', evento=evento)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)