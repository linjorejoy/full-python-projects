from typing import List


def nSum_strict(depth: int, arr: List[int], target: int) -> List[int]:

    all_answers = []

    if depth == 2:
        meta_map = {}
        answers = []
        for i, el in enumerate(arr):
            if el in meta_map.keys():
                answers.append([meta_map[el], i])
            else:
                meta_map[target - el] = i
        return answers
    else:
        for i, el in enumerate(arr):
            indeces_arr = nSum_strict(depth-1, [*arr[:i], *arr[i+1:]], target - el)
            if indeces_arr:
                for indeces in indeces_arr:
                    if i not in indeces:
                        new_answer = [*indeces, i]
                        new_answer.sort()
                        if new_answer not in all_answers:
                            all_answers.append(new_answer)

    return all_answers


if __name__ == "__main__":
    print(f"{nSum_strict(3, [1, 2, 3, 4, 5, 2], 6)=}")
    # print(f"{nSum_strict(4, [1,2,3,4,5,2,5,8,4,3,4,1,3,5], 10)=}")
    # print(f"{nSum_strict(10, [0,1,2,3,4,5,6,7,8,9], 45)=}")
