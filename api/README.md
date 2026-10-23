# API

Python scripts that use a REST API to gather employee data and export it to
different formats (standard output, CSV and JSON). They use the free
[JSONPlaceholder](https://jsonplaceholder.typicode.com) API, which provides
fake users and TODO lists for practice.

## Background

Bash is fine for many things, but it gets messy and inefficient for tasks like
talking to an API and reshaping data. Python is a better fit, so these scripts
are written in Python 3.

## Learning Objectives

- What Bash scripting should not be used for
- What an API is
- What a REST API is
- What microservices are
- What the CSV format is
- What the JSON format is
- Pythonic naming style for packages, modules, classes, variables, functions
  and constants
- The significance of CapWords (CamelCase) in Python

## Requirements

- Ubuntu 14.04 LTS with python3 (version 3.4.3)
- The `requests` module: `pip3 install requests`
- Allowed editors: `vi`, `vim`, `emacs`
- All files end with a new line
- The first line of every script is `#!/usr/bin/python3`
- Imports are in alphabetical order
- Code follows the PEP 8 style (check with `pycodestyle`)
- All files are executable (`chmod +x *.py`)
- Every module has a docstring
- Dictionary values are accessed with `get`
- Code does not run when imported (`if __name__ == "__main__":`)

## Files

| File | Description |
|------|-------------|
| `0-gather_data_from_an_API.py` | Prints an employee's TODO list progress |
| `1-export_to_CSV.py` | Exports an employee's tasks to `USER_ID.csv` |
| `2-export_to_JSON.py` | Exports an employee's tasks to `USER_ID.json` |
| `3-dictionary_of_list_of_dictionaries.py` | Exports every employee's tasks to `todo_all_employees.json` |

## Usage

Scripts 0, 1 and 2 need one argument: the employee ID (an integer).
Script 3 needs no argument.

### 0-gather_data_from_an_API.py

```
$ ./0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
	 distinctio vitae autem nihil ut molestias quo
	 voluptas quo tenetur perspiciatis explicabo natus
	 ...
```

Each completed task is printed with one tab and one space before the title.

### 1-export_to_CSV.py

```
$ ./1-export_to_CSV.py 2
$ cat 2.csv
"2","Antonette","False","suscipit repellat esse quibusdam voluptatem incidunt"
"2","Antonette","True","distinctio vitae autem nihil ut molestias quo"
...
```

Format: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`

### 2-export_to_JSON.py

```
$ ./2-export_to_JSON.py 2
$ cat 2.json
{"2": [{"task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false, "username": "Antonette"}, ...]}
```

Format: `{"USER_ID": [{"task": "TASK_TITLE", "completed": STATUS, "username": "USERNAME"}, ...]}`

### 3-dictionary_of_list_of_dictionaries.py

```
$ ./3-dictionary_of_list_of_dictionaries.py
$ cat todo_all_employees.json
{"1": [{"username": "Bret", "task": "delectus aut autem", "completed": false}, ...], "2": [...], ...}
```

Format: `{"USER_ID": [{"username": "USERNAME", "task": "TASK_TITLE", "completed": STATUS}, ...], ...}`

## Author
joshua hotay - [GitHub](https://github.com/hotay11)
