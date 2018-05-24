"""Implementation of solution of fifth task."""
import logging


def process(retries):
    """Gets data from source and does work on it."""
    timeout = 3
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    for _ in range(retries):
        my_connection = connect()

        if my_connection is not None:
            logger.info("Connected")
            break

        logger.error("Connection failed")

    while True:
        try:
            new_record = get_next_record(my_connection, timeout)
        except ConnectionException:
            logger.exception("Broken connection")
            break
        else:
            if new_record is not None:
                try:
                    do_work(new_record)
                except ProcessingException:
                    print("Error occurred while processing record!")

    return
