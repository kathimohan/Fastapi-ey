import multiprocessing
from typing import List

def add_lists(lists: List[List[int]]) -> List[int]:
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(sum, lists)
    return results
