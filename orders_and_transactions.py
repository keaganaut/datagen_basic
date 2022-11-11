import pandas as pd
from faker import Faker
import datetime
import random
import numpy

pd.set_option("display.max_columns", None)
fake = Faker()

fake.seed_instance(4242)
random.seed(4242)

"""
ORDERS
COLUMNS

id: int
customer_id: int
date: date
is_delivery: bool


"""

row_count = 150

order_ids = [i for i in range(row_count)]

order_dates = [
    fake.date_between_dates(
        date_start=datetime.date(2022, 1, 1), date_end=datetime.date(2022, 1, 7)
    )
    for i in range(row_count)
]

order_types = [
    "dine-in" if random.randint(0, 3) == 0 else "delivery" for i in range(row_count)
]

order_cols = {
    "id": order_ids,
    "customer_id": [random.randint(0, 100) for i in range(row_count)],
    "date": order_dates,
    "type": order_types,
}


df_orders = pd.DataFrame(data=order_cols)
df_orders.to_csv("output/orders.csv", index=False)


"""
TRANSACTIONS
COLUMNS

id: int
order_id: int
payment_method: "cash" | "credit_card"
amount_cents: int


"""

random.shuffle(order_ids)

transaction_cols = {
    "id": [i for i in range(row_count)],
    "order_id": order_ids,
    "payment_method": [
        "cash" if random.randint(0, 2) == 0 else "credit_card" for i in range(row_count)
    ],
    "amount_cents": [
        round(
            numpy.random.normal(loc=25, scale=6.5)
            + (4.20 if df_orders["type"][i] == "delivery" else 0),
            2,
        )
        for i in range(row_count)
    ],
}


df_transactions = pd.DataFrame(data=transaction_cols)
df_transactions.to_csv("output/transactions.csv", index=False)
