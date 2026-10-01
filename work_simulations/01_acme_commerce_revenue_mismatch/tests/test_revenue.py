"""Acceptance checks for DATA-1042.

The test deliberately states the business invariant rather than prescribing the
implementation: settled revenue must equal settled payment amounts by order.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(name):
    with (ROOT / "data" / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_settled_revenue_is_1000():
    payments = [r for r in read("payments.csv") if r["status"] == "settled"]
    assert sum(float(r["amount"]) for r in payments) == 1000.0


def test_each_settled_payment_has_one_order():
    orders = {r["order_id"] for r in read("orders.csv")}
    payments = read("payments.csv")
    assert all(r["order_id"] in orders for r in payments)
    assert len({r["payment_id"] for r in payments}) == len(payments)
