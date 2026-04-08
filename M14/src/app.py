#M14_L6_HW
# app.py

from flask import Flask, jsonify, request

app = Flask(__name__)


class TaskManager:
   def __init__(self):
       self.tasks = [
           {'id': 1, 'title': 'Buy milk', 'done': False},
           {'id': 2, 'title': 'Learn Pytest', 'done': False}
       ]

   def get_tasks(self):
       return self.tasks

   def create_task(self, title):
       new_task = {'id': len(self.tasks) + 1, 'title': title, 'done': False}
       self.tasks.append(new_task)
       return new_task

   def update_task(self, task_id, data):
       task = next((task for task in self.tasks if task['id'] == task_id), None)
       if task:
           task.update(data)
       return task

   def delete_task(self, task_id):
       task = next((task for task in self.tasks if task['id'] == task_id), None)
       if task:
           self.tasks.remove(task)
           return {'result': True}
       return {'error': 'Task not found'}, 404


task_manager = TaskManager()


@app.route('/tasks', methods=['GET'])
def get_tasks():
   return jsonify({'tasks': task_manager.get_tasks()})


@app.route('/tasks', methods=['POST'])
def create_task():
   data = request.get_json()
   if 'title' not in data:
       return jsonify({'error': 'Title is required'}), 400
   return jsonify(task_manager.create_task(data['title'])), 201


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
   data = request.get_json()
   return jsonify(task_manager.update_task(task_id, data) or {'error': 'Task not found'}), 200


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
   return jsonify(task_manager.delete_task(task_id))


if __name__ == '__main__':
   app.run(debug=True)