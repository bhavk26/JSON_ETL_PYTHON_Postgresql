import logging

#initiating logger class
def init_logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s')
    logging.info('Starting logger')
