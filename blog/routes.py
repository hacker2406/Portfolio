from flask import render_template, jsonify
from . import blog_bp
import json
import os

@blog_bp.route('/blog')
def blog():
    # Load blog posts from JSON
    blog_path = os.path.join(os.path.dirname(__file__), 'blog_data.json')
    with open(blog_path, 'r') as f:
        posts = json.load(f)
    return render_template('blog.html', posts=posts, name="Ratul Paul")

@blog_bp.route('/api/blog')
def blog_api():
    blog_path = os.path.join(os.path.dirname(__file__), 'blog_data.json')
    with open(blog_path, 'r') as f:
        posts = json.load(f)
    return jsonify(posts)