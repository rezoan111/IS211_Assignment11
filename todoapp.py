from flask import Flask, render_template

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

if __name__ == '__main__':
    # Run the Flask app
    app.run()
