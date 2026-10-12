import os
import sys

# Thêm thư mục gốc của project vào sys.path để import các module ở thư mục cha
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# Import Flask application instance từ sodiem.py
from sodiem import app

# Vercel Serverless Function sẽ tự động nhận diện biến `app` (WSGI callable)
