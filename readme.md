Store API Documentation 

=====================
Link to swagger:
gger:  IP_ADDRESS:8000/api/docs
=====================
POINT THE DB SETTINGS TO YOUR POSTGRES DB
======================
This is a store app API built with Django REST Framework with the following features:
* User authentication and authorization
* Product management
* Order management
* Payment processing
* Inventory management
* Reporting and analytics
Getting Started
---------------
To get started with the store app API, follow these steps:
1.  Clone the repository:
    ```
    git clone httpsth the following features:
* User authentication and authorization
* Product management
* Order management
* Payment processing
* Inventory management

Getting Started
---------------
To get started with the store app API, follow these steps:
1.  Clone the repository:
    ```
    git clone [https://github.com/Raks-Javac/Store-App-v1.git]
    ```
2.  Install the dependencies for debug mode:       
    ```
    pip install -r requirements-dev.txt
    ```
    Install the dependencies for production mode:
    ```
    pip install -r requirements.txt
    ```
3.  Create a new database:
    ```
    python manage.py migrate
    ```
4.  Create a superuser:
    ```
    python manage.py createsuperuser
    ```
5.  Start the development server:
    ```
    python manage.py runserver
    ```     

Endpoints:

Products API:
-------------
*   `GET /api/products/`: Get a list of all products.
*   `GET /api/products/<int:pk>/`: Get a single product by ID.
*   `POST /api/products/`: Create a new product.
*   `PUT /api/products/<int:pk>/`: Update a product by ID.
*   `DELETE /api/products/<int:pk>/`: Delete a product by ID.
Orders API:
-----------
*   `GET /api/orders/`: Get a list of all orders.
*   `GET /api/orders/<int:pk>/`: Get a single order by ID.
*   `POST /api/orders/`: Create a new order.
*   `PUT /api/orders/<int:pk>/`: Update an order by ID.
*   `DELETE /api/orders/<int:pk>/`: Delete an order by ID.          
Carts API:
-----------
*   `GET /api/carts/`: Get a list of all carts.
*   `GET /api/carts/<int:pk>/`: Get a single cart by ID.
*   `POST /api/carts/`: Create a new cart.
*   `PUT /api/carts/<int:pk>/`: Update a cart by ID.
*   `DELETE /api/carts/<int:pk>/`: Delete a cart by ID. 
Payments API:
-----------
*   get-reference
*   initialize-payment
Customers API:
-----------
*   `GET /api/customers/`: Get a list of all customers.
*   `GET /api/customers/<int:pk>/`: Get a single customer by ID.
*   `POST /api/customers/`: Create a new customer.
*   `PUT /api/customers/<int:pk>/`: Update a customer by ID.
*   `DELETE /api/customers/<int:pk>/`: Delete a customer by ID. 

