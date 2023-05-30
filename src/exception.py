import sys

def error_message_detail(error, error_detail:sys):
    -,-,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurrred in python script name [{1}] line number [{2}] error message [{3}]".format(
        file_name, exc_tb.tb_lineno, str(error))

    return error_message

    

class CustomeException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__():
        return self.error_message


