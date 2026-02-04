import convert_to_hugo
import os

# Create dummy content if not exists for testing
html_file = 'content/algorithms/backtracking/n_queens.html'
test_output = './test_n_queens.md'

if os.path.exists(html_file):
    convert_to_hugo.process_file(html_file, test_output, "N-Queens Problem")
    with open(test_output, 'r') as f:
        print(f.read())
else:
    print(f"File {html_file} not found.")
