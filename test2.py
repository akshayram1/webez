from webez.html_converter import convert_html_to_twig
from pathlib import Path

def convert_html_file(input_file: str, output_file: str = None) -> None:
    """
    Convert HTML file to Twig
    Args:
        input_file (str): Path to input HTML file
        output_file (str): Path to output Twig file (optional)
    """
    try:
        # Setup paths
        input_path = Path(input_file)
        output_path = Path(output_file) if output_file else input_path.with_suffix('.twig')
        
        # Read and convert
        html_content = input_path.read_text(encoding="utf-8")
        twig_content = convert_html_to_twig(html_content)
        
        # Write output
        output_path.write_text(twig_content, encoding="utf-8")
        print(f"✓ Successfully converted to: {output_path}")
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
    except Exception as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    # Example usage
    convert_html_file("input.html", "output.twig")