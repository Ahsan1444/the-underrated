import pytest
import os
import sys

# Ensure `src/` is recognized as a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

# Import FileProcessor
from file_processor import FileProcessor