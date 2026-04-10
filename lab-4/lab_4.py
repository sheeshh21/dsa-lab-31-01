from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

login_manager = LoginManager(app)
login_manager.login_view = 'login_page'

# Модель User
class User(UserMixin):
    def __init__(self, id, email, password, name):
        self.id = id
        self.email = email
        self.password = generate_password_hash(password)
        self.name = name

# База данных
users = []
next_id = 1

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if str(user.id) == user_id:
            return user
    return None

# Корневая страница
@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('index.html')
    return redirect(url_for('login_page'))

# Страница входа
@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

# Авторизация
@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = None
    for u in users:
        if u.email == email:
            user = u
            break
    
    if not user:
        return render_template('login.html', error='Пользователь не найден')
    
    if not check_password_hash(user.password, password):
        return render_template('login.html', error='Неверный пароль')
    
    login_user(user)
    return redirect(url_for('index'))

# Страница регистрации 
@app.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')

# Регистрация
@app.route('/signup', methods=['POST'])
def signup_post():
    global next_id
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    
    for u in users:
        if u.email == email:
            return render_template('signup.html', error='Пользователь уже существует')
    
    users.append(User(next_id, email, password, name))
    next_id += 1
    
    return redirect(url_for('login_page'))

# Выход
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login_page'))

if __name__ == '__main__':
    app.run(debug=True)