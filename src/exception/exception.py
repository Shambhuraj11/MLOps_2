import sys


class customexception(Exception):

    def __init__(self, error_msg: str, error_details:sys) -> None:
        self.error_msg = error_msg
        _,_,exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename



    def __str__(self) -> str:
        return f"An error occurred at line {self.lineno} in {self.file_name} with error message {self.error_msg}"
    


if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        raise customexception(e,sys)

