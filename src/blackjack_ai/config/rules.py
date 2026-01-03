from __future__ import annotations
from typing import Dict, List, Literal
from pydantic import BaseModel, Field, field_validator

class ShoeConfig(BaseModel):
    decks: int = Field(6, ge=1, le=8)
    penetration: float = Field(0.75, gt=0.0, lt=1.0)  # reshuffle when remaining fraction <= (1-penetration)

class TableConfig(BaseModel):
    min_bet_units: int = Field(1, ge=1)
    max_bet_units: int = Field(50, ge=1)
    bet_ramp_units: List[int] = Field(default_factory=lambda: [1, 2, 4, 8, 12, 16, 24, 32, 40, 50])

    @field_validator("bet_ramp_units")
    @classmethod
    def _validate_bet_ramp(cls, v: List[int]) -> List[int]:
        if not v:
            raise ValueError("bet_ramp_units must not be empty")
        if any(x <= 0 for x in v):
            raise ValueError("bet_ramp_units must contain positive integers")
        if sorted(v) != v:
            raise ValueError("bet_ramp_units must be sorted ascending")
        return v

class RulesConfig(BaseModel):
    blackjack_payout: float = Field(1.5, ge=0.0)  # profit multiple on blackjack (3:2 => 1.5)
    dealer_hits_soft_17: bool = True
    dealer_has_hole_card: bool = True
    dealer_peeks_for_blackjack: bool = True

    allow_double: bool = True
    double_after_split: bool = True
    double_on_any_two: bool = True

    allow_split: bool = True
    max_splits: int = Field(3, ge=0, le=10)
    resplit_aces: bool = False
    hit_split_aces: bool = False

    allow_surrender: bool = True

    @field_validator("dealer_peeks_for_blackjack")
    @classmethod
    def _peek_requires_hole_card(cls, v: bool, info) -> bool:
        # If there is no hole card (European no-hole-card), peeking doesn't make sense.
        # We allow it but it should be false in that ruleset; warn by raising.
        dealer_has_hole_card = info.data.get("dealer_has_hole_card", True)
        if v and not dealer_has_hole_card:
            raise ValueError("dealer_peeks_for_blackjack requires dealer_has_hole_card=true")
        return v

class CountingConfig(BaseModel):
    enabled: bool = False
    system: Literal["hilo"] = "hilo"
    true_count_floor: int = Field(-10, ge=-50, le=0)
    true_count_ceil: int = Field(10, ge=0, le=50)

    # Map of true_count (string keys in YAML) to bet units.
    bet_ramp_by_true_count: Dict[str, int] = Field(default_factory=dict)

    @field_validator("bet_ramp_by_true_count")
    @classmethod
    def _validate_bet_ramp_by_tc(cls, v: Dict[str, int]) -> Dict[str, int]:
        # empty ok (fallback will be used)
        for k, bet in v.items():
            try:
                int(k)
            except ValueError as e:
                raise ValueError(f"bet_ramp_by_true_count key must be int-like, got {k!r}") from e
            if bet <= 0:
                raise ValueError("bet_ramp_by_true_count bet units must be > 0")
        return v

class AppConfig(BaseModel):
    shoe: ShoeConfig = ShoeConfig()
    table: TableConfig = TableConfig()
    rules: RulesConfig = RulesConfig()
    counting: CountingConfig = CountingConfig()
