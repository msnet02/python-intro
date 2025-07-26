# Programa: func-attributes-1.py
# Creación: 26/07/2025

def multiplication(a, b):
    """Return a multiplied by b."""
    return a * b

special_attributes = [
    '__doc__', "__name__", "__qualname__", "__module__",
    "__defaults__", "__code__", "__globals__", "__dict__",
    "__closure__", "__annotations__", "__kwdefaults__",
]

# Main code
for attribute in special_attributes:
    print(attribute, '->', getattr(multiplication, attribute))
