import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import available_functions
from call_function import call_function


def main():
    load_dotenv()

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files


    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    
    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    user_prompt = " ".join(args)
 
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    
    

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
        )

    verbose = "--verbose" in user_prompt

    if "--verbose" in user_prompt:
        print(f"User prompt: {user_prompt}")    
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if not response.function_calls:
        print("Response:")
        print(response.text)
        return response.text
    

    function_responses = []
    for calls in response.function_calls:
        call_return = call_function(calls, verbose)
        if (not call_return.parts or not call_return.parts[0].function_response):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {call_return.parts[0].function_response.response}")
        function_responses.append(call_return.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting")
        
        


if __name__ == "__main__":
    main()

