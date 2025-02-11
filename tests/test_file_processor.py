import pytest
import os
import sys

# Ensure `src/` is recognized as a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

# Import FileProcessor
from file_processor import FileProcessor

def test_filename(): # Test if the filename is correctly set and retrieved
    obj = FileProcessor("test.txt")
    assert obj.filename == "test.txt"

def test_is_text_file(): # Test the static method that checks if a file is a text file
    assert FileProcessor.is_text_file("sample.txt") is True
    assert FileProcessor.is_text_file("image.png") is False
    assert FileProcessor.is_text_file("document.pdf") is False
    assert FileProcessor.is_text_file("notes.txt") is True

def test_read_file(tmp_path): # Test reading a file using the generator method
    file = tmp_path / "sample.txt"
    file.write_text("Line 1\nLine 2\nLine 3\n")

    processor = FileProcessor(str(file))

    # Convert generator output to list
    lines = list(processor.read_file())

    assert lines == ["Line 1", "Line 2", "Line 3"]

