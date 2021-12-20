from finance_data import MacrotrendsReader, TickerError
from finance_data.utils import MACROTRENDS_CONVERSION
import pytest

def test_default():
    data = MacrotrendsReader("AAPL").read()
    assert (
        ("income_statement" in data.keys())
        and ("balance_sheet" in data.keys())
        and ("cashflow_statement" in data.keys())
    )
    assert all(
        key in (data["income_statement"] | data["balance_sheet"] | data["cashflow_statement"])
        for key in MACROTRENDS_CONVERSION.values()
    )

def test_quarterly():
    data = MacrotrendsReader("AAPL", frequency="quarterly").read()
    assert (
        ("income_statement" in data.keys())
        and ("balance_sheet" in data.keys())
        and ("cashflow_statement" in data.keys())
    )

def test_hyphen_to_dot():
    data = MacrotrendsReader("BRK-A", frequency="quarterly").read()
    assert (
        ("income_statement" in data.keys())
        and ("balance_sheet" in data.keys())
        and ("cashflow_statement" in data.keys())
    )

def test_no_data():
    with pytest.raises(TickerError):
        MacrotrendsReader("PLACEHOLDER", frequency="quarterly").read()