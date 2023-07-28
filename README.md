# csb project

### How to run the application

1. Go to the [project folder](https://github.com/janikakalliokoski/csb/tree/main/flask) and create Python's virtual environment by running (macOS and Linux)
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
   venv\Scripts\activate
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
