from enum import IntEnum

class Rank(IntEnum):
    """
    Blackjack rank identity (no suits)
    Domain: A, 2, 3, ..., 10 (where 10 covers 10/J/Q/K)
    """
    
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10 # 10-value bucket: 10/J/Q/K
    
    # --- Constructors / validation ---
    @classmethod
    def from_int(cls, v: int) -> "Rank":
        """
        Accepts integers 1..10 only. Rejects everything else
        """
        if not isinstance(v, int):
            raise TypeError(f"Rank.from_int expects int, got {type(v).__name__}")
        
        if v < 1 or v > 10:
            raise ValueError(f"Rank.from_int expects value in the [1, 10] interval, got {v}")
        
        return cls(v)
    
    @classmethod
    def from_str(cls, s: str) -> "Rank":
        """
        Accepts: "A", "2"..."10" or "J", "Q", "K", "T" as TEN
        Normalizes to the Rank domain
        """
        if not isinstance(s, str):
            raise TypeError(f"Rank.from_str expects int, got {type(s).__name__}")
        
        t = s.strip().upper()
        
        if t == "A":
            return cls.ACE
        if t in {"10", "T", "J", "Q", "K"}:
            return cls.TEN
        if t.isdigit():
            v = int(t)
            if 2 <= v <= 9:
                return cls(v)
        
        raise ValueError(f"Invalid rank string, expected [A, 2..9, 10], got {s!r}")
    
    # --- Debug/log formatting ---

    def to_string(self) -> str:
        return "A" if self is Rank.ACE else str(int(self))

    def __str__(self) -> str:
        return self.to_string()
    
    # --- Blackjack / counting semantics ---
    @property
    def is_ace(self) -> bool:
        return self is Rank.ACE
    
    @property
    def is_ten_value(self) -> bool:
        return self is Rank.TEN
    
    def hilo_tag(self) -> int:
        """
        Hi-Lo counting tags:
        2-6 => +1
        7-9 => 0
        10 / A => -1
        """
        v = int(self)
        
        if 2 <= v <= 6:
            return 1
        if 7 <= v <= 9:
            return 0
        
        # ACE(1) and TEN(10)
        return -1