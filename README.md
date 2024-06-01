For installing dependencies ----     pip install -r requirements.txt

To run the application   ----        uvicorn app.main:app --reload

To test the application ----         pytest


Project structure  :



├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── request_models.py
│   │   └── response_models.py
│   ├── views/
│   │   ├── __init__.py
│   │   └── addition.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── addition_controller.py
│   └── utils/
│       ├── __init__.py
│       └── multiprocessing_utils.py
├── tests/
│   ├── __init__.py
│   ├── test_addition.py
└── requirements.txt

