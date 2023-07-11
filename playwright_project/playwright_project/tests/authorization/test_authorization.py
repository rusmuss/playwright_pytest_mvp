import allure
import pytest
# import pytest_check as check
from playwright_project.tests.base.auth import Auth


@pytest.mark.authorization
class TestAuthorization(Auth):
    @pytest.mark.parametrize("username, password", [
        ('0', '0'),
        ("1231312312321311231231232", "dsadlajsdkajsdkas3213213j"),
    ]) # будет 2 запуска с разными параметрами
    @pytest.mark.serial # маркируем как тест, который нужно запускать последовательно
    @allure.title('Неуспешная авторизация с некорректными данными')
    def test_fail_authorization(self, username, password):
        self.check_title()
        self.check_invalid_creds(user=username, password=password)
