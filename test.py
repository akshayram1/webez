from webez.html_converter import convert_html_to_twig
from pathlib import Path

# File paths
input_file = r"input.html"
output_file = r"output.twig"

try:
    # Read the input HTML file
    html_content = Path(input_file).read_text(encoding="utf-8")
    
    # Convert HTML to Twig
    twig_content = convert_html_to_twig(html_content)
    
    # Write the Twig content to the output file
    Path(output_file).write_text(twig_content, encoding="utf-8")
    
    print(f"Conversion successful! Twig file saved to: {output_file}")
except Exception as e:
    print(f"An error occurred: {e}")
