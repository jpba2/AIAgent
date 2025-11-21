import os
from config import FILE_MAX_CHARS

def get_file_content(working_directory, file_path):
    test_path = os.path.join(working_directory, file_path)
    
    if not os.path.abspath(test_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(test_path):
        return f'Error: File not found or is not a regular file: "{test_path}"'
    
    try:
        with open(test_path, "r") as f:
            file_content_string = f.read(FILE_MAX_CHARS)
            if os.path.getsize(test_path) > FILE_MAX_CHARS:
                file_content_string += (
                    f'[...File "{file_path}" truncated at {FILE_MAX_CHARS} characters]'
                )
        return file_content_string
    except Exception as e:
        print(f'Error: {e}')