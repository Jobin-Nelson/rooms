# Rooms

Rooms is a real-time chat application built using Django and Python. It allows users to create chat rooms and communicate with other users in a collaborative environment. The app is being hosted [here](http://jobin1.pythonanywhere.com/)

## Features

- User registration and authentication
- Create and join chat rooms
- Real-time messaging
- Shows recent activities
- Message history within chat rooms
- Profile customization (username, email)
- Search functionality to find rooms

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/Jobin-Nelson/rooms.git
```

2. Change into the project directory:

```
cd rooms
```

3. Create a virtual environment and activate it:

```
python3 -m venv env
source env/bin/activate
```

4. Install the required dependencies:

```
pip install -r requirements.txt
```

5. Apply the database migrations:

```
python manage.py migrate
```

6. Run the development server:

```
python manage.py runserver
```

7. Open your web browser and navigate to `http://localhost:8000` to access the application.

## Configuration

The application uses a default SQLite database for development. If you prefer to use a different database, update the database settings in `settings.py` with the appropriate credentials.

Additionally, you may want to configure other settings such as email backend, static file storage, and secret key according to your deployment environment.

## Usage

1. Create a new account by clicking on the "Register" button on the login page. Fill in the required information and submit the form.

2. Log in with your newly created account or use an existing account.

3. Once logged in, you will be redirected to the home page where you can see a list of available chat rooms, topics and recent activities.

4. Click on a chat room to enter and start messaging. You can also create your own chat room by clicking on the "Create Room" button.

5. Within a chat room, you can send messages in real-time. Users present in the same chat room will see the messages instantly.

6. Customize your profile by clicking on your username at the top right corner of the screen. From there, you can update your username and email.

7. Use the search functionality to find other. You can search by topic or room name

## Contributing

Contributions to the Rooms Chat App are welcome! If you find a bug or want to suggest an enhancement, please open an issue on the GitHub repository.

If you would like to contribute code, fork the repository, create a new branch, and submit a pull request detailing your changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

Rooms App was built with the help of the following resources:

- Django Web Framework: https://www.djangoproject.com/

Special thanks to the developers and contributors of these amazing tools and libraries.
