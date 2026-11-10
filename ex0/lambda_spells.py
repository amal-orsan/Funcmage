from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict[str, Any]],
                 min_power: int) -> list[dict[str, Any]]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    max_power = max(mages, key=lambda x: x['power'])['power']
    min_power = min(mages, key=lambda x: x['power'])['power']
    avg_power = round(sum(map(lambda x: x['power'], mages)) / len(mages), 2)
    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Amulet of Strength", "power": 50},
        {"name": "Ring of Wisdom", "power": 30},
        {"name": "Cloak of Invisibility", "power": 70}
    ]

    mages = [
        {"name": "Gandalf", "power": 100},
        {"name": "Merlin", "power": 80},
        {"name": "Morgana", "power": 60}
    ]

    spells = ["fireball", "heal", "shield"]

    sorted_artifacts = artifact_sorter(artifacts)
    filtered_mages = power_filter(mages, 70)
    transformed_spells = spell_transformer(spells)
    stats = mage_stats(mages)

    print("Testing artifact sorter...")
    print(f"{sorted_artifacts[0]['name']} "
          f"({sorted_artifacts[0]['power']} power)"
          f" comes before {sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power']} power)")

    print("\nTesting power filter...")
    print(f"Mages with power >= 70: {[m['name'] for m in filtered_mages]}")

    print("\nTesting spell transformer...")
    print(" ".join(transformed_spells))

    print("\nTesting mage stats...")
    print(stats)
