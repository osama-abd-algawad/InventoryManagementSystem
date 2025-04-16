# Inventory Management System

A web-based **Inventory Management System** built with Django MVC to efficiently track stock levels, manage products, and streamline inventory operations. This project showcases full-stack development, database management, and secure user authentication, designed for small to medium-sized businesses.

## Features

- **Product Management**: Add, update, delete, and view products with details like name, quantity, category, and price.
- **Stock Tracking**: Real-time monitoring of inventory levels with low-stock alerts.
- **User Authentication**: Secure login and role-based access (admin vs. user) using Django's authentication system.
- **Responsive UI**: User-friendly interface built with HTML, CSS, and Bootstrap, compatible across devices.
- **Reporting**: Generate summaries of inventory transactions and stock status.
- **Search Functionality**: Quickly find products using a full-text search feature.

## Technologies Used

- **Backend**: Django, Python
- **Database**: SQLite
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Version Control**: Git
- **Deployment**: Heroku (optional; can be adapted for other platforms)
- **Testing**: Django's built-in testing framework

## Prerequisites

- Python 3.8+
- Git
- Virtualenv (recommended for isolated environments)

## Setup Instructions

Follow these steps to run the project locally:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/inventory-management-system.git
   cd inventory-management-system
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**:

   - The project uses SQLite by default, so no additional database setup is required. The database file (`db.sqlite3`) will be created automatically during migrations.

5. **Apply Migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser** (for admin access):

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

   Access the app at `http://localhost:8000`.

## Usage

- **Admin Panel**: Log in as a superuser at `http://localhost:8000/admin` to manage products, users, and categories.
- **User Dashboard**: Access the main interface to view stock, add products, or generate reports.
- **Search**: Use the search bar to find products by name or category.
- **Reports**: Download inventory summaries from the reporting section.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please ensure your code follows the project's coding standards and includes tests where applicable.

## Contact

For questions or collaboration, open an issue on GitHub or reach out via osama0128000@gmail.com.