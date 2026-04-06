# Django API Practical Project

This Django project demonstrates basic CRUD operations using REST API endpoints for student data (name, course, age) and displays them on a web page.

---

## Setup & Run Instructions

Follow these steps to run the project locally:

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/yourproject.git
cd yourproject

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver
