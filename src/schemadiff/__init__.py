"""SchemaDiff: Compares two dataset schemas and lists added, removed or changed fields."""

__version__ = "1.0.0"

from .core import run
from .cli import main

__all__ = ["main", "run", "__version__"]