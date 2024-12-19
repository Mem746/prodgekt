from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = 'your_secret_key'
@app.route('/')
def tasks():
    tasks = ['Task 1', 'Task 2', 'Task 3']
    return render_template('tasks.html', tasks=tasks)
@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks = ['Task 1', 'Task 2', 'Task 3']
    tasks.append(task)
    flash('Task added successfully!')
    return redirect(url_for('tasks'))
