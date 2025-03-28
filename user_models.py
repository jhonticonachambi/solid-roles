from abc import ABC, abstractmethod

"""
Implementación de los principios:
- ISP (Interface Segregation Principle): Cada interfaz es específica para un rol
- LSP (Liskov Substitution Principle): Las subclases pueden sustituir a la clase base
"""

# --- INTERFACES SEGREGADAS (ISP) ---
# Cada interfaz define solo lo necesario para un rol específico

class IUser(ABC):
    """Interfaz base para cualquier usuario (mínimo común)"""
    @abstractmethod
    def get_name(self) -> str:
        """Obtiene el nombre del usuario"""
        pass

class IReader(ABC):
    """Interfaz específica para capacidades de lectura"""
    @abstractmethod
    def read_content(self) -> str:
        """Realiza acción de lectura"""
        pass

class IEditor(ABC):
    """Interfaz específica para capacidades de edición"""
    @abstractmethod
    def edit_content(self) -> str:
        """Realiza acción de edición"""
        pass

class IAdmin(ABC):
    """Interfaz específica para capacidades administrativas"""
    @abstractmethod
    def delete_content(self) -> str:
        """Realiza acción de eliminación"""
        pass


# --- CLASE BASE (Para LSP) ---
class User(IUser):
    """
    Implementación base de usuario que cumple con IUser.
    Puede ser sustituida por cualquier subclase (LSP)
    """
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
    
    def get_name(self) -> str:
        """Implementación concreta de IUser"""
        return self.name


# --- SUBCLASES (Implementan interfaces según su rol) ---

class Reader(User, IReader):
    """
    Usuario con rol de Lector.
    Implementa solo IUser + IReader (ISP)
    """
    def read_content(self) -> str:
        """Implementación concreta de IReader"""
        return f"{self.name} está leyendo contenido público."


class Editor(User, IReader, IEditor):
    """
    Usuario con rol de Editor.
    Implementa IUser + IReader + IEditor (ISP)
    Puede sustituir a Reader (LSP)
    """
    def read_content(self) -> str:
        """Implementación mejorada de IReader para editores"""
        return f"{self.name} (Editor) está revisando contenido."
    
    def edit_content(self) -> str:
        """Implementación concreta de IEditor"""
        return f"{self.name} ha editado un artículo."


class Admin(User, IReader, IEditor, IAdmin):
    """
    Usuario con rol de Administrador.
    Implementa todas las interfaces (ISP)
    Puede sustituir a Editor y Reader (LSP)
    """
    def read_content(self) -> str:
        """Implementación mejorada de IReader para admins"""
        return f"{self.name} (Admin) está auditando contenido."
    
    def edit_content(self) -> str:
        """Implementación mejorada de IEditor para admins"""
        return f"{self.name} ha realizado cambios administrativos."
    
    def delete_content(self) -> str:
        """Implementación concreta de IAdmin"""
        return f"{self.name} ha eliminado contenido inapropiado."