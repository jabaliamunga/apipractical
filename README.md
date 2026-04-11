
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


HERE ARE VIEWSET AND ROUTER ENDPOINTS FOR MY DRF LEARNING
| Action   | Method | URL            |
| -------- | ------ | -------------- |
| List     | GET    | `/students/`   |
| Create   | POST   | `/students/`   |
| Retrieve | GET    | `/students/1/` |
| Update   | PUT    | `/students/1/` |
| Delete   | DELETE | `/students/1/` |

VIEWSET handles all CRUD operations automatically it reduces work load of using if request.method == 'POST' etc all CRUD operations can be performed inside a single class basedview linked to a router in urls.py To use a router run from rest_framework.router import Defaultrouter then router= DefaultRouter() #now register url router.register(r'urlname', name of class based viewset) 


