# Wedding Gallery API

Basic endpoints to receive an image then send to moderation. Once approved, the image will be published to the public gallery.

## Installation

* Copy ```wedding/settings.py.dist``` to ```wedding/settings.py``` then update the variables to your environment. 

* Then create a virtual env and install all the libraries:

```
$ mkvirtualenv -p /usr/bin/python3.9 wedding
$ workon wedding
$ pip install -r requirements.txt
```

* Run database migrations:
```
$ ./manage.py migrate
```

* Start development server:
```
$ ./manage.py runserver
```

## API reference

The API reference is available at: http://localhost:8080/reference

## Unit Testing
There are some tests included. To run, execute:

```
$ ./manage.py test                                                                                                                                                                                                           1 ↵ 
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
----------------------------------------------------------------------
Ran 1 test in 3.175s

OK
Destroying test database for alias 'default'...

```


## S3 integration

To use S3 integration, you should configure your IAM Keys in the settings.py file


## Requirements:
- Python version >= 3.8.7

