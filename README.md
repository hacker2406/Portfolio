# Ratul Paul's Portfolio

A modern, responsive personal portfolio web application built with **Flask (Python)**, **Tailwind CSS**, and **JavaScript**.

Showcases personal introduction, skills, projects, experience, blog, and a contact form with persistent storage.

---

## 🚀 Features

- **Responsive Design:** Built with Tailwind CSS for mobile and desktop.
- **Modular Backend:** Flask Blueprints for clean code structure.
- **Dynamic Content:** Skills, projects, experience, blog posts, and contact messages loaded from JSON files.
- **Interactive UI:** Animated backgrounds, hover effects, and mobile navigation.
- **Contact Form:** Stores submissions in a JSON file.
- **Blog Section:** Posts loaded dynamically from JSON.
- **Easy Deployment:** Ready for platforms like Render, Railway, or Vercel.

---

## 🛠️ Tech Stack

- **Frontend:** HTML, Tailwind CSS, JavaScript
- **Backend:** Python, Flask, Jinja2
- **Data:** JSON files for blog posts and contact messages

---

## 📦 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hacker2406/Portfolio.git
   cd Portfolio
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app:**
   ```bash
   python app.py
   ```
   The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## 📁 Project Structure

```
Portfolio/
│
├── app.py
├── requirements.txt
├── main/
│   └── routes.py
├── blog/
│   ├── routes.py
│   └── blog_data.json
├── contact/
│   ├── routes.py
│   └── contact_messages.json
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── hero.html
│   ├── skills.html
│   ├── projects.html
│   ├── experience.html
│   ├── education.html
│   ├── training_certificates.html
│   ├── blog.html
│   └── contact.html
└── static/
    └── images/
        └── mypic.jpg
```

---

## ✉️ Contact

- **Email:** ratul.9paul@gmail.com
- **LinkedIn:** [ratulpaul2002](https://www.linkedin.com/in/ratulpaul2002/)
- **GitHub:** [hacker2406](https://github.com/hacker2406)

---

## 🌐 Deployment

You can deploy this project on [Render](https://render.com), [Railway](https://railway.app), or [Vercel](https://vercel.com).

See below for Vercel deployment steps.

---

## 📄 License

This project is for educational and personal portfolio use.

---

## 🙏 Credits

- [Tailwind CSS](https://tailwindcss.com/)
- [Flask](https://flask.palletsprojects.com/)
- [Icons8](https://icons8.com/) for project icons

---

**Thank you
