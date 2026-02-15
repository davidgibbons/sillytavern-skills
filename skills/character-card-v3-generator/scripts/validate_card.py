#!/usr/bin/env python3
"""Lightweight validator for Character Card V3 JSON files."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_DATA_FIELDS = [
    "name",
    "description",
    "tags",
    "creator",
    "character_version",
    "mes_example",
    "extensions",
    "system_prompt",
    "post_history_instructions",
    "first_mes",
    "alternate_greetings",
    "personality",
    "scenario",
    "creator_notes",
    "group_only_greetings",
]


class ValidationError(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def is_str_list(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value)


def validate_entry(entry: Any, idx: int) -> None:
    prefix = f"data.character_book.entries[{idx}]"
    require(isinstance(entry, dict), f"{prefix} must be an object")

    for field in ["keys", "content", "extensions", "enabled", "insertion_order", "use_regex"]:
        require(field in entry, f"{prefix}.{field} is required")

    require(is_str_list(entry["keys"]), f"{prefix}.keys must be string[]")
    require(isinstance(entry["content"], str), f"{prefix}.content must be string")
    require(isinstance(entry["extensions"], dict), f"{prefix}.extensions must be object")
    require(isinstance(entry["enabled"], bool), f"{prefix}.enabled must be boolean")
    require(
        isinstance(entry["insertion_order"], (int, float)),
        f"{prefix}.insertion_order must be number",
    )
    require(isinstance(entry["use_regex"], bool), f"{prefix}.use_regex must be boolean")

    if "secondary_keys" in entry:
        require(is_str_list(entry["secondary_keys"]), f"{prefix}.secondary_keys must be string[]")
    if "selective" in entry:
        require(isinstance(entry["selective"], bool), f"{prefix}.selective must be boolean")


def validate_card(payload: Any) -> None:
    require(isinstance(payload, dict), "Card root must be an object")
    require(payload.get("spec") == "chara_card_v3", "spec must be 'chara_card_v3'")
    require(payload.get("spec_version") == "3.0", "spec_version must be '3.0'")

    data = payload.get("data")
    require(isinstance(data, dict), "data must be an object")

    for field in REQUIRED_DATA_FIELDS:
        require(field in data, f"data.{field} is required")

    require(isinstance(data["name"], str), "data.name must be string")
    require(isinstance(data["description"], str), "data.description must be string")
    require(isinstance(data["personality"], str), "data.personality must be string")
    require(isinstance(data["scenario"], str), "data.scenario must be string")
    require(isinstance(data["first_mes"], str), "data.first_mes must be string")
    require(isinstance(data["mes_example"], str), "data.mes_example must be string")
    require(isinstance(data["creator_notes"], str), "data.creator_notes must be string")
    require(is_str_list(data["tags"]), "data.tags must be string[]")
    require(isinstance(data["creator"], str), "data.creator must be string")
    require(isinstance(data["character_version"], str), "data.character_version must be string")
    require(isinstance(data["extensions"], dict), "data.extensions must be object")
    require(isinstance(data["system_prompt"], str), "data.system_prompt must be string")
    require(
        isinstance(data["post_history_instructions"], str),
        "data.post_history_instructions must be string",
    )
    require(is_str_list(data["alternate_greetings"]), "data.alternate_greetings must be string[]")
    require(is_str_list(data["group_only_greetings"]), "data.group_only_greetings must be string[]")

    if "source" in data:
        require(is_str_list(data["source"]), "data.source must be string[]")
    if "creator_notes_multilingual" in data:
        multilingual = data["creator_notes_multilingual"]
        require(isinstance(multilingual, dict), "data.creator_notes_multilingual must be object")
        for key, value in multilingual.items():
            require(isinstance(key, str), "data.creator_notes_multilingual keys must be strings")
            require(
                isinstance(value, str),
                "data.creator_notes_multilingual values must be strings",
            )
    if "creation_date" in data:
        require(isinstance(data["creation_date"], (int, float)), "data.creation_date must be number")
    if "modification_date" in data:
        require(
            isinstance(data["modification_date"], (int, float)),
            "data.modification_date must be number",
        )

    if "assets" in data:
        require(isinstance(data["assets"], list), "data.assets must be array")
        for idx, asset in enumerate(data["assets"]):
            prefix = f"data.assets[{idx}]"
            require(isinstance(asset, dict), f"{prefix} must be object")
            for field in ["type", "uri", "name", "ext"]:
                require(field in asset, f"{prefix}.{field} is required")
                require(isinstance(asset[field], str), f"{prefix}.{field} must be string")

    if "character_book" in data:
        book = data["character_book"]
        require(isinstance(book, dict), "data.character_book must be object")
        require(isinstance(book.get("extensions"), dict), "data.character_book.extensions must be object")
        entries = book.get("entries")
        require(isinstance(entries, list), "data.character_book.entries must be array")
        for idx, entry in enumerate(entries):
            validate_entry(entry, idx)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_card.py <path-to-card.json>")
        return 1

    card_path = Path(sys.argv[1])
    if not card_path.exists():
        print(f"[ERROR] File not found: {card_path}")
        return 1

    try:
        payload = json.loads(card_path.read_text())
        validate_card(payload)
    except json.JSONDecodeError as exc:
        print(f"[ERROR] Invalid JSON: {exc}")
        return 1
    except ValidationError as exc:
        print(f"[ERROR] {exc}")
        return 1

    print("[OK] Card looks valid for CCv3 core structure.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
