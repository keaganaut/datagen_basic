import pandas as pd
from faker import Faker
import datetime
from random import randrange, uniform, randint, choice

pd.set_option("display.max_columns", None)
fake = Faker()

fake.seed_instance(4242)

"""
COLUMNS

id: int
first_name: str
last_name: str

"""

row_count = 100


cols = {

    "id": [i for i in range(row_count)],
    "first_name": [fake.first_name() for i in range(row_count)],
    "last_name": [ fake.last_name() for i in range(row_count)]
}

df = pd.DataFrame(data=cols)
df.to_csv("output/customers.csv", index=False)
