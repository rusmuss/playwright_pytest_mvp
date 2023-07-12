import pathlib
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

base_path = pathlib.Path(__file__).parent.absolute()
config_path = base_path / ".env"
config = Config(str(config_path))


TITLE = config('TITLE', cast=str, default="Sign in to GitHub · GitHub")
HEADLESS_MODE = config('HEADLESS_MODE', cast=bool, default=True)
SITE_URL = config('SITE_URL', cast=str, default="https://github.com/login")
BROWSER_LIST = config('BROWSER_LIST', cast=CommaSeparatedStrings, default="chromium,firefox,webkit")
