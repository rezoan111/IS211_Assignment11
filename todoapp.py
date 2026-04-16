from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)

# Store all to do items here
todo_items = []


def is_valid_email(email):
    # Simple email check
    pattern = r'^[^@\s]+@[^@\s]+\.[^@\s]+$'
    return re.match(pattern, email) is not None


@app.route('/')
def show_list():
    # Show the main page with the current to do items
    return render_template('index.html', todo_items=todo_items)


@app.route('/submit', methods=['POST'])
def submit():
    # Get the form values
    task = request.form.get('task', '').strip()
    email = request.form.get('email', '').strip()
    priority = request.form.get('priority', '').strip()

    # Validate the data
    if task == '':
        return redirect('/')

    if not is_valid_email(email):
        return redirect('/')

    if priority not in ['Low', 'Medium', 'High']:
        return redirect('/')

    # Add the new item to the list
    todo_items.append({
        'task': task,
        'email': email,
        'priority': priority
    })

    # Go back to the main page
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    # Clear all items from the list
    todo_items.clear()

    # Go back to the main page
    return redirect('/')


if __name__ == '__main__':
    # Run the Flask app
    app.run()
