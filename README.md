# Fibonacci Api Microservice (RESTFul)

Example project to implement a Fibonacci API microservice.

Getting Started

$ git clone https://github.com/davidebruno/fibonacci_rest_api.git
$ cd fibonacci_rest_api

Then proceed to create a local virtual environment (useful to manage independently packages dependencies)

$ cd fibonacci_rest_api
$ python -m venv envfoldername --no-site-packages # (for info: https://docs.python.org/3/library/venv.html)
$ ./envfoldername/bin/activate                    # to ensure you are using the correct virtualenv python
$ pip install --upgrade pip
$ pip install -r requirements.txt                 # this command installs the packages specific for the project into the project venv 

Deployment

For deployment is suggested to use Docker as it is scalable and machine independent (the project is not yet setup for it, wip)

Documentation

Documentation for the project could be generated using Sphinx (not implemented)


Testing

Run the tests with nosetests

$ cd fibonacci_rest_api
$ nosetests
nosetests
......
Ran 6 tests in 0.129s

Run the Microservice

To run the service, after having followed the steps referred in the Getting Started section

$ cd fibonacci_rest_api
$ python main.py

You can use curl to interact with the API or open your browser and paste the url below

$ curl http://localhost:5000/fibonacci/18
The response is:
[
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597
]

Technology Stack

Python 3.6.5 - All components are build in Python
Flask & Flask-RESTful- Web application framework suitable for creating microservices in Python.
Docker - Container technology to create simple and machine independent deployments. (To be implemented)
Nose - Unit testing framework.
Sphinx - Could be used to generated documentation
