import json
import os
from flask import render_template, request, flash, redirect, url_for
from . import contact_bp

@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Prepare the message data
        entry = {
            "name": name,
            "email": email,
            "message": message
        }
        # Path to the messages file
        messages_path = os.path.join(os.path.dirname(__file__), 'contact_messages.json')
        # Safely load existing messages
        messages = []
        if os.path.exists(messages_path):
            with open(messages_path, 'r') as f:
                try:
                    content = f.read().strip()
                    if content:
                        messages = json.loads(content)
                except Exception:
                    messages = []
        # Add the new entry
        messages.append(entry)
        # Write back to the file
        with open(messages_path, 'w') as f:
            json.dump(messages, f, indent=2)
        flash('Thank you for contacting me! I will get back to you soon.', 'success')
        return redirect(url_for('main.home'))
    return render_template('contact.html', name="Ratul Paul")