from functools import wraps
import time
from collections.abc import Callable
from typing import Any
import random


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = round(time.time() - start_time, 3)
        print(f"Spell completed in {elapsed} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get('power', args[-1] if args else 0)
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            c.isalpha() or c.isspace() for c in name
        )

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball(target: str) -> str:
        return f"{target} cast!"

    result = fireball("Fireball")
    print(f"Result: {result}")

    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def unstable_spell(target: str) -> str:
        if random.random() < 0.7:
            raise Exception("Spell fizzled randomly")
        return f"{target} spelled!"

    result = unstable_spell("Waaaaaaagh")
    print(result)

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("G1"))

    guild = MageGuild()
    print(guild.cast_spell("Fireball", power=15))
    print(guild.cast_spell("Ice Shard", power=5))
