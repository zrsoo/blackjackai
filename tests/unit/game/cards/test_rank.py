import pytest
from src.blackjack_ai.game.cards.rank import Rank


class TestRankEnum:
    """Test basic enum functionality and values."""
    
    def test_enum_values(self):
        """Test that all rank values are correct."""
        assert Rank.ACE == 1
        assert Rank.TWO == 2
        assert Rank.THREE == 3
        assert Rank.FOUR == 4
        assert Rank.FIVE == 5
        assert Rank.SIX == 6
        assert Rank.SEVEN == 7
        assert Rank.EIGHT == 8
        assert Rank.NINE == 9
        assert Rank.TEN == 10
    
    def test_enum_count(self):
        """Test that we have exactly 10 ranks."""
        ranks = list(Rank)
        assert len(ranks) == 10
    
    def test_enum_iteration(self):
        """Test that we can iterate over all ranks."""
        expected_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual_values = [int(rank) for rank in Rank]
        assert actual_values == expected_values
    
    def test_int_conversion(self):
        """Test that ranks can be converted to integers."""
        assert int(Rank.ACE) == 1
        assert int(Rank.FIVE) == 5
        assert int(Rank.TEN) == 10
    
    def test_comparison_operations(self):
        """Test that ranks can be compared as integers."""
        assert Rank.ACE < Rank.TWO
        assert Rank.NINE < Rank.TEN
        assert Rank.ACE <= Rank.ACE
        assert Rank.TEN > Rank.NINE
        assert Rank.FIVE == Rank.FIVE
        assert Rank.ACE != Rank.TEN


class TestFromInt:
    """Test Rank.from_int class method."""
    
    def test_valid_integers(self):
        """Test creating ranks from valid integers 1-10."""
        assert Rank.from_int(1) == Rank.ACE
        assert Rank.from_int(2) == Rank.TWO
        assert Rank.from_int(3) == Rank.THREE
        assert Rank.from_int(4) == Rank.FOUR
        assert Rank.from_int(5) == Rank.FIVE
        assert Rank.from_int(6) == Rank.SIX
        assert Rank.from_int(7) == Rank.SEVEN
        assert Rank.from_int(8) == Rank.EIGHT
        assert Rank.from_int(9) == Rank.NINE
        assert Rank.from_int(10) == Rank.TEN
    
    def test_invalid_integers_below_range(self):
        """Test that integers below 1 raise ValueError."""
        with pytest.raises(ValueError, match="expects value in the \\[1, 10\\] interval, got 0"):
            Rank.from_int(0)
        
        with pytest.raises(ValueError, match="expects value in the \\[1, 10\\] interval, got -1"):
            Rank.from_int(-1)
        
        with pytest.raises(ValueError, match="expects value in the \\[1, 10\\] interval, got -10"):
            Rank.from_int(-10)
    
    def test_invalid_integers_above_range(self):
        """Test that integers above 10 raise ValueError."""
        with pytest.raises(ValueError, match="expects value in the \\[1, 10\\] interval, got 11"):
            Rank.from_int(11)
        
        with pytest.raises(ValueError, match="expects value in the \\[1, 10\\] interval, got 13"):
            Rank.from_int(13)
        
        with pytest.raises(ValueError, match="expects value in the \\[1, 10\\] interval, got 100"):
            Rank.from_int(100)
    
    def test_non_integer_types(self):
        """Test that non-integer types raise TypeError."""
        with pytest.raises(TypeError, match="Rank.from_int expects int, got float"):
            Rank.from_int(5.0) # type: ignore
        
        with pytest.raises(TypeError, match="Rank.from_int expects int, got str"):
            Rank.from_int("5") # type: ignore
        
        with pytest.raises(TypeError, match="Rank.from_int expects int, got NoneType"):
            Rank.from_int(None) # type: ignore
        
        with pytest.raises(TypeError, match="Rank.from_int expects int, got list"):
            Rank.from_int([5]) # type: ignore


class TestFromStr:
    """Test Rank.from_str class method."""
    
    def test_ace_strings(self):
        """Test creating ACE from various ace strings."""
        assert Rank.from_str("A") == Rank.ACE
        assert Rank.from_str("a") == Rank.ACE
        assert Rank.from_str(" A ") == Rank.ACE  # with whitespace
    
    def test_numeric_strings(self):
        """Test creating ranks from numeric strings 2-9."""
        assert Rank.from_str("2") == Rank.TWO
        assert Rank.from_str("3") == Rank.THREE
        assert Rank.from_str("4") == Rank.FOUR
        assert Rank.from_str("5") == Rank.FIVE
        assert Rank.from_str("6") == Rank.SIX
        assert Rank.from_str("7") == Rank.SEVEN
        assert Rank.from_str("8") == Rank.EIGHT
        assert Rank.from_str("9") == Rank.NINE
    
    def test_ten_value_strings(self):
        """Test creating TEN from various ten-value strings."""
        assert Rank.from_str("10") == Rank.TEN
        assert Rank.from_str("T") == Rank.TEN
        assert Rank.from_str("t") == Rank.TEN
        assert Rank.from_str("J") == Rank.TEN
        assert Rank.from_str("j") == Rank.TEN
        assert Rank.from_str("Q") == Rank.TEN
        assert Rank.from_str("q") == Rank.TEN
        assert Rank.from_str("K") == Rank.TEN
        assert Rank.from_str("k") == Rank.TEN
    
    def test_whitespace_handling(self):
        """Test that whitespace is properly handled."""
        assert Rank.from_str(" 5 ") == Rank.FIVE
        assert Rank.from_str("  K  ") == Rank.TEN
        assert Rank.from_str("\t7\n") == Rank.SEVEN
    
    def test_invalid_strings(self):
        """Test that invalid strings raise ValueError."""
        with pytest.raises(ValueError, match="Invalid rank string, expected \\[A, 2..9, 10\\], got 'B'"):
            Rank.from_str("B")
        
        with pytest.raises(ValueError, match="Invalid rank string, expected \\[A, 2..9, 10\\], got '1'"):
            Rank.from_str("1")
        
        with pytest.raises(ValueError, match="Invalid rank string, expected \\[A, 2..9, 10\\], got '11'"):
            Rank.from_str("11")
        
        with pytest.raises(ValueError, match="Invalid rank string, expected \\[A, 2..9, 10\\], got ''"):
            Rank.from_str("")
        
        with pytest.raises(ValueError, match="Invalid rank string, expected \\[A, 2..9, 10\\], got 'AA'"):
            Rank.from_str("AA")
    
    def test_non_string_types(self):
        """Test that non-string types raise TypeError."""
        with pytest.raises(TypeError, match="Rank.from_str expects int, got int"):
            Rank.from_str(5) # type: ignore
        
        with pytest.raises(TypeError, match="Rank.from_str expects int, got NoneType"):
            Rank.from_str(None) # type: ignore
        
        with pytest.raises(TypeError, match="Rank.from_str expects int, got list"):
            Rank.from_str(["A"]) # type: ignore


class TestStringFormatting:
    """Test string representation methods."""
    
    def test_to_string(self):
        """Test to_string method."""
        assert Rank.ACE.to_string() == "A"
        assert Rank.TWO.to_string() == "2"
        assert Rank.FIVE.to_string() == "5"
        assert Rank.NINE.to_string() == "9"
        assert Rank.TEN.to_string() == "10"
    
    def test_str_method(self):
        """Test __str__ method."""
        assert str(Rank.ACE) == "A"
        assert str(Rank.THREE) == "3"
        assert str(Rank.SEVEN) == "7"
        assert str(Rank.TEN) == "10"
    
    def test_str_consistency(self):
        """Test that str() and to_string() return the same values."""
        for rank in Rank:
            assert str(rank) == rank.to_string()


class TestBlackjackProperties:
    """Test blackjack-specific properties."""
    
    def test_is_ace_property(self):
        """Test is_ace property."""
        assert Rank.ACE.is_ace is True
        
        # All other ranks should not be ace
        for rank in [Rank.TWO, Rank.THREE, Rank.FOUR, Rank.FIVE, 
                    Rank.SIX, Rank.SEVEN, Rank.EIGHT, Rank.NINE, Rank.TEN]:
            assert rank.is_ace is False
    
    def test_is_ten_value_property(self):
        """Test is_ten_value property."""
        assert Rank.TEN.is_ten_value is True
        
        # All other ranks should not be ten-value
        for rank in [Rank.ACE, Rank.TWO, Rank.THREE, Rank.FOUR, 
                    Rank.FIVE, Rank.SIX, Rank.SEVEN, Rank.EIGHT, Rank.NINE]:
            assert rank.is_ten_value is False


class TestHiLoCountingSystem:
    """Test Hi-Lo counting system tags."""
    
    def test_low_cards_plus_one(self):
        """Test that cards 2-6 have +1 tag."""
        low_cards = [Rank.TWO, Rank.THREE, Rank.FOUR, Rank.FIVE, Rank.SIX]
        for rank in low_cards:
            assert rank.hilo_tag() == 1
    
    def test_neutral_cards_zero(self):
        """Test that cards 7-9 have 0 tag."""
        neutral_cards = [Rank.SEVEN, Rank.EIGHT, Rank.NINE]
        for rank in neutral_cards:
            assert rank.hilo_tag() == 0
    
    def test_high_cards_minus_one(self):
        """Test that ACE and TEN have -1 tag."""
        high_cards = [Rank.ACE, Rank.TEN]
        for rank in high_cards:
            assert rank.hilo_tag() == -1
    
    def test_all_ranks_have_valid_tags(self):
        """Test that all ranks return valid Hi-Lo tags."""
        valid_tags = {-1, 0, 1}
        for rank in Rank:
            assert rank.hilo_tag() in valid_tags


class TestEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_rank_identity(self):
        """Test that ranks maintain identity."""
        ace1 = Rank.ACE
        ace2 = Rank.from_int(1)
        ace3 = Rank.from_str("A")
        
        assert ace1 is ace2
        assert ace1 is ace3
        assert ace2 is ace3
    
    def test_rank_membership(self):
        """Test membership in Rank enum."""
        assert Rank.ACE in Rank
        assert Rank.TEN in Rank
        assert 1 in Rank
        assert 11 not in Rank
    
    def test_rank_comparison_with_integers(self):
        """Test that ranks can be compared with integers."""
        assert Rank.ACE == 1
        assert Rank.TEN == 10
        assert Rank.FIVE < 6
        assert Rank.NINE > 8
    
    def test_arithmetic_operations(self):
        """Test arithmetic operations with ranks."""
        # These work because Rank inherits from IntEnum
        assert Rank.ACE + 1 == 2
        assert Rank.TEN - 1 == 9
        assert Rank.FIVE * 2 == 10
        assert Rank.EIGHT // 2 == 4


class TestDocstringExamples:
    """Test examples that might be in documentation."""
    
    def test_common_usage_patterns(self):
        """Test common ways the Rank class would be used."""
        # Creating from different sources
        ace_from_int = Rank.from_int(1)
        ace_from_str = Rank.from_str("A")
        ten_from_str = Rank.from_str("K")  # King maps to TEN
        
        # Properties
        assert ace_from_int.is_ace
        assert not ten_from_str.is_ace
        assert ten_from_str.is_ten_value
        
        # String representation
        assert str(ace_from_str) == "A"
        assert str(ten_from_str) == "10"
        
        # Counting system
        assert ace_from_int.hilo_tag() == -1
        assert Rank.FIVE.hilo_tag() == 1
        assert Rank.EIGHT.hilo_tag() == 0