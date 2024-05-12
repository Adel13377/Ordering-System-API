# Ordering-System-API
- **Overview**
- **Technologies Used**
- **Installation and setup**
- **Installation and setup (Using Docker)**
- **Deployed App**
- **Features**

## Overview
A simplified Order Processing System API for an online store. The system handles order processing, including stock validation, payment processing (integrated with a mock payment gateway), and sending order confirmation emails to customers.



## Technologies Used
- **Flask**: Python web framework for building the application.
- **Flask-Restful**: Extension for building REST APIs in Flask.
- **SQLAlchemy**: Python SQL toolkit and Object-Relational Mapping (ORM) library.
- **SQLite**: Database management system used for storing data.
- **Stripe API**: Used for payment processing.
- **Google SMTP**: Used for sending order confirmation emails.
- **Docker**: Containerization platform for packaging and deploying the application.
- **Postman**: API development and testing tool.
- **PythonAnywhere**: Cloud platform as a service for hosting and deploying web applications.

## Installation and Setup
1. Clone the repository to your local machine using git or simply download the code base.<br>`git clone https://github.com/your_username/your_repository`
2. Create `.env` file to store your Stripe API environment variables, for simplicity you can use my testing APIs
   1. Create a file named `.env`.
   2. Copy paste the following environment variables.<br>`STRIPE_PUBLISHABLE_KEY = pk_test_51PFLVnJx9Vg564EumWmr5ZgfNkdLcD2cbVHue5dxHOyv5FUK1IniUFyqvivXYhjtxjE7Gqaxq5IKh0tJxCrJiJXD00zzjMYFSQ` <br>
`STRIPE_SECRET_KEY = sk_test_51PFLVnJx9Vg564EuCrORbcMQ09Ml2tQ40dPW5KXyP3lt52V9TtZsW9U3Ip9HQb17FmzXeC4d3AhHwGok7sfRtzAx00Kix0pYg3`
4. Being inside the project directory, Create a virtual environment.<br>`python -m venv venv`
5. Activate the virtual environment.<br>`venv/Scripts/activate` <br>
   *If you have problems trying to activate the virtual environment using the last command, try using that command first then trying again <br> `set-Executionpolicy -scope process -Executionpolicy Bypass 
`*
7. After activating the venv, Install the required dependencies using pip.<br>`pip install -r requirements.txt`
8. Run the Flask Application <br> `flask run`
9. Follow the Postman APIs Documentation below to test the APIs endpoints in your localhost <br> [https://documenter.getpostman.com/view/34868263/2sA3JNaL2v](https://documenter.getpostman.com/view/34868263/2sA3JNaL2v)

## Installation and Setup (Using Docker)
1. Pull the system Image from dockerhub [Link](https://hub.docker.com/r/adel1337/ordersystem).<br>`docker pull adel1337/ordersystem:v1.0`
2. Create/Run the Container:.<br>`docker run --name order-system-container -p 5000:5000 adel1337/ordersystem:v1.0`
3. Follow the Postman APIs Documentation below to test the APIs endpoints in your localhost <br> [https://documenter.getpostman.com/view/34868263/2sA3JNaL2v](https://documenter.getpostman.com/view/34868263/2sA3JNaL2v)
   <br> <br>***Note that you can create the Image yourself instead of pulling it by using Dockerfile and use it to create/run a container.***


## Deployed App:
  [https://orderingsystem.pythonanywhere.com/](https://orderingsystem.pythonanywhere.com/) 
  #### Postman APIs Documentation to test the deployed API server directly
  [https://documenter.getpostman.com/view/34868263/2sA3JNaKxV#intro](https://documenter.getpostman.com/view/34868263/2sA3JNaKxV#intro)
  

## Features

1. **Stock Management:** Implement functionality to validate the availability of products in the store's inventory when placing an order. Ensure that the system updates the stock count accordingly after each successful order.✅
2. **Payment Processing:** Integrate with a mock payment gateway to simulate payment processing. Upon successful payment, mark the order as paid and proceed with order fulfillment.✅
3. **Order Confirmation Emails:** Develop a feature to send order confirmation emails to customers after a successful purchase. The email should include details such as the order ID, purchased items, and total amount.✅
4. **Error Handling:** Implement error handling to gracefully manage any issues that may occur during the order processing flow, such as stock unavailability or payment failures.✅
5. **Documentation:** Provide clear and concise documentation on how to set up and run the Order Processing System.✅
6. **Containerization:** Dockerize the Order Processing System by creating a Dockerfile to package the application into a container. Ensure that the Dockerfile is included in the repository.✅
7. **Repository Integration:** Push the built Docker image to a container registry/repository of your choice (e.g., Docker Hub, GitHub Container Registry).✅

### Bonus
1. **Customization:** Allow customization of email templates for order confirmation emails.✅
2. **Deployment:** Deploy the Order Processing System to a cloud platform such as Heroku or AWS.✅
