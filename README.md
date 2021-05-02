# [TremendoDjango](https://microblog.pythonanywhere.com/login)
This is a micro blogging platform for teachers and students interactions. It is completely verified and safe for registration and email verifications too.
The various features included in this site are:
1) It is completely built and have a good ability to register user with their email verifications.
2) User can login to their dashboard and it also supports forgot password facility.
3) On dashboard user can edit their details of profile.
4) Separate dashboards for teachers and students.
5) Models and DB are also well designed by taking care of relationships.

This site is hosted using PythonAnywhere hosting services for three months from today.
Link to site is in the title above.

# Note:
1) The email verification and forgot password concepts requires an temp testing email. So in site it is not working through email. If you want to verify the user than you have to do it manually by going to admin board of django [here](https://microblog.pythonanywhere.com/admin/) and then you have to login using password :harsh and username:harsh.
  Then you can verify the user and can continue login.
2) To run this site locally follow these steps:
  a) Clone the repo.
  b) Install pip and python.
  c) run the command (without quotes) "pip install -r requirements.txt"
  d) activate the virtual environment.
  e) in settings.py file make the necessary changes like addition of test email and password.
  f) run the server "python manage.py runserver"
