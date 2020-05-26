class NotImplementedError(Exception):
    def __init__(self, message):
        self.msg = message


class ApiError(Exception):
    def __init__(self, error_code, error_msg, error_text):
        self.error_code = error_code
        self.error_msg = error_msg
        self.error_text = error_text
