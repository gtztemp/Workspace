import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

logger.debug("Start of program")


def factorial(n):
    logger.debug("Start of factorial(%d)", n)
    total = 1

    for i in range(1, n + 1):
        total *= i
        logger.debug("i is %d, total is %d", i, total)

    logger.debug("End of factorial(%d)", n)
    return total


print(factorial(5))

logger.debug("End of program")
