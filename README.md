# FastAPI Project Setup

## Prerequisites
Ensure you have the following installed:
- Python 3.8+

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Suraj1089/get-five-minute-activites
cd get-five-minute-activites
```

### 2. Create and Activate a Virtual Environment (Optional but Recommended)
```bash
# On macOS/Linux
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the FastAPI Application

### 1. Start the Server
```bash
uvicorn main:app --reload
```
- `main` refers to the filename (main.py)
- `app` refers to the FastAPI instance
- `--reload` enables automatic reload on code changes

### 2. Open API Docs
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

