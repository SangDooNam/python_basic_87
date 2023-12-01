# Manipulating the File System

## Description

In this exercise, we will focus on the `os` module to manipulate the directory tree of our file system and we will practice some more with reading and writing files.

##

## Tasks

###

### Task 1

Define a function named `show_data_list` that prints the contents of the directory [src/data/initial](src/data/initial).

- Your result should look like this:

```
todos.txt
jobs.csv
bookmarks.txt
customers.csv
```

###

### Task 2

To avoid manipulating the file system outside of our working folder you will define the constants `ROOT` and `DATA_ROOT`.

> These constants will be used throughout the rest of the exercise.

Define a constant, named `ROOT` that points to the full path of your current script.

Now, define another constant, named `DATA_ROOT` that defines the full path of the `initial` directory, based on the `ROOT`.

In pseudocode:

```
ROOT = detect the current path of the script
DATA_ROOT = ROOT + src/data/initial
```

> You are not allowed to type in the paths. The script should produce the correct answer if you clone this repository in a different location of your file system.
>
> You are not allowed to concatenate strings or use string formatting. Only the methods from the `os` and `os.path` modules are allowed.

- Once defined, print them on the console. Your output should look similar to this(*):

```
/home/DCI/PythonCourse/Python-basics-io-os
/home/DCI/PythonCourse/Python-basics-io-os/src/data/initial
```

> (\*) The exact path will depend on where you cloned this repository and the type of Operating System used.

###

### Task 3

Define a function named `create_data_directories` that takes a list of strings and creates a directory for each one (with the given name) in the directory [src/data/initial](src/data/initial).

The script will only create these directories if they do not exist. If they do, it will output a message saying `The directory {directory} already exists.`

> Use the constant DATA_ROOT to make sure the function will not create directories outside the working directory.

Use the following list to call the function:

```
dirs = ["personal", "work"]
```

- After executing your script, the directory tree should look like this:

```
+ initial
  + personal
  + work
  - todos.txt
  - jobs.csv
  - bookmarks.txt
  - customers.csv
```

- Now, execute the script again, and you should see this message:

```
The directory personal already exists.
The directory work already exists.
```

###

### Task 4

Now write another function named `classify` that takes a dictionary like this one:

```
{
    "directory_name": ["file_name_1", "file_name_2"]
}
```

The function should move each file to the appropriate directory.

> Use the constant DATA_ROOT to make sure the function will not move the files outside the working directory.

Use the following dictionary to test it on the data:

```
categories = {
    "personal": ["todos.txt", "bookmarks.txt"],
    "work": ["customers.csv", "jobs.csv"]
}
```

- Once executed, the directory tree of the `initial` directory should look like this:

```
+ initial
  + personal
    - bookmarks.txt
    - todos.txt
  + work
    - customers.csv
    - jobs.csv
```

###

### Task 5

Now you will produce a basic report about the pending jobs (those with a `status` different than `done`).

This report will be in the form of a CSV, it will be named `pending_jobs.csv` and will be placed in a new directory named `reports` in the `work` directory. The script should create this directory if it does not exist. If it does, it should continue silently.

The report should have the following fields:

- **id**: the id of the job.
- **description**: the description of the job.
- **client**: the **name** of the client.

> Hints
>
> - Remember that it is better to ask forgiveness, than asking permission.
> - You will have to open 3 files: `customers.csv` and `jobs.csv` for reading, and `pending_jobs.csv` for writing.
> - You may want to store first the data about customers in a list and then go through each line in the `jobs.csv` file to search for the customer name and filter those with a status different than `done`.

The `pending_jobs.csv` file should look like this:

```
id,description,client
2,Provide a report,Digital Inc.
3,Review GIT pull requests,Juniper Features

```

The directory tree now should look like this:

```
+ initial
  + personal
    - bookmarks.txt
    - todos.txt
  + work
    + reports
      - pending_jobs.csv
    - customers.csv
    - jobs.csv
```
