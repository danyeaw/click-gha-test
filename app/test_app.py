from .app import main
import sys
from io import StringIO
from rich.console import Console


def test_hello():
    console = Console(file=StringIO())
    console.print(main())
    str_output = console.file.getvalue()
    assert "Hello" in str_output
