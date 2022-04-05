"""Implementations of coalescing strategies"""
from statistics import mean

from .models import Coverage


def average(coverages: list[Coverage]) -> Coverage:
    """Finds the average of each attribute across all coverages"""
    return Coverage(
        deductible=round(mean([cov.deductible for cov in coverages])),
        stop_loss=round(mean([cov.stop_loss for cov in coverages])),
        oop_max=round(mean([cov.oop_max for cov in coverages]))
    )


def minimum(coverages: list[Coverage]) -> Coverage:
    """Finds the minimum of each attribute across all coverages"""
    return Coverage(
        deductible=min([cov.deductible for cov in coverages]),
        stop_loss=min([cov.stop_loss for cov in coverages]),
        oop_max=min([cov.oop_max for cov in coverages])
    )


def maximum(coverages: list[Coverage]) -> Coverage:
    """Finds the maximum of each attribute across all coverages"""
    return Coverage(
        deductible=max([cov.deductible for cov in coverages]),
        stop_loss=max([cov.stop_loss for cov in coverages]),
        oop_max=max([cov.oop_max for cov in coverages])
    )


STRATEGIES = {
    "average": average,
    "minimum": minimum,
    "maximum": maximum
}
