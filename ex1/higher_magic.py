from collections.abc import Callable


def spell_combiner(
        spell1: Callable[[str, int], str],
        spell2: Callable[[str, int], str]
        ) -> Callable[[str, int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(
        base_spell: Callable[[str, int], str],
        multiplier: int
        ) -> Callable[[str, int], str]:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(
        condition: Callable[[str, int], bool],
        spell: Callable[[str, int], str]
        ) -> Callable[[str, int], str]:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return caster


def spell_sequence(
        spells: list[Callable[[str, int], str]]
        ) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} with {power} power!"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def is_powerful(target: str, power: int) -> bool:
        return power > 50

    print("Testing spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined_spell('Dragon', 10)}")

    print("\nTesting power amplifier...")
    amplified_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Goblin', 10)}")
    print(f"Amplified: {amplified_fireball('Goblin', 10)}")

    print("\nTesting conditional caster...")
    conditional_fireball = conditional_caster(is_powerful, fireball)
    print(conditional_fireball("Dragon", 60))
    print(conditional_fireball("Troll", 40))

    print("\nTesting spell sequence...")
    sequence_spell = spell_sequence([fireball, heal])
    print(sequence_spell("Elf", 20))
