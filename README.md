# Online-Shop

Welcome to **Online-Shop**, a modern e-commerce web application built with Django. This project aims to provide a robust and scalable platform for online shopping, featuring product listings, cart management, user authentication, and order processing.

## Features

- **Product Catalog:** Browse products with detailed descriptions, images, and categories.
- **Shopping Cart:** Add, update, and remove items from your cart.
- **User Accounts:** Register, log in, and manage your profile.
- **Order Management:** Place orders, view order history, and track order status.
- **Admin Dashboard:** Manage products, categories, orders, and users (Django admin).
- **Responsive Design:** A user-friendly interface for both desktop and mobile devices.

## Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite (default), easily switchable to PostgreSQL or MySQL
- **Frontend:** HTML, CSS, Bootstrap (customizable)
- **Authentication:** Django's built-in authentication system
- **Deployment:** Ready for deployment on platforms like Heroku or Vercel

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Soroush-Eghdami/Online-Shop.git
   cd Online-Shop
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

- Register as a new user to start shopping.
- Add products to your cart and proceed to checkout.
- Admin users can add/edit products and manage orders via the admin dashboard.

## Folder Structure

```
Online-Shop/
├── shop/              # Main Django app
├── templates/         # HTML templates
├── static/            # Static files (CSS, JS, images)
├── requirements.txt   # Python dependencies
├── manage.py
└── README.md
```

## Contributing

Contributions are welcome! Please open issues or pull requests for new features, bug fixes, or suggestions.

## License

This project is licensed under the MIT License.

## Author

Made with ❤️ by [Soroush Eghdami](https://github.com/Soroush-Eghdami)

---

