import random
from core.models import Store, PhoneModel

def seed_database():
    Store.objects.all().delete()
    PhoneModel.objects.all().delete()

    # 1. 25 Stores Setup (8 Bangalore + 17 Tier-2/3)
    bangalore_areas = ['Indiranagar', 'Koramangala', 'Jayanagar', 'Whitefield', 'HSR Layout', 'Malleshwaram', 'MG Road', 'Electronic City']
    tier2_cities = ['Mysore', 'Hubli', 'Tumkur', 'Davangere', 'Belgaum', 'Mangalore', 'Shimoga', 'Gulbarga', 'Bellary', 'Udupi', 'Hassan', 'Bidar', 'Hospet', 'Gadag', 'Robertsonpet', 'Bhadravati', 'Chitradurga']

    for area in bangalore_areas:
        Store.objects.create(name=f"MobiMart {area}", city="Bangalore", tier="TIER_1")

    for city in tier2_cities:
        Store.objects.create(name=f"MobiMart {city}", city=city, tier="TIER_2_3")

    # 2. 60 Phone Models Setup
    categories = [('BUDGET', 8000, 10000), ('MID', 22000, 26000), ('FLAGSHIP', 75000, 85000)]
    for i in range(1, 61):
        cat, cp_base, sp_base = random.choice(categories)
        is_eol = True if i % 10 == 0 else False
        PhoneModel.objects.create(
            name=f"PhoneModel-{i:02d}",
            category=cat,
            cost_price=cp_base + random.randint(-1000, 1000),
            selling_price=sp_base + random.randint(1000, 3000),
            launch_week=random.randint(1, 20),
            is_eol=is_eol
        )
    print("Database successfully seeded with 25 Stores and 60 Models.")



