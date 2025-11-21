import os
from google import genai
from google.genai import types

def call_function(function_call_part, verbose=False):
    if verbose == True:
        print("Verbose == True")
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print("Verbose == False")
        print(f" - Calling function: {function_call_part.name}")
    #result = 

print(call_function(write_file({'content': 'hello', 'file_path': 'main.txt'}), verbose=False))
print(call_function(write_file({'content': 'hello', 'file_path': 'main.txt'}), verbose=True))