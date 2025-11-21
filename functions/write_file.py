import os
from config import FILE_MAX_CHARS
from google import genai
from google.genai import types

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
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write to a file, relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the file to be written, relative to the working directory. If not provided, or the file is not in the working dictionary, returns an error",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written to the file."
            )
        },
    ),
)
    
