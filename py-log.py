import logging
import os
from datetime import datetime
#give your path
LOG_FILENAME = datetime.now().strftime('./log/%d-%m-%Y.log')
logging.basicConfig(level=logging.DEBUG, filename=LOG_FILENAME, format='%(asctime)s %(levelname)s:%(message)s')
if os.path.isfile(LOG_FILENAME)!=True:
    file_handler = logging.FileHandler(LOG_FILENAME, mode="w", encoding=None, delay=False)
else:
    #log your message
    logging.info('else case 1')
    logging.debug('else case 2')