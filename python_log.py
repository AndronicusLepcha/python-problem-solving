import logging
logging.basicConfig(filename="log.txt",level=logging.WARNING)
print('loggig DEMO')
logging.critical('this is critical message ')
logging.error('this is error messge')
logging.warning('this is a warning msg')
logging.info('this is info message')
logging.debug('this is debug message')