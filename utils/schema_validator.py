from jsonschema import validate
from jsonschema.exceptions import ValidationError

def validate_schema(data, schema):
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        raise AssertionError(f"Schema validation error: {e.message}")
