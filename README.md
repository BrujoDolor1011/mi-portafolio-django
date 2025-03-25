# 🌐 Mi Portafolio en Django  

🚀 **Portafolio web desarrollado con Django y Bootstrap**, donde presento mi **currículum**, certificados y una opción para descargar mi CV. También incluye un enlace para invitarme un café ☕.  

## 📸 Capturas de Pantalla  

![Portafolio Preview](static/img/preview.png)  
*(Si tienes una imagen del proyecto, agrégala aquí y cambia la ruta del archivo.)*  

---

## 🛠️ Tecnologías Utilizadas  

- 🐍 **Python 3.x**  
- 🎨 **Django** (Back-end)  
- 💄 **Bootstrap 5.3** (Diseño responsivo)  
- 🎭 **Font Awesome** (Iconos)  
- 📄 **HTML5, CSS3 y JavaScript**  

---

## 📦 Instalación y Uso  

### 🔹 1. Clona el repositorio  

```bash
git clone https://github.com/BrujoDolor1011/mi-portafolio-django.git
cd mi-portafolio-django
```

### 🔹 2. Crea un entorno virtual (opcional, pero recomendado)  

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 🔹 3. Instala las dependencias  

```bash
pip install -r requirements.txt
```

### 🔹 4. Ejecuta migraciones y arranca el servidor  

```bash
python manage.py migrate
python manage.py runserver
```

🔗 Luego, accede a **http://127.0.0.1:8000/** en tu navegador.  

---

## 📁 Estructura del Proyecto  

```
mi-portafolio-django/
│── mi_portafolio/         # Aplicación principal de Django
│── static/                # Archivos estáticos (CSS, JS, imágenes)
│── templates/             # Plantillas HTML
│── db.sqlite3             # Base de datos SQLite (se genera automáticamente)
│── manage.py              # Archivo principal de Django
│── requirements.txt       # Lista de dependencias
└── README.md              # Este archivo
```

---

## 🎨 Personalización  

- 📌 **Para cambiar tu información personal**, edita el modelo `Perfil` en la base de datos.  
- 📸 **Para agregar más certificados**, súbelos a la carpeta `media/` y regístralos en la base de datos.  
- 🎨 **Puedes modificar los estilos en** `static/style.css`.  

---

## 🤝 Contribuciones  

¡Cualquier sugerencia, mejora o contribución es bienvenida! Solo haz un **fork** del repositorio y envía un **pull request**.  

---

## ☕ Apóyame  

Si te gusta mi trabajo y quieres apoyar, **¡invítame un café!**  

[![Invítame un café](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-FFDD00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/brujodolor1011)  

---

## 📜 Licencia  

Este proyecto está bajo la **Licencia MIT**. Puedes usarlo y modificarlo libremente.  