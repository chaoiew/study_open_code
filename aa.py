def f(a, b):
    return a + b


if __name__ == "__main__":
    # 测试用例
    print(f"f(1, 2) = {f(1, 2)}")  # 预期: 3
    print(f"f(0, 0) = {f(0, 0)}")  # 预期: 0
    print(f"f(-1, 1) = {f(-1, 1)}")  # 预期: 0
    print(f"f(3.14, 2.86) = {f(3.14, 2.86)}")  # 预期: 6.0
    print(f"f('hello', ' world') = {f('hello', ' world')}")  # 预期: hello world
