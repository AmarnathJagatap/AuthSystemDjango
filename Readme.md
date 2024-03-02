# Django Rest API Project

This Django project serves as a RESTful API for user authentication using Django Rest Framework and SimpleJWT.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [User Registration](#user-registration)
  - [User Login](#user-login)
  - [Test Token Validity](#test-token-validity)
  - [Refresh Token](#refresh-token)
  - [Logout](#logout)
- [Usage Examples](#usage-examples)

## Project Structure

The project structure is organized as follows:


- **project/authApp/:** Django app for user authentication.
  - **migrations/:** Database migration files.
  - **__init__.py:** Initialization file.
  - **admin.py:** Admin configurations.
  - **apps.py:** App configuration.
  - **models.py:** User and other models.
  - **serializers.py:** API serializers.
  - **tests.py:** Unit tests.
  - **urls.py:** URL patterns for the app.
  - **views.py:** API views and logic.

- **project/authAPISystem/:** Django project settings.
  - **__init__.py:** Initialization file.
  - **asgi.py:** ASGI configuration.
  - **settings.py:** Django project settings.
  - **urls.py:** Main URL patterns for the project.
  - **wsgi.py:** WSGI configuration.

## API Hosting on PythonAnywhere

The API is currently hosted on PythonAnywhere, allowing you to access and test the endpoints. For development purposes, the `DEBUG` setting is set to `True`.

- **API URL:** [https://amarnathjjagatap2001.pythonanywhere.com/](https://amarnathjjagatap2001.pythonanywhere.com/)
- **DEBUG Mode:** True

### Important Note:

- **Debug Mode:** The `DEBUG` setting is enabled for development, providing detailed error pages. Ensure to set `DEBUG` to `False` in a production environment for security reasons.


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AmarnathJagatap/AuthSystemDjango.git
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### User Registration

- **Endpoint:** `/auth/register/`
- **Method:** `POST`
- **Description:** Registers a new user.
- **Registration Curl:**
    ```bash
    curl --location 'https://amarnathjjagatap2001.pythonanywhere.com/auth/register/' \
    --form 'email="email"' \
    --form 'name="user-name"' \
    --form 'password="password"'
    ```

### User Login

- **Endpoint:** `/auth/login/`
- **Method:** `POST`
- **Description:** Authenticates a user and generates access and refresh tokens.
- **Login Curl:**
    ```bash
    curl --location 'https://amarnathjjagatap2001.pythonanywhere.com/auth/login/' \
        --form 'email="email"' \
        --form 'password="password"'
    ```

### Test Token Validity

- **Endpoint:** `/auth/test-token/`
- **Method:** `GET`
- **Description:** Checks the validity of the access token.
- **Token Verification Curl:**
    ```bash
    curl --location 'https://amarnathjjagatap2001.pythonanywhere.com/auth/test-token/' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer access_token'
    ```

### Refresh Token

- **Endpoint:** `/auth/refresh-token/`
- **Method:** `POST`
- **Description:** This endpoint refreshes the access token using the provided refresh token. It verifies whether the refresh token is revoked or not. If revoked, the request will fail, and no new access token will be provided. If the refresh token is valid, a new access token will be generated and returned.

- **Refresh Token Curl:**

  To refresh the access token, use the following `curl` command:

    ```bash
    curl --location 'https://amarnathjjagatap2001.pythonanywhere.com/auth/refresh-token/' \
    --header 'Content-Type: application/json' \
    --form 'refresh_token="refresh_token"'
    ```

  Replace `"refresh_token"` with the actual refresh token obtained during the login process.

**Note:** Ensure that the `Content-Type` header is set to `application/json`, and the refresh token is provided in the form data.

This endpoint is essential for maintaining a continuous authentication session by obtaining new access tokens without requiring the user to log in again.


### Logout

- **Endpoint:** `/auth/logout/`
- **Method:** `POST`
- **Description:** Logs out the user by revoking the refresh token.
- **Logout Curl:**
    ```bash
    curl --location 'https://amarnathjjagatap2001.pythonanywhere.com/auth/logout/' \
        --header 'Authorization: Bearer access_token' \
        --header 'Content-Type: application/json' \
        --form 'refresh_token="refresh_token"'
    ```

This is the README.md file.
