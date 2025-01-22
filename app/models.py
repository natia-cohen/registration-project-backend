from pydantic import BaseModel, EmailStr, Field

class UserSignup(BaseModel):
    email: EmailStr
    password: str
    confirmPassword: str = Field(..., min_length=6)

    def validate_passwords(self):
        if self.password != self.confirmPassword:
            raise ValueError("Passwords do not match")
            
class UserLogin(BaseModel):
    email: EmailStr
    password: str