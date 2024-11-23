from app.utils.exceptions import BaseKnittingException


class CredentialsValidateException(BaseKnittingException):
    message = 'Could not validate credentials'


class IncorrectUsernameOrPasswordException(BaseKnittingException):
    message = 'Incorrect username or password'
