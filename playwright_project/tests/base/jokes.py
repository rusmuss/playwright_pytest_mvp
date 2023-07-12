from datetime import datetime
import pytest
import allure
import requests
from pytest_check import check


class Jokes:

    start_test_time: datetime = None

    # fixtures list
    request_session = None

    @pytest.fixture(autouse=True)
    def before_test(self, request_session: requests.Session):
        self.request_session = request_session
        self.start_test_time = datetime.utcnow()

    @allure.step("Get joke")
    def get_joke(self):
        request = self.request_session.get("https://backend-omega-seven.vercel.app/api/getjoke")
        return request.json()[0]

    @allure.step("Check joke parts")
    def check_joke_parts(self, joke_data):
        check.is_not_none(joke_data['question'])
        check.is_not_none(joke_data['punchline'])

