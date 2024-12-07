import math


def test_equation_1(nums, result):
    if len(nums) <= 2:
        return (sum(nums) == result or
                math.prod(nums) == result)
    return (test_equation_1([nums[0] + nums[1]] + nums[2:], result) or
            test_equation_1([nums[0] * nums[1]] + nums[2:], result))


def parse_line(line: str):
    result, nums = line.split(': ')
    nums = nums.split(' ')
    return int(result), [int(n) for n in nums]


def q1():
    with open('input.txt', 'r') as f:
        experiments = [parse_line(line) for line in f.read().splitlines()]
    return sum(result for result, nums in experiments if test_equation_1(nums, result))


def test_equation_2(nums, result):
    if len(nums) <= 2:
        return (sum(map(int, nums)) == result or
                math.prod(map(int, nums)) == result or
                ''.join(map(str, nums)) == str(result))
    return (test_equation_2([nums[0] + nums[1]] + nums[2:], result) or
            test_equation_2([nums[0] * nums[1]] + nums[2:], result) or
            test_equation_2([int(str(nums[0]) + str(nums[1]))] + nums[2:], result))


def q2():
    with open('input.txt', 'r') as f:
        experiments = [parse_line(line) for line in f.read().splitlines()]
    return sum(result for result, nums in experiments if test_equation_2(nums, result))


if __name__ == '__main__':
    from time import perf_counter as pc

    st = pc()
    print(f'Part 1: {q1()}')
    pt1 = pc()
    print(f'Part 2: {q2()}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1 - st) * 1000}ms\n\
            Part 2: {(pt2 - pt1) * 1000}ms\n\
            Total: {(pt2 - st) * 1000}ms')
