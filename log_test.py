import logging

logging.basicConfig(filename="log_test.txt",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logging.getLogger().addHandler(logging.StreamHandler())

logging.info("Running Urban Planning")