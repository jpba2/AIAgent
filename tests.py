from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from call_function import call_function

class FakeFunctionCall:
    def __init__(self, name, args):
        self.name = name
        self.args = args

fake = FakeFunctionCall(
    name="get_file_content",
    args={"file_path" : "lorem.txt"}
)

fake2 = FakeFunctionCall(
    name="get_file_address",
    args={"file_path" : "lorem.txt"}
)

def test():
    result = call_function(fake, verbose=True)
    print(" --> Result A - verbose = True")
    print(result)
    print("")

    result = call_function(fake, verbose=False)
    print(" --> Result B - Verbose = False")
    print(result)
    print("")

    result = call_function(fake2, verbose=True)
    print(" --> Result C")
    print(result)
    print("")

    result = call_function(fake2, verbose=False)
    print(" --> Result for D")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for calculator/nonexistent.py")
    print(result)
    print("")

    result = run_python_file("calculator", "lorem.txt")
    print("Result for calculator/lorem.txt:")
    print(result)
    print("")

if __name__ == "__main__":
    test()