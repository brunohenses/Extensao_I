from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from hashlib import sha256
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eventos.db'
app.config['SECRET_KEY'] = 's3cr3t_k3y'
db = SQLAlchemy(app)

# Configuração do Flask Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)


class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data = db.Column(db.String(50), nullable=False)
    local = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.template_filter('format_date')
def format_date(value):
    try:
        date_obj = datetime.strptime(value, '%Y-%m-%d')
        return date_obj.strftime('%d/%m/%Y')
    except:
        return value

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = sha256(request.form['password'].encode()).hexdigest()
        user = User.query.filter_by(username=username, password_hash=password).first()
        if user:
            login_user(user)
            return redirect(url_for('index'))
        flash('Usuário ou senha inválidos.')
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = sha256(request.form['password'].encode()).hexdigest()
        if User.query.filter_by(username=username).first():
            flash('Usuário já existe.')
            return redirect(url_for('registro'))
        new_user = User(username=username, password_hash=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('registro.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/')
def index():
    eventos = Evento.query.all()
    return render_template('index.html', eventos=eventos)

@app.route('/adicionar', methods=['GET', 'POST'])
@login_required
def adicionar():
    if request.method == 'POST':
        novo_evento = Evento(
            nome=request.form['nome'],
            data=request.form['data'],
            local=request.form['local'],
            descricao=request.form['descricao'],
            user_id=current_user.id
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
@login_required
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
@login_required
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