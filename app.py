from flask import Flask, render_template, request, redirect, url_for, make_response
from auth import AuthSystem
from user_models import Reader, Editor, Admin

app = Flask(__name__)
app.secret_key = 'clave_super_secreta'  # Cambia esto en producción

# Sistema de autenticación en memoria
auth_system = AuthSystem()

# Datos iniciales de prueba
auth_system.add_user("Ana", "ana@example.com", "pass123", "Reader")
auth_system.add_user("Luis", "luis@example.com", "pass123", "Editor")
auth_system.add_user("Carlos", "carlos@admin.com", "pass123", "Admin")

@app.route('/')
def home():
    session_id = request.cookies.get('session_id')
    user_data = auth_system.get_user_from_session(session_id)
    
    if not user_data:
        return redirect(url_for('login'))
    
    # Crear instancia de usuario según su rol (LSP)
    role = user_data['role']
    if role == "Reader":
        user = Reader(user_data['name'], user_data['email'])
    elif role == "Editor":
        user = Editor(user_data['name'], user_data['email'])
    elif role == "Admin":
        user = Admin(user_data['name'], user_data['email'])
    
    return render_template('index.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        session_id = auth_system.login(email, password)
        
        if session_id:
            response = make_response(redirect(url_for('home')))
            response.set_cookie('session_id', session_id, httponly=True)
            return response
        return render_template('login.html', error="Credenciales incorrectas")
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session_id = request.cookies.get('session_id')
    if session_id:
        auth_system.logout(session_id)
    response = make_response(redirect(url_for('login')))
    response.delete_cookie('session_id')
    return response

if __name__ == '__main__':
    app.run(debug=True)