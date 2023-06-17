from twoSum import twoSum_strict
from typing import List


def threeSum_strict(arr: List[int], target: int) -> List[int]:
    answers = []
    for i, el in enumerate(arr):
        twoSum_indices = twoSum_strict(arr, target - el)
        if twoSum_indices:
            for indeces in twoSum_indices:
                if i not in indeces:
                    answer = [*indeces, i]
                    answer.sort()
                    answers.append(answer)
    return answers


if __name__ == "__main__":
    print(threeSum_strict([1, 2, 3, 4, 5, 2], 6))
