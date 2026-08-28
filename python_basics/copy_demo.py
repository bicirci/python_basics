import copy


def print_state(label, a, b):
    """打印两个对象的内容及关键元素的 id"""
    print(f"\n{label}")
    print(f"a: {a}, id(a)={id(a)}, id(a[1])={id(a[1])}, id(a[2])={id(a[2])}")
    print(f"b: {b}, id(b)={id(b)}, id(b[1])={id(b[1])}, id(b[2])={id(b[2])}")


def test_direct_assignment():
    print("\n" + "=" * 60)
    print("测试 1：直接赋值 b = a")
    a = [1, [2, 3], (4, 5)]
    b = a
    print_state("初始状态", a, b)

    a[0] = 10  # 修改顶层元素
    print_state("修改顶层 a[0] = 10", a, b)

    a[1][0] = 20  # 修改嵌套可变对象（列表）
    print_state("修改嵌套可变 a[1][0] = 20", a, b)

    a[2] = (6, 7)  # 重新赋值嵌套不可变对象（元组）
    print_state("修改嵌套不可变 a[2] = (6,7)", a, b)


def test_copy_method():
    print("\n" + "=" * 60)
    print("测试 2：浅拷贝 b = a.copy()")
    a = [1, [2, 3], (4, 5)]
    b = a.copy()
    print_state("初始状态", a, b)

    a[0] = 10
    print_state("修改顶层 a[0] = 10", a, b)

    a[1][0] = 20
    print_state("修改嵌套可变 a[1][0] = 20", a, b)

    a[2] = (6, 7)
    print_state("修改嵌套不可变 a[2] = (6,7)", a, b)


def test_copy_module():
    print("\n" + "=" * 60)
    print("测试 3：浅拷贝 b = copy.copy(a)")
    a = [1, [2, 3], (4, 5)]
    b = copy.copy(a)
    print_state("初始状态", a, b)

    a[0] = 10
    print_state("修改顶层 a[0] = 10", a, b)

    a[1][0] = 20
    print_state("修改嵌套可变 a[1][0] = 20", a, b)

    a[2] = (6, 7)
    print_state("修改嵌套不可变 a[2] = (6,7)", a, b)


def test_deepcopy():
    print("\n" + "=" * 60)
    print("测试 4：深拷贝 b = copy.deepcopy(a)")
    a = [1, [2, 3], (4, 5)]
    b = copy.deepcopy(a)
    print_state("初始状态", a, b)

    a[0] = 10
    print_state("修改顶层 a[0] = 10", a, b)

    a[1][0] = 20
    print_state("修改嵌套可变 a[1][0] = 20", a, b)

    a[2] = (6, 7)
    print_state("修改嵌套不可变 a[2] = (6,7)", a, b)


if __name__ == "__main__":
    test_direct_assignment()
    test_copy_method()
    test_copy_module()
    test_deepcopy()
