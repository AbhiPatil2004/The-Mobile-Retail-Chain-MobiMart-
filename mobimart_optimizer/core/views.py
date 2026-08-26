from django.shortcuts import render
from django.db.models import Sum
from .models import InventoryAllocation, Store, PhoneModel
from .services.allocation_engine import run_weekly_allocation

def dashboard_view(request):
    current_week = int(request.GET.get('week', 1))

    # Trigger allocation on demand
    if 'run_allocation' in request.GET:
        run_weekly_allocation(current_week)

    allocations = InventoryAllocation.objects.filter(week_number=current_week).select_related('store', 'phone')
    total_capital_deployed = allocations.aggregate(Sum('capital_allocated'))['capital_allocated__sum'] or 0.0

    # Risk summary
    at_risk_models = PhoneModel.objects.filter(is_eol=True)
    
    context = {
        'current_week': current_week,
        'allocations': allocations[:50],
        'total_capital': total_capital_deployed,
        'remaining_budget': 40000000.0 - float(total_capital_deployed),
        'at_risk_count': at_risk_models.count(),
        'total_stores': Store.objects.count(),
    }
    return render(request, 'core/dashboard.html', context)