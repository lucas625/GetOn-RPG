# GetOn-RPG

Django template project.

- [GetOn-RPG](#geton-rpg)
  - [Team](#team)
  - [Requirements](#requirements)
  - [Installation](#installation)
    - [Windows Installation](#windows-installation)
      - [Windows General Installation](#windows-general-installation)
      - [Windows Front-end Installation](#windows-front-end-installation)
      - [Windows Back-end Installation](#windows-back-end-installation)
  - [Environment Setup](#environment-setup)
    - [Windows Environment Setup](#windows-environment-setup)
      - [Windows Front-end Environment Setup](#windows-front-end-environment-setup)
      - [Windows Back-end Environment Setup](#windows-back-end-environment-setup)
  - [Project Execution](#project-execution)
    - [Windows Execution](#windows-execution)
      - [Front-end Execution](#front-end-execution)
      - [Back-end Execution](#back-end-execution)
  - [Testing](#testing)
    - [Windows Tests](#windows-tests)
      - [Windows Front-end Tests](#windows-front-end-tests)
      - [Windows Back-end Tests](#windows-back-end-tests)
  - [Linting](#linting)
    - [Windows](#windows)
      - [Windows Front-end Linting](#windows-front-end-linting)
      - [Windows Back-end Linting](#windows-back-end-linting)
  - [Code Guides](#code-guides)
    - [General Code Guides](#general-code-guides)
    - [Front-end Code Guides](#front-end-code-guides)
      - [Front-end General Code Guides](#front-end-general-code-guides)
      - [Vue Code Guides](#vue-code-guides)
    - [Back-end Code Guides](#back-end-code-guides)
      - [Back-end General Code Guides](#back-end-general-code-guides)
      - [Django Code Guides](#django-code-guides)

## Team

Project Manager: [Lucas Aurelio](https://github.com/lucas625)
Developer: [Gabriel Moura](https://github.com/bibidam)

## Requirements

- [Python 3.7](https://www.python.org/downloads/)
- [Yarn](https://classic.yarnpkg.com/en/docs/install/#windows-stable)

## Installation

Follow the next steps to install the dependencies.

### Windows Installation

#### Windows General Installation

1. Git:

   - Install [Git](https://git-scm.com/).

2. Project:

   - Clone the project:

        ```$ git clone https://github.com/lucas625/GetOn-RPG.git```

   - Go to project folder:

        ```$ cd GetOn-RPG```

#### Windows Front-end Installation

1. Yarn:

    - Install [Yarn](https://classic.yarnpkg.com/en/docs/install/#windows-stable).

2. Go to front-end folder:

    ```$ cd frontend```

3. Dependencies:

    ```$ yarn install```

4. Return to root folder:

    ```$ cd ..```

#### Windows Back-end Installation

1. Python:

   - Install [Python 3.7](https://www.python.org/downloads/).

2. Go to back-end folder:

    ```$ cd backend```

3. Setup virtualenv:

    ```sh
    # Creates the virtualenv.
    $ python3 -m venv venv

    # Initiates the virtualenv.
    $ venv\Scripts\activate
    ```

4. Install backend dependencies:

    ```sh
    # Updates current virtualenv pip to latest version.
    $ python -m pip install --upgrade pip

    # Install python dependencies.
    $ pip install -r requirements-dev.txt
    ```

5. Return to root folder:

    ```$ cd ..```

## Environment Setup

You must set the environment variables of the project, in order to do that we will be using a `.env` file.

### Windows Environment Setup

#### Windows Front-end Environment Setup

1. Go to front-end folder:

    ```$ cd frontend```

2. Set Vue variables:

    ```sh
    # Sets the environment variable VUE_APP_BACKEND_ADDRESS.
    $ @echo VUE_APP_BACKEND_ADDRESS='http://localhost:8000/'> .env

    # Sets the environment variable VUE_APP_ENVIRONMENT.
    $ @echo VUE_APP_ENVIRONMENT='development'>> .env
    ```

3. Return to root folder:

    ```$ cd ..```

#### Windows Back-end Environment Setup

1. Go to back-end folder:

    ```$ cd backend```

2. Set Django variables:

    ```sh
    # Sets the environment variable ENVIRONMENT.
    $ @echo ENVIRONMENT='development'> .env

    # Sets the environment variable SECRET_KEY.
    $ @echo SECRET_KEY='ANY STRING FOR A SECRET KEY*'>> .env
    ```

3. Run Migrations:

    ```sh
    # Applies all migrations to your local database.
    $ python manage.py migrate
    ```

4. Return to root folder:

    ```$ cd ..```

## Project Execution

After completing the installation of the project, follow the next steps to execute it.
Remember that you will need 2 terminals in the project's root folder and only the one with the **venv** open is able to run the *back-end*.

### Windows Execution

#### Front-end Execution

1. Go to front-end folder:

    ```$ cd frontend```

2. Run Vue server:

    ```$ yarn serve --port 8080```

#### Back-end Execution

1. Go to back-end folder:

    ```$ cd backend```

2. Run Django server:

    ```$ python manage.py runserver 8000```

## Testing

It is important to always test the project before trying to create a pull request, however, we have tools that helps continuous tests such as [travis](https://travis-ci.org/). If you need to test the project locally follow the next steps.

### Windows Tests

#### Windows Front-end Tests

Front-end tests must be executed on the *frontend/* folder.

- Testing with jest:

    ```$ yarn jest```

#### Windows Back-end Tests

Back-end tests must be executed on the *backend* folder.

- Testing with coverage:

    ```$ coverage run manage.py test --no-input --debug-mode -v 2```

  - After testing with coverage you might want to see the report.

    ```$ coverage report```

## Linting

Linters are important to keep the code readable so it's important to always keep your pull requests 100% ok with project's linters.

### Windows

#### Windows Front-end Linting

Front-end linting must be done in the *frontend/* folder.

- Yarn linter:

    ```sh
    # Runs the linter with yarn.
    $ yarn lint --no-fix
    ```

#### Windows Back-end Linting

Back-end linting must be done in the *backend/* folder.

- Python linter:

    ```sh
    # Runs linting with pylint.
    $ pylint --load-plugins=pylint_json2html,pylint_django GetOn-RPG core
    ```

## Code Guides

In order to have a better code quality this projects follows **strictly** the code guide described bellow and also tries to follow the community standards up to a certain point.

### General Code Guides

- Docs:
  
  - All classes must implement its language docs for class function.
  
  - All functions and methods must implement its language docs with clear description of parameters' function, parameters' types, returns' types and function description.

- Separation of concerns:
  
  - There should be at least a "acceptable" level of separation of concerns.

  - Always implement *beans* instead of pure dicts/objects.

  - Any file **should** only contain a single class.

  - Files should be placed in a folder that is exclusive for that type of file, example: `app_name;models/person` and `app_name/models/user`, therefore never use `app_name/person` and `app_name/user`. There are some exceptions to this rule, but those cases should be studied carefully.

- Folder types:
  
  - utils folders must only contain code that need to be imported somewhere else, these files must be named with a `utils` sufix.

  - resources folders must only contain scripts and binary files.

- Security:

  - `.env` files **must not** be added to github.

  - Environment variables should be in caps.

- Classes:

  - Whenever possible use static methods instead of common methods.

### Front-end Code Guides

#### Front-end General Code Guides

- Filenames:

  - Files should be named using `kebab-case`.

#### Vue Code Guides

- Components:

  - Component names must start with `get`.

  - Components should be placed inside the `frontend/src/components` package.

  - Base components should be placed inside the `frontend/src/components/base` package without subdirectories and with `base` as the first word of its name.

  - Base components should not be manually imported.

  - Components should be named using `kebab-case`.

  - Components should be implemented as single file component.
  
- Style:

  - The main style should be acquired from **Vuetify**.

  - If there is a need to specify a custom style for a *component* or *view* it should be declared in the style block of the file with *scoped*.

  - Global styles may be added to the `frontend/src/design` folder inside a related *.scss* file, but these files need to be imported in the *components* or *views* that use them.

- Tests:

  - Tests should be placed in `frontend/src/spec` folder inside the subdirectory related to the file to be tested.

  - Tests should be named as its target file but adding a *.spec* before the final *.js*.

- Vuex:

  - There should only be a single store.

  - The store may contain multiple modules, and those modules should be place within frontend/src/store/modules.

  - Be aware of cases where it is necessary to use v-model with the store as it will result in a commit not enclosed by a Vuex handler, therefore Vuex proposes a solution for this.
  
  - Mutations of a module should be placed inside frontend/src/store/mutation_types.

- Environment Variables

  - Vue environment variables must start with `VUE_APP_`.

### Back-end Code Guides

#### Back-end General Code Guides

- Filenames:

  - Files should be named using `snake_case`.

#### Django Code Guides

- Migrations:

  - Migrations must always be included in github remote.

  - To run migrations use:

    ```sh
    # Create migrations.
    $ python manage.py makemigrations

    # Apply migrations
    $ python manage.py migrate
    ```

- Apps:

  - Django concerns must be splitted into apps.

    - Urls must be splitted by apps.

    - Models must be splitted by apps.

    - Tests must be splitted by apps.

    - Views/Viewsets must be splitted by apps.

  - If a utils or resource file is used only in an app then it must be placed in the app folder.

  - If a utils of resource file is used in more than an app then it must be placed in the `backend/` folder.

  - All apps must be placed in the `backend/` folder.
