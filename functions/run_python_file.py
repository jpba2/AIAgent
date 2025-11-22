import os
import subprocess
import sys
from  google import genai
from google.genai import types

def run_python_file(working_directory, file_path, args = []):
    test_path = os.path.join(working_directory, file_path)

    if not os.path.abspath(test_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(test_path):
        return f'Error: File "{file_path}" not found.'

    if not test_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        sub_args = ["python3", test_path] + args
        result = subprocess.run(sub_args, capture_output=True, timeout=30)
        if result == None:
            return "No output produced"
        if result.returncode == 0:
            return f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"
        return f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}\nProcess exited with code {result.returncode}"
        
    except Exception as e:
        return f'Error: executing Python file: {e}'
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file, provided it is within the the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Option arguments to pass to the Python file.",
                ),
                description="Option arguments to pass to the Python file."
            )
        },
        required=["file_path"]
    ),
)
    


    
