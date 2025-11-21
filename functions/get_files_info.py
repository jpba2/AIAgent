import os
from google import genai
from google.genai import types

def get_files_info(working_directory, directory="."):
    test_path = os.path.join(working_directory, directory)
    
    if not os.path.abspath(test_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(test_path):
        return f'Error: "{test_path}" is not a directory'
    
    else:
        try:
            directory = os.listdir(test_path)
            directory_list = str()
            for file in directory[:-1]:
                rel_path = os.path.join(test_path, file)
                directory_list += f"- {file}:  file_size={os.path.getsize(rel_path)} bytes, is_dir={os.path.isdir(rel_path)}\n"
            directory_list += f"- {directory[-1]}:  file_size={os.path.getsize(os.path.join(test_path, directory[-1]))} bytes, is_dir={os.path.isdir(os.path.join(test_path, directory[-1]))}"
            return directory_list
        except Exception as e:
            print(f'Error: {e}')

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
