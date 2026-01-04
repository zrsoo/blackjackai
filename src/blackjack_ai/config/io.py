from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

import yaml

from .rules import AppConfig

def load_config(path: str | Path) -> AppConfig:
    p = Path(path)
    data = yaml.safe_load(p.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Config root must be a mapping/dict")
    return AppConfig.model_validate(data)

def save_config(cfg: AppConfig, path: str | Path) -> None:
    p = Path(path)
    d: Dict[str, Any] = cfg.model_dump(mode="json")
    p.write_text(yaml.safe_dump(d, sort_keys=False), encoding="utf-8")