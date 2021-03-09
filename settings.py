from decouple import config

SECRET_KEY = config("SECRET_KEY", default="No Key Found", cast=str )

print("my secret is:" + SECRET_KEY)
