from itertools import product
from functools import partial
from typing import Callable, Iterable

Operation = Callable[[int, int], int]
Operands = list[int]
Equation = tuple[int, Operands]


def add(a: int, b: int) -> int:
    return a + b


def mul(a: int, b: int) -> int:
    return a * b


def concat(a: int, b: int) -> int:
    return int(f"{a}{b}")


def calculate(operands: Operands, strategy: Iterable[Operation]) -> int:
    queue = iter(operands)
    register = next(queue)
    for operation in strategy:
        register = operation(register, next(queue))
    return register


def calibrated(equation: Equation, operations: tuple[Operation, ...]) -> int:
    test, operands = equation
    strategies = product(operations, repeat=len(operands) - 1)
    for strategy in strategies:
        if calculate(operands, strategy) == test:
            return test
    return 0


def part_one(equations: list[Equation]) -> int:
    return sum(map(partial(calibrated, operations=(add, mul)), equations))


def part_two(equations: list[Equation]) -> int:
    return sum(map(partial(calibrated, operations=(add, mul, concat)), equations))


def parse(line: str) -> Equation:
    left, _, right = line.partition(":")
    return int(left), [int(num) for num in right.split()]


def main() -> None:
    with open("input.txt") as f:
        equations = [parse(l.strip()) for l in f.readlines()]
    print(part_one(equations))
    print(part_two(equations))


main()
