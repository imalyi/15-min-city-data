from pydantic import BaseModel, confloat
from pydantic import BaseModel, constr, validator, ValidationError, field_validator
import re
from typing import List
from pydantic.functional_validators import AfterValidator
from typing import List, Dict, Optional
from typing_extensions import Annotated


class Stop(BaseModel):
    name: constr(max_length=70, min_length=5)
    lat: confloat(ge=-90, le=90)
    lon: confloat(ge=-180, le=180)
