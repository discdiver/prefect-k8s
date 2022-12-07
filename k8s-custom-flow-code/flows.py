from prefect import flow, get_run_logger
from platform import node, platform


@flow
def check():
    logger = get_run_logger()
    logger.info(f"Network: {node()}. ✅")
    logger.info(f"Instance: {platform()}. ✅")


if __name__ == "__main__":
    check()
