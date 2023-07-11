#!/bin/bash

poetry run pytest playwright_project/tests/*/test_* --alluredir docker-allure-results -n 0 -m "authorization and serial" --disable-warnings

#poetry run pytest tests/*/test_* --alluredir docker-allure-results -n 0 -m "admin_panel and smoke and serial" --disable-warnings
#poetry run pytest tests/*/test_* --alluredir docker-allure-results -n 4 -m "admin_panel and smoke and not serial" --disable-warnings

