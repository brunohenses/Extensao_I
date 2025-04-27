import os
import bcrypt
import yaml
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

app = Flask(__name__)

# Carrega configurações do YAML
with open('config.yml') as f:
    config = yaml.safe_load(f)

# Configurações
app.config['SQLALCHEMY_DATABASE_URI'] = config['database']['uri']
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')  # Chave lida do .env

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# --- Modelos ---
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data = db.Column(db.String(50), nullable=False)
    local = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# --- Configuração do Login ---
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- Filtro de Formatação de Data ---
@app.template_filter('format_date')
def format_date(value):
    try:
        date_obj = datetime.strptime(value, '%Y-%m-%d')
        return date_obj.strftime('%d/%m/%Y')
    except:
        return value

# --- Rotas de Autenticação ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if not user:
            flash('Usuário não encontrado.', 'error')
            return redirect(url_for('login'))

        if user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Usuário ou senha inválidos.', 'error')
   
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Usuário já existe.')
            return redirect(url_for('registro'))
        
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash('Usuário registrado com sucesso!')
        return redirect(url_for('login'))
    
    return render_template('registro.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# --- Rotas Principais ---
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