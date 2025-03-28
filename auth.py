import secrets
from datetime import datetime, timedelta

class AuthSystem:
    def __init__(self):
        self.users = {}      # {email: {name, password, role}}
        self.sessions = {}   # {session_id: {email, expires_at}}
    
    def add_user(self, name, email, password, role):
        """Añade un nuevo usuario al sistema"""
        self.users[email] = {
            'name': name,
            'password': password,  # En producción usaría hashing
            'role': role
        }
    
    def login(self, email, password):
        """Intenta autenticar al usuario"""
        user = self.users.get(email)
        if user and user['password'] == password:
            session_id = secrets.token_hex(16)
            expires_at = datetime.now() + timedelta(hours=1)
            self.sessions[session_id] = {
                'email': email,
                'expires_at': expires_at
            }
            return session_id
        return None
    
    def logout(self, session_id):
        """Cierra la sesión del usuario"""
        self.sessions.pop(session_id, None)
    
    def get_user_from_session(self, session_id):
        """Obtiene los datos del usuario si la sesión es válida"""
        if not session_id:
            return None
            
        session = self.sessions.get(session_id)
        if not session or session['expires_at'] < datetime.now():
            return None
            
        user_email = session['email']
        user_data = self.users.get(user_email)
        if user_data:
            return {**user_data, 'email': user_email}
        return None