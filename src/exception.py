import sys

def error_message_detail(error, error_detail:sys):
    '''exc_tb gives info about the file exception has occured and
    in which line did that occured....
    exc_info---execution info'''
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format()
