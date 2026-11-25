#!/usr/bin/env python3
"""Count exact 1-dart, 2-dart, and 3-dart combinations summing to 100 without item reuse."""
from itertools import combinations
import json

SAMPLE_US_STATES = {f"State_{i}": i for i in range(1, 51)}

def solve_checkouts(items: dict[str, int], target: int = 100) -> dict:
    pairs = list(items.items())
    one = [a[0] for a in pairs if a[1] == target]
    two = [(a[0], b[0]) for a, b in combinations(pairs, 2) if a[1] + b[1] == target]
    three = [(a[0], b[0], c[0]) for a, b, c in combinations(pairs, 3) if a[1] + b[1] + c[1] == target]
    return {
        "item_count": len(pairs),
        "has_rescue_dart_100": len(one) > 0,
        "exact_1_dart": len(one),
        "exact_2_dart": len(two),
        "exact_3_dart": len(three),
        "total_bullseye_ways": len(one) + len(two) + len(three),
        "sample_checkout": two[0] if two else (three[0] if three else one[:1]),
    }

if __name__ == "__main__":
    print(json.dumps(solve_checkouts(SAMPLE_US_STATES), indent=2))
