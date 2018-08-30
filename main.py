import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME = 'github'
HOMPAGE = 'https://github.com/beingabeer'
DOMAIN_NAME = get_domain_name(HOMPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMPAGE, DOMAIN_NAME)

