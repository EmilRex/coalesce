from coalesce.models import Coverage
from coalesce.strategies import average, minimum, maximum


def coverage(deductible: int, stop_loss: int, oop_max: int):
    return Coverage(
        deductible=deductible,
        stop_loss=stop_loss,
        oop_max=oop_max
    )


def test_average_single():
    result = average([
        coverage(100, 100, 100),
    ])
    assert result == coverage(100, 100, 100)


def test_average_multiple_even():
    result = average([
        coverage(100, 100, 200),
        coverage(300, 100, 200),
    ])
    assert result == coverage(200, 100, 200)


def test_average_multiple_odd():
    result = average([
        coverage(1, 1000, 5),
        coverage(2, 0, 2),
    ])
    assert result == coverage(2, 500, 4)


def test_minimum():
    result = minimum([
        coverage(3, 1, 3),
        coverage(10, 5, 2),
        coverage(6, 2, 2),
    ])
    assert result == coverage(3, 1, 2)


def test_maximim():
    result = maximum([
        coverage(1000, 0, 2),
        coverage(100, 100, 100),
        coverage(2000, 0, 3),
    ])
    assert result == coverage(2000, 100, 100)
