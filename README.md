# 🕒 EmployeeTracker (Backend)

EmployeeTracker is a backend API built for companies that hire contract-based workers and want to track work hours, activity, and basic performance data — all without micromanagement.

This backend powers features like:

✅ Company accounts to manage workers

👷 Contractor logins to track their work

📊 Work session tracking (time in/time out, tasks)

📁 Basic reporting and data export (planned)

## ⚙️ Tech Stack

FastAPI – Modern, fast (high-performance) Python web framework

SQLAlchemy – ORM for interacting with the database

PostgreSQL (Neon) – Scalable cloud DB

Pydantic – For schema validation

Alembic – For DB migrations

## 📦 Features (Backend)

Company registration/login (JWT-based auth)

Company can:

Create & manage contractor accounts

Assign tasks

View work logs and track time

Contractor can:

Log in

Clock in/out

View assigned tasks

Submit daily work logs

## 🛠️ Setup Instructions

Clone the repo

git clone [https://github.com/yourusername/employeetracker_backend.git](https://github.com/ShadowAdi/emplyoyeeTracker)
cd employeetracker_backend

Create virtual environment

python -m venv env
source env/bin/activate  # Windows: .\env\Scripts\activate

Install dependencies

pip install -r requirements.txt

Set up .env

DATABASE_URL=postgresql+psycopg2://user:password@host:port/dbname
SECRET_KEY=your_jwt_secret


Start the API server

uvicorn app.main:app --reload

🧪 Coming Soon

Work session summaries

Time conflict detection

Multi-admin support per company

## 🤝 Contributing

Suggestions and PRs welcome — if you're passionate about better time management tools for the gig/contractor economy, jump in.

