def expand_nested(value: list | tuple, cur_dept, max_dept):
    result = []
    if cur_dept > max_dept:
        raise ValueError("exceed max depth")
    for x in value:
        if isinstance(x, (list, tuple)):
            cur_dept, item_list = expand_nested(x, cur_dept + 1, max_dept)
            result.extend(item_list)
        else:
            result.append(x)
    return cur_dept, result


def flatten_nested(value: list | tuple, *, max_depth: int = 100) -> list:
    if not isinstance(value, (list, tuple)):
        raise TypeError(f"value must be a list or tuple, got {type(value).__name__}")
    if max_depth < 0:
        raise ValueError("invalid max_depth value")

    final_dept, result = expand_nested(value, 0, max_depth)
    print(f"final_dept = {final_dept}, result = {result}")
    return result


if __name__ == "__main__":
    test = ["chacha", [1, 2, 3, [1, 2]]]
    flatten_nested(test, max_depth=1)
