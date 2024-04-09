# Discord Server for Dev Discussions

[https://discord.gg/TerPNMwM](https://discord.gg/QqSPN5a9)

# Hyperlocal Search

Lets you search Zepto / Instamart / Blinkit all at once

## Getting Started

These instructions will guide you through setting up a copy of the project running on your local machine for development and testing purposes.

### Prerequisites

Python 3.6 or higher
pip (Python package installer)
Ensure Python and pip are installed on your system. You can check their installation by running the following commands in your terminal:

```
python --version
pip --version
```

If you're using a Unix-based system (Linux/Mac), you might need to use `python3` and `pip3` in the commands.

### Setting Up the Environment

#### Create a Virtual Environment

Navigate to your project directory:


```
git clone <repo-url>

cd hyperlocal-search
```

Create a virtual environment named `env` (you can name it anything you like) within the project directory:

```
python -m venv env
```

On Unix-based systems, you might need to use `python3` instead of `python`.

### Activate the Virtual Environment

On Windows:

```
.\env\Scripts\activate
```

On Unix or MacOS:

```
source env/bin/activate
```

After activation, your terminal prompt will change to indicate that you are now working inside the virtual environment. It's now set up to run and develop the project in isolation from the rest of your system.

### Install Required Packages

With the virtual environment activated, install the project dependencies using `pip`:

```
pip install -r requirements.txt
```

This command installs all the packages listed in your `requirements.txt` file, ensuring your project has all its dependencies.

### Running the Application

With your virtual environment activated and dependencies installed, you can start the Flask application using `gunicorn` by running:

```
gunicorn --workers 3 --bind 0.0.0.0:8000 app:app
```

This command starts the application with 3 worker processes, binding it to all network interfaces on port 8000.

### Deactivating the Virtual Environment

When you're done working on the project, you can deactivate the virtual environment by running:

```
deactivate
```

This command will return you to your system's global Python environment.
