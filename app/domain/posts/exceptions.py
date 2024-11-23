from app.utils.exceptions import BaseKnittingException


class CreatorCheckedException(BaseKnittingException):
    message = 'Creator verification error'
