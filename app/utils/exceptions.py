class BaseKnittingException(Exception):
    message: str | None = None

    def __init__(self, msg: str | None = message):
        super().__init__(msg)