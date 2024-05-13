# ecom-ripoff
A ripoff of my ecommerce app. main code is private, you can contact me for the main code.  

**E-Commerce App Documentation**
## Table of Contents
- Introduction
- Features
- Technologies Used
- Installation
- Usage
- Frontend
    - Real-time Notifications
    - API Requests
    - Libraries and Frameworks
    - State Management
    - Admin Pages
    - User Ratings
- Backend
    - APIs
    - Authentication and Authorization
    - Caching
- Testing  

**Introduction**

Welcome to my E-Commerce app, a platform where users can buy and sell goods. The app offers real-time updates for buyers and sellers, with features such as following favorite sellers, instant notifications, and detailed user and sales statistics. This documentation provides a comprehensive guide to understanding and using the app.  

**Features**
- User registration and authentication
- Real-time notifications for buyers and sellers.
- Following favorite sellers for updates.
- Cart management with Redux Toolkit.
- Admin pages with sales, users, and goods statistics.
- MUI Datagrid for tabular representation of goods.
- Seller ratings and reviews.
- Password reset via email.  

**Technologies Used**  

**Frontend**: React, Socket.IO, Axios, Fetch, React Query, Swiper, React Chart.js, React Redux Toolkit, Context API.  

**Backend**: Django, Django Rest Framework (DRF), CORS, REST framework simplejwt  

**Installation**
1. Clone the repository:
> git clone https://github.com/your-username/ecommerce-app.git
2. Install dependencies:

   `cd ecommerce-app`  
   
   *Install frontend dependencies*  
   `npm install`  
   
   *Install backend dependencies*  
   `pip install -r requirements.txt`


*Configure backend settings:*

- Set up the database and run migrations:
  
  `python manage.py migrate`

- Create a superuser for admin access:  
  `python manage.py createsuperuser`

*Configure frontend settings:*

- Set up environment variables and configuration files as required.  
    
**Usage**  

To run the app, use the following commands:  

- Start backend server  
    `python manage.py runserver`

- Start frontend  

     `npm start`

# Frontend

 **Real-time Notifications**
 
The app leverages Socket.IO for real-time notifications. Buyers receive updates when their favorite sellers upload new goods, and sellers get instant notifications when they are followed.

**API Requests**  

API requests are made using Axios, Fetch, and React Query. This demonstrates a versatile knowledge of different approaches to handling API requests.

**Libraries and Frameworks**  

The frontend utilizes Swiper and React Chart.js for enhanced user experience. React Redux Toolkit manages the shopping cart, while Context API is employed for data sharing within components.

**State Management**  

The state management includes the use of React Redux Toolkit for the cart and Context API for other data sharing within components. Additionally, useMemo and useCallback are employed for optimizing performance.

**Admin Pages**  

Admins have access to specialized pages for blocking users, deleting goods, and viewing detailed statistics on sales, users, and goods per month. This functionality is restricted to users with the necessary permissions.

**User Ratings**  

Sellers can be rated by users, with their ratings visible to all. A higher number of stars indicates a higher rating. Sellers can also view their critical and positive ratings.

# Backend
**APIs**
The backend is built with Django and DRF, providing APIs for various functionalities. The endpoints are structured to handle user registration, goods management, user statistics, and more.

**Authentication and Authorization**  

Authentication is handled using REST framework simplejwt, ensuring secure access to the app. Authorization is implemented to allow only admins access to specific functionalities.

**Caching**  

Caching is implemented to improve performance, and certain views are cached for better response times.

**Testing**  

Testing is an integral part of the development process. We are actively working on creating test suites for both the Django backend and the React frontend. Detailed documentation on testing procedures will be provided soon.

*Feel free to reach out if you have any questions or need further assistance!*





