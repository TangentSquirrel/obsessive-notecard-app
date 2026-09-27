from __future__ import annotations

from typing import Any


class ValidationError(Exception):
    pass


def validate_library(library: dict[str, Any]) -> None:
    errors: list[str] = []
    if "schemaVersion" not in library:
        errors.append("missing schemaVersion")
    if "id" not in library:
        errors.append("missing id")

    dim_defs = {d["id"]: d for d in library.get("dimensionDefinitions") or []}
    dim_value_ids: dict[str, set[str]] = {}
    for d in library.get("dimensionDefinitions") or []:
        if "id" not in d:
            errors.append("dimension definition missing id")
            continue
        dim_value_ids[d["id"]] = {v["id"] for v in d.get("values") or [] if "id" in v}

    catalog_dims: dict[str, dict[str, str]] = {}
    for entry in library.get("tenseCatalog") or []:
        tid = entry.get("id")
        dims = entry.get("dimensions")
        if tid and isinstance(dims, dict):
            catalog_dims[tid] = dims

    unit_ids: set[str] = set()
    for verb in library.get("verbs") or []:
        if "id" not in verb:
            errors.append("verb missing id")
            continue
        for unit in verb.get("units") or []:
            uid = unit.get("id")
            if not uid:
                errors.append(f"verb {verb['id']}: unit missing id")
                continue
            if uid in unit_ids:
                errors.append(f"duplicate unit id: {uid}")
            unit_ids.add(uid)
            tense_id = unit.get("tenseId")
            if not tense_id:
                errors.append(f"unit {uid}: missing tenseId")
            elif tense_id not in catalog_dims:
                errors.append(f"unit {uid}: tenseId {tense_id!r} not in tenseCatalog")
            else:
                expected = catalog_dims[tense_id]
                ud = unit.get("dimensions") or {}
                for axis in ("time", "mood", "aspect"):
                    if ud.get(axis) != expected.get(axis):
                        errors.append(
                            f"unit {uid}: dimensions.{axis}={ud.get(axis)!r} "
                            f"but tenseCatalog expects {expected.get(axis)!r}"
                        )
            answers = unit.get("answers")
            if not answers:
                errors.append(f"unit {uid}: missing answers")
            for dim_id, val_id in (unit.get("dimensions") or {}).items():
                if dim_id not in dim_defs:
                    errors.append(f"unit {uid}: unknown dimension {dim_id!r}")
                elif val_id not in dim_value_ids.get(dim_id, set()):
                    allowed_ids = dim_value_ids.get(dim_id, set())
                    if val_id not in allowed_ids:
                        errors.append(
                            f"unit {uid}: invalid value {val_id!r} for dimension {dim_id!r}"
                        )

    if errors:
        raise ValidationError("\n".join(errors))
