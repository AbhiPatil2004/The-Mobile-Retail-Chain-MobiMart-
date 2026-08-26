import numpy as np
from core.models import Store, PhoneModel, InventoryAllocation

TOTAL_BUDGET = 40000000.0  # ₹4 Crore constraint

def run_weekly_allocation(current_week):
    stores = Store.objects.all()
    phones = PhoneModel.objects.all()
    
    InventoryAllocation.objects.filter(week_number=current_week).delete()
    
    allocations = []
    total_spent = 0.0

    # Demand Scoring Logic
    scored_demands = []
    for store in stores:
        for phone in phones:
            base_demand = 12 if store.tier == 'TIER_1' and phone.category == 'FLAGSHIP' else 25
            if store.tier == 'TIER_2_3' and phone.category == 'FLAGSHIP':
                base_demand = 2  # Low flagship demand in Tier 2/3
            
            # Stockout penalty & profit weighting
            unit_margin = float(phone.selling_price - phone.cost_price)
            expected_revenue = base_demand * float(phone.selling_price)
            score = (expected_revenue * unit_margin) / float(phone.cost_price)

            scored_demands.append({
                'store': store,
                'phone': phone,
                'demand_units': base_demand,
                'unit_cost': float(phone.cost_price),
                'score': score
            })

    # Sort greedy by highest return score per rupee
    scored_demands.sort(key=lambda x: x['score'], reverse=True)

    for item in scored_demands:
        cost = item['demand_units'] * item['unit_cost']
        if total_spent + cost <= TOTAL_BUDGET:
            units = item['demand_units']
            alloc_cost = cost
            total_spent += cost
        else:
            remaining_cap = TOTAL_BUDGET - total_spent
            units = int(remaining_cap // item['unit_cost'])
            alloc_cost = units * item['unit_cost']
            total_spent += alloc_cost

        if units > 0:
            allocations.append(InventoryAllocation(
                store=item['store'],
                phone=item['phone'],
                week_number=current_week,
                allocated_units=units,
                capital_allocated=alloc_cost,
                reasoning_rupees=f"Allocated {units} units. Expected Margin Yield: ₹{(units * (item['phone'].selling_price - item['phone'].cost_price)):,.2f}"
            ))

    InventoryAllocation.objects.bulk_create(allocations)
    return total_spent