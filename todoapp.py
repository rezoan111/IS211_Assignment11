from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Temporary fake list for testing the table
todo_items = [
    {'task': 'Buy Milk', 'email': 'test1@example.com', 'priority': 'High'},
    {'task': 'Finish Homework', 'email': 'test2@example.com', 'priority': 'Medium'}
]

@app.route('/')
def show_list():
    # Show the current to do items in the HTML table
    return render_template('index.html', todo_items=todo_items)

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    task = request.form.get('task', '').strip()
    email = request.form.get('email', '').strip()
    priority = request.form.get('priority', '').strip()

    # Check that the email looks valid
    if '@' not in email or '.' not in email:
        return redirect('/')

    # Check that priority is one of the allowed values
    if priority not in ['Low', 'Medium', 'High']:
        return redirect('/')

    # Add the new item if everything is valid
    todo_items.append({
        'task': task,
        'email': email,
        'priority': priority
    })

    # Go back to the main page
    return redirect('/')

if __name__ == '__main__':
    # Run the Flask app
    app.run()
