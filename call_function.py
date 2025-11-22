from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file, write_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ]
    )   

def call_function(function_call_part, verbose=False):
    if verbose == True:
        print("verbose is true")
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print("verbose is false")
        print(f" - Calling function: {function_call_part.name}")
    #result = 

print(call_function(write_file(**{'working_directory': './calculator', 'content': 'hello', 'file_path': 'main.txt'}), verbose=False))
print(call_function(write_file(**{'content': 'hello', 'file_path': 'main.txt'}), verbose=True))