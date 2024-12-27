# Django Project Setup

## Requirements

- Python 3.8+
- pip
- Virtualenv (optional but recommended)

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone git@github.com:Robben1972/CustomAdmin.git
   cd CustomAdmin
   ```

2. **Create a virtual environment (optional)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```
5. **Create Super User**:
  ```bash
  python manage.py createsuperuser
  ```
6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000/admin).
