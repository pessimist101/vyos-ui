import os

def get_env(key, required=False, or_else=None):
    value = os.environ.get(key)
    if required and or_else:
        print(f"get_env(): for {key}, or_else parameter was ignored because this variable is required")
    if value is not None:
        return value
        if required:
            raise RuntimeError(f"Required environment variable {key} is missing.")
        else:
            return or_else

FLASK_ENV = get_env("FLASK_ENV", or_else="development")
FLASK_APP = get_env("FLASK_APP", or_else="app.py")
FLASK_SECRET_KEY = get_env("FLASK_SECRET_KEY", required=True)