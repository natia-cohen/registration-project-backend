from pydantic import BaseModel, EmailStr, Field, root_validator

class UserSignup(BaseModel):
    email: EmailStr
    password: str

    @root_validator(pre=True)
    def validate_passwords(cls, values):
        confirm_password = values.pop("confirmPassword", None)  
        if not confirm_password or values.get("password") != confirm_password:
            raise ValueError("Passwords do not match")
        return values

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str = Field(..., min_length=6, description="New password must be at least 6 characters long")