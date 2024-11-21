import inspect
import importlib
import sys
import os
#  python3 '.\import inspect.py' pandas ./test.txt
def export_functions_from_module(module_name, output_file):
    try:
        # Import the module dynamically
        module = importlib.import_module(module_name)

        with open(output_file, 'w') as file:
            file.write(f"# Functions, classes, and methods from module: {module_name}\n\n")

            # Export functions
            file.write("# Functions:\n")
            for name, obj in inspect.getmembers(module, inspect.isfunction):   
                signature = inspect.signature(obj)
                file.write(f"{name}{signature}\n")
            file.write("\n")

            # Export classes and their methods
            file.write("# Classes and methods:\n")
            for name, obj in inspect.getmembers(module, inspect.isclass):
                file.write(f"Class: {name}\n")
                
                # Get methods of the class
                for method_name, method_obj in inspect.getmembers(obj, inspect.isfunction):
                    method_signature = inspect.signature(method_obj)
                    file.write(f"    {method_name}{method_signature}\n")
                file.write("\n")

        print(f"Functions and classes exported successfully to {output_file}")


    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python export_functions.py <module_name> <output_file>")
        sys.exit(1)

    module_name = sys.argv[1]
    output_file = sys.argv[2]

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    export_functions_from_module(module_name, output_file)
