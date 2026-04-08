#M14_L6_HW

import pytest
import sys
import os
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, task_manager

API_URL = 'http://localhost:5000/tasks'


@pytest.fixture
def client():
   with app.test_client() as client:
       yield client


def test_get_tasks(client):
   response = client.get(API_URL)
   assert response.status_code == 200
   assert isinstance(response.json['tasks'], list)


@pytest.mark.parametrize("task_input, expected_status, expected_title", [
   ({'title': 'New Task 1'}, 201, 'New Task 1'),
   ({'title': 'Новая задача 2'}, 201, 'Новая задача 2'),
])
@patch('app.task_manager.create_task')  # Мокирование
def test_create_task(mock_create_task, client, task_input, expected_status, expected_title):
   mock_create_task.return_value = {'id': 3, 'title': expected_title, 'done': False}  # Определяем return_value

   response = client.post(API_URL, json=task_input)
   assert response.status_code == expected_status
   assert response.json['title'] == expected_title
   mock_create_task.assert_called_once_with(expected_title)


@patch('app.task_manager.create_task')
def test_create_task_invalid_input(mock_create_task, client):
   mock_create_task.side_effect = ValueError('Invalid input')

   # Сброс списка задач перед выполнением теста
   task_manager.tasks.clear()

   response = client.post(API_URL, json={})
   assert response.status_code == 400
   assert 'error' in response.json
   assert not task_manager.tasks
   mock_create_task.assert_not_called()