from decouple import config

SECRET_KEY = config("SECRET_KEY", default="No Key Found", cast=str )

print("my secret is:" + SECRET_KEY)


#Can cast config environment vars of different types. Ex. cast=bool or cast=int or cast=<type>
#Lines 14+15 show conveting of type to str so it can print a boolean or int

#DEBUG = config('DEBUG', default=False, cast=bool)
#EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)

#print("The DEBUG default value is: " + str(DEBUG))
#print("The EMAIL_PORT default value is: " + str(EMAIL_PORT))
