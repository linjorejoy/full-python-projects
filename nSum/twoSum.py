from typing import List


def twoSum_strict(arr: List[int], target: int) -> List[List[int]]:
    meta_map = {}
    answers = []
    for i, el in enumerate(arr):
        if el in meta_map.keys():
            answers.append([meta_map[el], i])
        else:
            meta_map[target - el] = i
    return answers


def twoSum_linient(arr: List[float], target: float, margin_top: float, margin_bottom: float) -> List[List[int]]:
    if margin_top < 0:
        raise ValueError("margin_top should be non negative")
    if margin_bottom < 0:
        raise ValueError("margin_bottom should be non negative")
    meta_map = {}
    answers = []
    for i, el in enumerate(arr):

        pass


if __name__ == "__main__":
    print(f"{twoSum_strict([1, 2, 3, 4, 5, 20], 6) = }")
    print(f"{twoSum_linient([1, 2, 3, 4, 5, 4], 6, 1, 2)}")
