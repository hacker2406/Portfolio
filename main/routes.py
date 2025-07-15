import json
import os
from flask import render_template
from . import main_bp

@main_bp.route('/')
def home():
    blog_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'blog', 'blog_data.json')
    with open(blog_path, 'r') as f:
        posts = json.load(f)
    return render_template('index.html', name="Ratul Paul", posts=posts)

@main_bp.route('/skills')
def skills():
    return render_template('skills.html', name="Ratul Paul")

@main_bp.route('/projects')
def projects():
    return render_template('projects.html', name="Ratul Paul")

@main_bp.route('/experience')
def experience():
    return render_template('experience.html', name="Ratul Paul")

@main_bp.route('/training')
def training():
    return render_template('training_certificates.html', name="Ratul Paul")

@main_bp.route('/education')
def education():
    return render_template('education.html', name="Ratul Paul")