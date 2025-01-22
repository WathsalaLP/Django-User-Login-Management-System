# User Login Management System

This project is a lightweight and efficient **User Login Management System** built using **Django**, **Bootstrap**, and **Supabase**. It is designed to handle essential user authentication and management functionalities with a clean and responsive interface.

## Features
- User registration and login
- Secure authentication with Supabase
- User profile management
- Responsive front-end using Bootstrap
- Scalable and easy-to-extend architecture

- **Role-Based Redirection**:
  - `Normal User`: Redirected to the Home page.
  - `Hotel Admin`: Redirected to the Hotel Admin Dashboard.
  - `Main Admin`: Redirected to the Main Admin Dashboard.
  
- **User Authentication**:
  - Secure signup and login using Django's built-in authentication system.
  - Password validation and hashed storage.
  
- **Bootstrap Integration**:
  - Clean and responsive user interface.

## Technologies Used
- **Django**: Backend framework for handling logic and server-side processing.
- **Bootstrap**: Front-end framework for responsive design.
- **Supabase**: Authentication and database management.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd user-login-management-system
   ```

3. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Configure the Supabase settings:
   - Add your Supabase project URL and API key to the settings file.

6. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Open your browser and navigate to `http://127.0.0.1:8000`.

## Usage
- Register a new account.
- Log in using your credentials.
- Access and update your user profile.

## Contribution
Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Feel free to reach out with any questions or suggestions!

