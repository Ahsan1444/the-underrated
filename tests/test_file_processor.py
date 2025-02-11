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

def test_read_empty_file(tmp_path): # Test reading an empty file
    file = tmp_path / "empty.txt"
    file.write_text("")  # Create an empty file

    processor = FileProcessor(str(file))

    # Convert generator output to list
    lines = list(processor.read_file())

    assert lines == []  # Should return an empty list

def test_invalid_file_read(): # Test reading a non-existent file
    processor = FileProcessor("non_existent_file.txt")

    with pytest.raises(FileNotFoundError):
        list(processor.read_file())  # Attempt to read a missing file should raise an error

def test_add_operator(): # Test the __add__ dunder method
    fp1 = FileProcessor("sample1.txt")
    fp2 = FileProcessor("sample2.txt")
    combined_fp = fp1 + fp2  # This should create a new FileProcessor with concatenated names

    assert combined_fp.filename == "sample1.txt_sample2.txt"  # Correct expected output

def test_concat_files(tmp_path): # Test file concatenation
    file1 = tmp_path / "sample1.txt"
    file2 = tmp_path / "sample2.txt"
    output_file = tmp_path / "output.txt"

    # Write content to temporary files
    file1.write_text("Hello\n")
    file2.write_text("World\n")

    processor = FileProcessor(str(file1))
    processor.concat_files(str(file2), str(output_file))

    # Read the output file and compare expected content
    expected_output = "Hello\nWorld"  # No extra newline at the end
    assert output_file.read_text() == expected_output


def test_concat_files_empty_file(tmp_path): # Test concatenation when one file is empty
    file1 = tmp_path / "sample1.txt"
    file2 = tmp_path / "sample2.txt"
    output_file = tmp_path / "output.txt"

    # Write content to one file and leave the other empty
    file1.write_text("Only this file has content\n")
    file2.write_text("")

    processor = FileProcessor(str(file1))
    processor.concat_files(str(file2), str(output_file))

    expected_output = "Only this file has content"  # No extra newlines
    assert output_file.read_text() == expected_output

