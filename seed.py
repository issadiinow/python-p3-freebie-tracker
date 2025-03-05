#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, Company, Dev, Freebie
from lib.db import session



# Create database connection
engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data (optional)
session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()

# Create sample companies
google = Company(name="Google", founding_year=1998)
microsoft = Company(name="Microsoft", founding_year=1975)

# Create sample developers
alice = Dev(name="Alice")
bob = Dev(name="Bob")

# Create sample freebies
freebie1 = Freebie(item_name="T-shirt", value=15, company=google, dev=alice)
freebie2 = Freebie(item_name="Mug", value=10, company=microsoft, dev=bob)

# Add everything to session and commit
session.add_all([google, microsoft, alice, bob, freebie1, freebie2])
session.commit()

print("Database seeded successfully!")

# Close session
session.close()
