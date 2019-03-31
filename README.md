# Sulur Website

Sulur Website is a project which created by Tech Evengelist Team in Sulur Dreamwork. This website contains some profile of Sulur Dreamwork and also will be a medium for Sulur Dreamwork to share ideas, projects, and events.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

- Git. Download the installer [here](https://git-scm.com/downloads)
- Python-3.7.x. Download the installer [here](https://www.python.org/downloads/)
- PostgreSQL Version 11. Download the installer [here](https://www.postgresql.org/download/)

### Project Installation

A step by step series of examples that tell you how to get a development env running

Open terminal for macOS and linux or Command Prompt for Windows

1. If your python version is not >= 3.4 for Python3 or >= 2.7.9 for Python2, Install 'pip' package manager by running this command

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

and

```
python get-pip.py
```

2. Clone this repositories by download the zip file [here](https://github.com/sulur/sulur) or run this command in your git bash.

```
git clone https://github.com/sulur/sulur.git
```

3. Open terminal or command prompt and Install virtualenv by running this command (add sudo before the command if you are Mac or Linux user)

```
 pip install virtualenv
```

4. activate the virtualenv by run this command

```
 source /path/to/ENV/bin/activate (Mac OS and Linux) or \path\to\env\Scripts\activate (Windows)
```

5. In your terminal or command prompt, change directory to the project folder

6. Install all requirements stuff by run this command:

```
 pip install -r requirements.txt
```

### Database Setup

1. Open PostgreSQL and start the connection

2. Open command prompt and run this command

```
psql -U postgres
```

3. Create new user for postgres server by run this command

```
CREATE USER yourcustomusername WITH PASSWORD 'yourcustompassword';
```

4. Create Database by run this command

```
CREATE DATABASE yourcustomdatabasename
```

5. Grant privileges by run this command

```
GRANT ALL PRIVILEGES ON DATABASE yourcustomdatabasename to yourcustomusername;
```

6. run this command:

```
\q
```

7. login to postgres again with your custom user by running this command

```
psql -U customusername
```

8. if login is succeed, run this command:

```
\l
```

9. the setup is succed when you see your custom user has access in the custom database.

10. contact the coordinator of TE team in Sulur for the next required setup before running the tests

## Running the tests

1. activate the virutalenv by running this command

```
 source /path/to/ENV/bin/activate (Mac OS and Linux) or \path\to\env\Scripts\activate (Windows)
```

2. virtualenv is activated when you see (ENV or other words) at the beginning of command line

3. to run the test, type this command and enter

```
python manage.py runserver
```

### this is the end of document
