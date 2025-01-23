from pydantic import BaseModel, EmailStr, Field

from pydantic import BaseModel, EmailStr, Field, root_validator

class UserSignup(BaseModel):
    email: EmailStr
    password: str
    confirmPassword: str = Field(..., min_length=6)

    @root_validator(pre=True)
    def validate_passwords(cls, values):
        if values.get("password") != values.get("confirmPassword"):
            raise ValueError("Passwords do not match")
        return values

            
class UserLogin(BaseModel):
    email: EmailStr
    password: str