import allure
import pytest
from playwright_project.tests.base.jokes import Jokes


@pytest.mark.jokes
class TestJokes(Jokes):
    @pytest.mark.serial
    @pytest.mark.jokes
    @allure.title('Test /api/getjoke')
    def test_get_jokes(self):
        joke = self.get_joke()
        self.check_joke_parts(joke_data=joke)
