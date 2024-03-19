from pydantic import BaseModel, constr, validator, ValidationError, field_validator
import re
from typing import List
from pydantic.functional_validators import AfterValidator
from typing import List, Dict, Optional
from typing_extensions import Annotated


class Address(BaseModel):
    city: constr(max_length=100, min_length=1)
    postcode: Optional[str]
    street: constr(max_length=250, min_length=1)

    @field_validator('postcode')
    def check_postcode_format(cls, value):
        if not value:
            return value
        if not re.match(r'^\d{2}-\d{3}$', value):
            raise ValueError("Invalid postcode format")
        return value

    @field_validator('city')
    def no_special_characters(cls, value):
        if not value.replace(' ', '').isalnum():
            raise ValueError("Can only contain Polish letters and whitespaces")
        return value

    @field_validator('street')
    def validate_street_format(cls, value):
        polish_address_pattern = re.compile(r'^[\w\s,.ąćęłńóśźżĄĆĘŁŃÓŚŹŻ-]+ \d+\/?\d*\b$')

        if polish_address_pattern.match(value):
            return True
        else:
            return False


def validate_categories(value: str) -> str:
    if not value.replace(' ', '').isalnum():
        raise AssertionError("Categories can only contain Polish letters and whitespaces")
    return value


Category = Annotated[str, AfterValidator(validate_categories)]


class POI(BaseModel):
    name: constr(max_length=100, min_length=1)
    address: Address
    categories: List[Category]

    @field_validator('categories')
    def validate_categories_len(cls, value):
        if len(value) == 0:
            raise ValueError("Categories list cannot be empty")
        return value
