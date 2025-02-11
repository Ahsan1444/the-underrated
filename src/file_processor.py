import os
from src.text_decorator import color_text

class FileProcessor:
    def __init__(self, filename): # Initialize the file processor with a filename
        self._filename = filename

    @property
    def filename(self): # Getter for filename
        return self._filename

    @filename.setter
    def filename(self, new_name): # Setter for filename
        self._filename = new_name

    def read_file(self): # Generator function to read the file line by line
        with open(self.filename, 'r') as file:
            for line in file:
                yield line.strip()

    @staticmethod
    def is_text_file(filename): # Check if a file is a .txt file
        return filename.endswith('.txt')

    @classmethod
    def create_from_file(cls, filename): # Creates an instance from a given filename
        return cls(filename)

    def __str__(self): # String representation of the object
        return f"FileProcessor({self.filename})"

    def __add__(self, other): # Concatenates two file processors into one
        return FileProcessor(self.filename + '_' + other.filename)

    def concat_files(self, other_filename, output_filename): # Concatenates two files and writes output (without extra newlines)
        print(f"\033[93mReading from: {self.filename} and {other_filename}\033[0m")
        print(f"\033[93mWriting to: {output_filename}\033[0m")

        with open(self.filename, 'r') as f1, open(other_filename, 'r') as f2, open(output_filename, 'w') as out:
            content1 = f1.read().rstrip()  # Remove trailing newlines
            content2 = f2.read().rstrip()

            if content1 and content2:
                out.write(content1 + "\n" + content2)  # Add only one newline between them
            elif content1:
                out.write(content1)  # Avoid extra newlines
            elif content2:
                out.write(content2)  # Avoid extra newlines

        print("\033[92mFile concatenated successfully.\033[0m")


    def concat_multiple_files(self, output_filename, *filenames): #Concatenates multiple files and writes output (without colors)
        print(f"\033[93mMerging multiple files into: {output_filename}\033[0m")

        with open(output_filename, 'w') as out:
            for file in filenames:
                with open(file, 'r') as f:
                    out.writelines(f.readlines())
                    out.write("\n")  # Add a newline for separation

        print("\033[92mMultiple files merged successfully.\033[0m")

    @color_text("green")
    def display_success(self): # Displays success message"""
        return "File processed successfully!"

