import typing
from collections import Counter
from typing import Callable, List, Tuple


def main():
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    # part1(lines)
    part2(lines)


def part1(lines: List[str]):
    gamma_bin = most_common_bits(lines)
    gamma = int(gamma_bin, 2)

    epsilon_bin = flip(gamma_bin)
    epsilon = int(epsilon_bin, 2)

    print(gamma * epsilon)


def part2(lines: List[str]):
    oxygen_bin = find_line_matching_bit_criteria(oxygen_crit, lines)
    oxygen = int(oxygen_bin, 2)

    co2_bin = find_line_matching_bit_criteria(co2_crit, lines)
    co2 = int(co2_bin, 2)

    print(oxygen * co2)


Ranking = List[Tuple[str, int]]
BitCriteria = Callable[[Ranking], str]


def oxygen_crit(rank: Ranking) -> str:
    (bit, n), (_, m) = rank
    if n == m:
        bit = "1"
    return bit


def co2_crit(rank: Ranking) -> str:
    (_, n), (bit, m) = rank
    if n == m:
        bit = "0"
    return bit


def find_line_matching_bit_criteria(bit_crit: BitCriteria, lines: List[str]) -> str:
    for i in range(len(lines[0])):
        rank = count_ith_bits(i, lines).most_common(2)
        bit = bit_crit(rank) if len(rank) == 2 else rank[0][0]
        lines = [line for line in lines if line[i] == bit]
        if len(lines) == 1:
            return lines[0]
    raise ValueError("not found")


def most_common_bits(lines: List[str]) -> str:
    result = ""
    for i in range(len(lines[0])):
        c = count_ith_bits(i, lines)
        result += c.most_common(1)[0][0]
    return result


def count_ith_bits(i: int, lines: List[str]) -> typing.Counter[str]:
    return Counter([line[i] for line in lines])


def flip(bits: str) -> str:
    return bits.replace("0", "_").replace("1", "0").replace("_", "1")


if __name__ == "__main__":
    main()
