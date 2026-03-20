# test_patch_example.py
from unittest.mock import patch, Mock

# --- Тестируемый код (обычно в другом файле) ---
import requests
def get_external_data(item_id):
    # Эта функция делает реальный сетевой запрос
    print(f"\nВызов requests.get для {item_id}...") # Оставим print для демонстрации, что он НЕ выполнится в тесте
    response = requests.get(f"https://api.example.com/items/{item_id}")
    if response.status_code == 200:
        return response.json()
    return None
# --- Конец тестируемого кода ---

#### Использование patch как декоратора

@patch('__main__.requests.get') # Патчим requests.get в текущем модуле, где он используется
def test_get_external_data_with_decorator(mock_requests_get):
    # Настраиваем мок, который будет передан в mock_requests_get
    print("\nЗапуск test_get_external_data_with_decorator")
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Test Item"}
    mock_requests_get.return_value = mock_response

    data = get_external_data(1)

    assert data == {"id": 1, "name": "Test Item"}
    mock_requests_get.assert_called_once_with("https://api.example.com/items/1")

#### Использование patch как контекстного менеджера

def test_get_external_data_with_context_manager():
    print("\nЗапуск test_get_external_data_with_context_manager")
    with patch('__main__.requests.get') as mock_requests_get_cm:
        mock_response = Mock()
        mock_response.status_code = 404
        mock_requests_get_cm.return_value = mock_response

        data = get_external_data(2)

        assert data is None
        mock_requests_get_cm.assert_called_once_with("https://api.example.com/items/2")

#### Патчинг методов объекта с patch.object

# --- Тестируемый код ---
class ReportGenerator:
    def _get_user_stats(self, user_id):
        # Имитация сложного/медленного вызова
        raise NotImplementedError("Не вызывайте реальный метод в тесте!")

    def generate_report(self, user_id):
        stats = self._get_user_stats(user_id)
        return f"User {user_id}: Logins - {stats['logins']}, Spent - {stats['spent']}"
# --- Конец тестируемого кода ---

@patch.object(ReportGenerator, '_get_user_stats') # Патчим метод конкретного класса
def test_generate_report_patches_object_method(mock_get_stats):
    print("\nЗапуск test_generate_report_patches_object_method")
    mock_get_stats.return_value = {"logins": 10, "spent": 50} # Упрощенные данные для теста

    generator = ReportGenerator()
    report = generator.generate_report(user_id=123)

    assert report == "User 123: Logins - 10, Spent - 50"
    mock_get_stats.assert_called_once_with(123)
