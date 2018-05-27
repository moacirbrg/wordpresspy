class WordPressError(Exception):
    def __init__(self, message, http_status):
        super().__init__(message)
        self.http_status = http_status


class WordPressPyError(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code
