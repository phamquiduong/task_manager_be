from dotenv import load_dotenv
from dotenv.main import StrPath

from auth.constants import ENV_FILE_DIR


def load_env_from_file(env_dir: StrPath = ENV_FILE_DIR):
    if not load_dotenv(env_dir):
        raise FileNotFoundError("Could not find environment variable")
