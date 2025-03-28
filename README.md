# SOLID Principles - User Roles Implementation  

This project demonstrates the **Liskov Substitution Principle (LSP)** and **Interface Segregation Principle (ISP)** through a role-based user system in Python.  

## 🚀 Features  
- **LSP**: Subclasses (`Reader`, `Editor`, `Admin`) can replace the base `User` class without issues.  
- **ISP**: Each role implements only the necessary interfaces (`IReader`, `IEditor`, `IAdmin`).  
- Clean and scalable design following **SOLID** principles.  

## 📜 Code Overview  
- `User`: Base class for all users.  
- `Reader`: Can read content.  
- `Editor`: Can read and edit content.  
- `Admin`: Can read, edit, and delete content.  

## 🛠 Installation  
```bash
git clone https://github.com/jhonticonachambi/solid-roles.git  
cd solid-roles  
python app.py  
