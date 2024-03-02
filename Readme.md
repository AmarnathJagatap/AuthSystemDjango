# Django Rest API Project

This is a Django project that serves as a RESTful API for user authentication using Django Rest Framework and SimpleJWT.

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
project/
│
├── authAPp/
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
| ├── urls.py
│ └── views.py
│
├── apfauthsystem/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repo.git
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
    curl --location 'http://127.0.0.1:8000/auth/register/' \
    --form 'email="email"' \
    --form 'name="user-name"' \
    --form 'password="password"'

### User Login
- **Endpoint:** `/auth/login/`
- **Method:** `POST`
- **Description:** Authenticates a user and generates access and refresh tokens.
- **Login Curl:**
    curl --location 'http://127.0.0.1:8000/auth/login/' \
        --form 'email="email"' \
        --form 'password="passowrd"'


### Test Token Validity

- **Endpoint:** `/auth/test-token/`
- **Method:** `GET`
- **Description:** Checks the validity of the access token.
- **Token Verificaion Curl:**
    curl --location 'http://127.0.0.1:8000/auth/test-token/' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer access_token'


### Refresh Token

- **Endpoint:** `/auth/refresh-token/`
- **Method:** `POST`
- **Description:** Refreshes the access token using the refresh token.
- **Refresh Token Curl:**
    curl --location 'http://127.0.0.1:8000/auth/refresh-token/' \
    --header 'Content-Type: application/json' \
    --form 'refresh_token="refresh_token"'


### Logout

- **Endpoint:** `/auth/logout/`
- **Method:** `POST`
- **Description:** Logs out the user by revoking the refresh token.
- **Logout Curl:**
    curl --location 'http://127.0.0.1:8000/auth/logout/' \
        --header 'Authorization: Bearer access_token' \
        --header 'Content-Type: application/json' \
        --form 'refresh_token="refresh_token"'


