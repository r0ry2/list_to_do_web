# To-Do List Web App ✅

# Project Idea  
This project is a simple ((web application for managing tasks To-Do Lists))  
It allows users to:  

1. Add new tasks  
2. Edit any existing tasks  
3. Delete unwanted tasks  
4. Mark tasks as completed  

---

# Database  
- **Database Used**: SQLite  
- **ORM**: SQLAlchemy  

---

# Migration  
i used Flask Migrate commands:  

flask db init
# Create a migrations/ folder to start tracking changes

flask db migrate -m "Add completed field"
# i used to add for completed field

flask db upgrade
# Apply the changes to the database

flask db downgrade
# Roll back to the previous database version
