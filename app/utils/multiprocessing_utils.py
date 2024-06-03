import multiprocessing
from typing import List
import logging
logger = logging.getLogger(__name__)
def add_lists(lists: List[List[int]]) -> List[int]:
    logger.info("Starting add_lists with payload: %s", lists)
    try:
        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            results = pool.map(sum, lists)
        logger.info("Completed add_lists with results: %s", results)
        return results
    except Exception as e:
        logger.error("Error in add_lists: %s", e)
        raise
