# csb project

### How to run the application

1. Go to the [flask](https://github.com/janikakalliokoski/csb/tree/main/flask) folder and create Python's virtual environment by running (macOS and Linux)
  ```bash
   python3 -m venv venv
  ```
  or (Windows)
  ```bash
   python -m venv venv
  ```
2. Activate the virtual environment by running (macOS and Linux)
  ```bash
   source venv/bin/activate
  ```
  or (Windows)
  ```bash
   .\venv\Scripts\activate
  ```
  if you get an error like this:
  ```bash
  .\venv\Scripts\Activate : File C:\Users\user\csb\flask\venv\Scripts\Activate.ps1 cannot be loaded because
  running scripts is disabled on this system. For more information, see about_Execution_Policies at
  https:/go.microsoft.com/fwlink/?LinkID=135170.
  At line:1 char:1
  + .\venv\Scripts\Activate
  + ~~~~~~~~~~~~~~~~~~~~~~~
      + CategoryInfo          : SecurityError: (:) [], PSSecurityException
      + FullyQualifiedErrorId : UnauthorizedAccess
  ```
  run Powershell as an administrator and check the current execution policy by running
  ```bash
   Get-ExecutionPolicy
  ```
  The current is most likely set to "Restricted."
  To enable script execution for the current user (which will allow you to activate the virtual environment), run
  ```bash
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```
  Now you should be able to activate the virtual environment in the [flask](https://github.com/janikakalliokoski/csb/tree/main/flask) folder by running
  ```bash
   .\venv\Scripts\activate
  ```
3. Install required packages by running
  ```bash
   pip install -r requirements.txt
  ```
4. Create .env file in the [flask folder](https://github.com/janikakalliokoski/csb/tree/main/flask) and include your secret key
 ```bash
 SECRET_KEY=<your_secret_key>
 ```
6. Start the application by running
  ```bash
  flask run
  ```
  You can log in to admin user with username: admin and password: password or create new users.
