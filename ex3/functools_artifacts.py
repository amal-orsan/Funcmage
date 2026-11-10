from functools import lru_cache, partial, reduce, singledispatch
from typing import Any
import operator
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation in operations:
        return reduce(operations[operation], spells)
    else:
        raise ValueError(f"Unknown operation: {operation}")


def partial_enchanter(
        base_enchantment: Callable[..., str]
        ) -> dict[str, Callable[..., str]]:
    return {
        "fire": partial(base_enchantment, power=50, element="fire"),
        "ice": partial(base_enchantment, power=50, element="ice"),
        "lightning": partial(
            base_enchantment, power=50, element="lightning"
        ),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(arg: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(arg: int) -> str:
        return f"{arg} damage"

    @dispatch.register
    def _(arg: str) -> str:
        return arg

    @dispatch.register
    def _(arg: list) -> str:
        return f"{len(arg)} spells"

    return dispatch


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [10, 20, 30]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(10) again: {memoized_fibonacci(10)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(f"Damage spell: {dispatch(42)}")
    print(f"Enchantment: {dispatch('Fireball')}")
    print(f"Multi-cast: {dispatch(['Lightning Bolt', 'Ice Shard'])}")
    print(dispatch(3.14))

    print("\nTesting partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element.capitalize()} {target} (+{power} power)"

    enchantments = partial_enchanter(base_enchantment)
    print(enchantments["fire"](target="Sword"))
    print(enchantments["ice"](target="Shield"))
