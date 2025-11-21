import os
from config import FILE_MAX_CHARS

def write_file(working_directory, file_path, content):
    test_path = os.path.join(working_directory, file_path)

    if not os.path.abspath(test_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(test_path):
        return f'Error: File not found or does not exist: "{test_path}"'
    
    try:
        with open(test_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{test_path}" ({len(content)} characters written)'
    except Exception as e:
        return print(f'Error: {e}')
    
