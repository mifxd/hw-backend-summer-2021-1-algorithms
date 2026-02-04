__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    if not numbers:
        return 0.0

    sum_even = 0
    sum_odd = 0

    for n in numbers:
        if n % 2 == 0:
            sum_even += n
        else:
            sum_odd += n

    if sum_odd == 0:
        return 0.0

    return sum_even/sum_odd
