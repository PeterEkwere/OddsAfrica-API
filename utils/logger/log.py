import logging

# Set up logging configuration
logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def log_error(message):
    """ This function logs all errors to the file

    Args:
        message (str): The error message
    """
    logging.error(message)
    
def log_success(message):
    """ This function logs all success status to the file

    Args:
        message (str): the success message
    """
    logging.info(message)
    
def log_exception(message):
    """ This function logs all exceptions raised to the file 

    Args:
        message (str): the exception message
    """
    logging.exception(message)
    
    