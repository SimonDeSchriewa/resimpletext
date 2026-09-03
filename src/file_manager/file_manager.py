from mistletoe import markdown

def open_file(file_name) -> str:
    """Opens a file and returns its contents in a str."""
    with open(file_name, 'r') as f:
        return f.read()

def convert_file_to_html(file_name) -> str:
    """Opens a file and returns its contents in html format."""
    with open(file_name, 'r') as f:
        return markdown(f)


def convert_str_to_html(content: str) -> str:
    """Formats a str to html and returns it."""
    return markdown(content)
