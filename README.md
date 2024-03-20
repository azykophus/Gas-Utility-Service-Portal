# Gas Utility Service Portal

The Gas Utility Service Portal is a Django-based web application designed to streamline the process of managing service requests for both customers and service providers in the gas utility industry. This platform allows customers to submit service requests online, track the status of their requests, and view their account information. Simultaneously, it equips customer support representatives with tools to efficiently manage and respond to service requests, improving overall service quality and customer satisfaction.

## Features

- **Customer Account Management**: Users can register, login, and manage their profiles.
- **Service Request Submission**: Customers can submit service requests, detailing the nature of the issue and attaching relevant files.
- **Request Tracking**: Customers can track the status of their service requests in real-time, from submission through to resolution.
- **Admin Dashboard**: An admin interface for customer support representatives to view, manage, and resolve service requests.
- **Responsive Design**: Accessible from various devices, ensuring a seamless user experience across platforms.

## Getting Started

These instructions will guide you through setting up and running the Gas Utility Service Portal on your local machine for development and testing purposes.

### Prerequisites

- Python (3.8 or later)
- Django (3.2 or later)
- Additional dependencies listed in `requirements.txt`

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/azykophus/gas-utility-service-portal.git
    cd gas-utility-service-portal
    ```

2. **Create and Activate a Virtual Environment**

    - For Unix/macOS:
    
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

    - For Windows:
    
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

3. **Install Required Packages**

    ```bash
    pip install -r requirements.txt
    ```

4. **Migrate the Database**

    ```bash
    python manage.py migrate
    ```

5. **Create an Admin User**

    ```bash
    python manage.py createsuperuser
    ```
    
    Follow the prompts to set up an admin username, email, and password.

6. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```
    
    Visit `http://127.0.0.1:8000/` in your web browser to view the application.

### Usage

- **Customer Use**: Navigate to `http://127.0.0.1:8000/` to register or login. Once logged in, you can submit new service requests and track existing ones through the dashboard.
- **Admin Use**: Log in to the admin panel at `http://127.0.0.1:8000/admin` using your superuser credentials. Here, you can manage users, view, and resolve service requests.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for more information.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- Django Documentation
- Bootstrap for the responsive design
- All contributors and supporters of the project
