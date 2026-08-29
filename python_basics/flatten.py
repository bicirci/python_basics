def expand_nested(value: list | tuple, ids :list,  cur_dept:int , max_dept:int):
    result = []
    if cur_dept > max_dept:
        raise ValueError("exceed max depth")
    if id(value) in ids:
        raise ValueError("loop ref")
    ids.append(id(value))
    for x in value:
        if isinstance(x, (list, tuple)):
            item_list = expand_nested(x, ids, cur_dept + 1, max_dept)
            result.extend(item_list)
        else:
            result.append(x)
    ids.pop()
    return result


def flatten_nested(value: list | tuple, *, max_depth: int = 100) -> list:
    if not isinstance(value, (list, tuple)):
        raise TypeError(f"value must be a list or tuple, got {type(value).__name__}")
    if max_depth < 0:
        raise ValueError("invalid max_depth value")

    id_trace = []
    result = expand_nested(value, id_trace , 0, max_depth)
    print(f" result = {result}")
    return result


if __name__ == "__main__":
    test = ["chacha", [1, 2, 3, [1, 2]]]
    flatten_nested(test, max_depth=1)
