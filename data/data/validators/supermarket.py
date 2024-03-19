from pydantic import BaseModel, constr, validator, ValidationError, field_validator
import re
from typing import List
from pydantic.functional_validators import AfterValidator

from typing_extensions import Annotated


from data.validators.POI import Address


class Supermarket(BaseModel):
    name: constr(max_length=100, min_length=1)
    address: Address
    categories: List[str]
