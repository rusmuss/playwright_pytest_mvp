# Playwright pytest mvp
playwright pytest template


#### Install pyenv

```
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
```

To ~/.bashrc add this

```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```


```
sudo apt-get install build-essential
sudo apt-get install python-dev libreadline-dev libbz2-dev libssl-dev libsqlite3-dev libxslt1-dev libxml2-dev libsasl2-dev
sudo apt-get install git
```

Install python version via pyenv 

`pyenv install -v 3.10.2`

Create project env

```
pyenv virtualenv 3.10.2 autotests
pyenv local autotests
python -m pip install --upgrade pip
pip install poetry
```

Install poetry project

``` 
cd playwright_project
poetry install
```

how to add new package:

```
poetry add PACKAGE-NAME
```

Run tests:

```
poetry run pytest playwright_project/tests/*/test_* --alluredir allure-results -n 0 -m "authorization and serial" --disable-warnings
```

To see allure results

```
# install allure commandline (only first time)
npm install -g allure-commandline --save-dev

# run allure report
allure serve allure-results
```
