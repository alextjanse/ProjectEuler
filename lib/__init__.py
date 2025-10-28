"""lib: helper modules for Project Euler solutions."""
__all__ = ["primes", "factors", "cont_fractions", "graphs"]
__version__ = "0.0.0"

# make submodules available as attributes of the package
from . import primes, factors, cont_fractions, graphs