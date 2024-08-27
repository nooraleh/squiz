import xml.etree.ElementTree as ET
import sys
import os
# from mappings import (
#     gregoire, cpp_youtube, oliveira, excel,
#     effective_cpp_11_14, options_futures_derivatives
# )
import gregoire
import importlib
module_name = os.path.splitext( sys.argv[1])[0]
module_path = os.path.join(os.path.dirname(__file__), f"{module_name}.py")
spec = importlib.util.spec_from_file_location(module_name, module_path)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)

def convert_to_csharp(dictionary):
    csharp_code = "Dictionary<int, Dictionary<string, string>> dict = new Dictionary<int, Dictionary<string, string>>() {\n"
    for key, inner_dict in dictionary.items():
        csharp_code += f"\t{{{key}, new Dictionary<string, string>() {{\n"
        for inner_key, inner_value in inner_dict.items():
            # Escape double quotes inside the string and ensure verbatim string formatting
            escaped_value = inner_value.replace('"', '""')
            csharp_code += f'\t\t{{"{inner_key}", @"{escaped_value.strip()}"}},\n'
        
        # Add additional Dictionary<string, string> items for "snippetQ" and "snippetA"
        csharp_code += '\t\t{"snippetQ", @""},\n'
        csharp_code += '\t\t{"snippetA", @""},\n'

        csharp_code += "\t}},\n"
    csharp_code += "};"
    return csharp_code

# Example dictionary
python_dict = {
    1: {
        'q': "What's an alternative way of writing 'include <iostream>' introduced by C++20 standard?",
        'a': "import <iostream>",
    }
}

def write_to_file(csharp_code, filename):
    with open(filename, 'w') as file:
        file.write(csharp_code)

# Convert to C#
csharp_code = convert_to_csharp(module.qna)
 
write_to_file(csharp_code, f'{module_name}_output_final.cs')


