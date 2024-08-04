from pydantic import BaseModel
import enum



class CutCategories(str,enum.Enum):
    Fair = "Fair" 
    Good = "Good"
    Very_Good = "Very Good"
    Premium = "Premium"
    Ideal = "Ideal"

class ColorCategories(str, enum.Enum):
    J = "J"
    I = "I" 
    H = "H"
    G = "G"
    F = "F"
    E = "E"
    D = "D"

class ClarityCategories(str, enum.Enum):
    I1 = "I1"
    SI2 = "SI2" 
    SI1 = "SI1"
    VS2 = "VS2"
    VS1 = "VS1" 
    VVS2 = "VVS2"
    VVS1 = "VVS1"
    IF = "IF"


class Requestmodel(BaseModel):
    carat: float
    cut: CutCategories
    color: ColorCategories 
    clarity: ClarityCategories 
    depth: float
    table: float 
    x: float 
    y: float
    z: float

class Responsemodel(BaseModel):
    price : float