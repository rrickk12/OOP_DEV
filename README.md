
# OOP-DEV Flask Application

## Description

OOP-DEV is a Flask-based web application demonstrating Object-Oriented Programming (OOP) principles, RESTful API design, and CRUD operations. It's designed as an educational tool to showcase best practices in Python web development, including use of design patterns, ORM with SQLAlchemy, and structured project organization.

## Features

- **RESTful API**: Implements CRUD operations for User entities.
- **OOP Principles**: Demonstrates inheritance, encapsulation, polymorphism, and more.
- **Design Patterns**: Includes examples of Factory, Builder, and Template patterns.
- **Flask SQLAlchemy**: Utilizes ORM for database operations.
- **Environment Configuration**: Manages configurations through environment variables.

## Installation

To get started with this project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/OOP-DEV.git
cd OOP-DEV
pip install -r requirements.txt
```

## Running the Application

To run the application, use the following command:

```bash
flask run
```

This will start a local development server on `http://localhost:5000`.

## API Usage

### Get All Users

**Request:**

`GET /users`

**Response:**

```json
[
    {
        "id": 1,
        "name": "John Doe",
        "age": 30,
        "email": "johndoe@example.com"
    },
    ...
]
```

### Create a New User

**Request:**

`POST /user`

**Payload:**

```json
{
    "name": "Jane Doe",
    "age": 25,
    "email": "janedoe@example.com"
}
```

**Response:**

```json
{
    "id": 2,
    "name": "Jane Doe",
    "age": 25,
    "email": "janedoe@example.com"
}
```
