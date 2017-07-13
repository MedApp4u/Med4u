# DoctorsWebApp

An Easy-to-Use but useful Web Application where end-users can register free of charge and have their Medical Records sorted. Other functionalites include Finding Doctors by location, speciality and booking appointments without having to make a ring!

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The total list of requirements is [here](https://github.com/MedicalAppInfibeam/DoctorsWebApp/blob/master/requirements.txt). Make sure you have all of these within your virtual envrionment.

### Installing

* Install all the requirements within your virtual envrionment.
* Clone this repository from [here](https://github.com/MedicalAppInfibeam/DoctorsWebApp.git).

## Deployment

### Local Server

* Activate your Virtual Environment
* Move to your project directory
* Within your terminal type `python manage.py runserver`
* The server will be hosted on `http://localhost:8000/`

### Staging Server

* You must first go through the [docs](https://cloud.google.com/python/django/appengine). We have  most of the required files here in this repo. Other than these you must have a static folder and a virtualenv folder in the root directory.
* Download and install the Google Cloud SDK.
* Move straight to 'Run the app on your local computer'. The second point is very important as it uploads the Third-Party APIs to the App Engine. However, don't forget to replace 'lib' with 'virtualenv' and 'requirements-vendor.txt' to 'requirements.txt'.
* Move on to 'Deploy the app to the App Engine standard environment'. Once you finish with this point you will have the Django App up and running on your registered URL.
* Our staging server is on [https://med-4-u.appspot.com](https://med-4-u.appspot.com)

## Built With

* [Django](https://docs.djangoproject.com/en/1.11/) - The web framework used
* [Google App Engine](https://cloud.google.com/appengine/) - For deploying to the Staging Server

## Contributing

Please read [CONTRIBUTING.md](https://github.com/MedicalAppInfibeam/DoctorsWebApp/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/MedicalAppInfibeam/DoctorsWebApp/blob/master/LICENSE) file for details.

## Acknowledgments

See also the list of [contributors](https://github.com/MedicalAppInfibeam/DoctorsWebApp/graphs/contributors) who participated in this project.
    
     
