#!/usr/bin/env python3
"""
CBM & Container Logistics Economics Calculator for B2B Export Sites.
Used for verifying packaging data and estimating per-unit shipping amortizations.
"""

def calculate_shipping_breakdown(quantity: int, unit_weight_g: float = 6.8, pcs_per_ctn: int = 2500,
                                 ctn_cbm: float = 0.037632, ctn_gross_kg: float = 18.0,
                                 ocean_freight_40hq_usd: float = 3200.0):
    import math

    total_cartons = math.ceil(quantity / pcs_per_ctn)
    total_cbm = round(total_cartons * ctn_cbm, 4)
    total_weight_kg = round(total_cartons * ctn_gross_kg, 2)
    
    # 20GP capacity: ~28 CBM (~744 cartons)
    # 40HQ capacity: ~68 CBM (~1807 cartons)
    twenty_gp_utilization = round((total_cartons / 744.0) * 100, 1)
    forty_hq_utilization = round((total_cartons / 1807.0) * 100, 1)

    # Unit shipping cost in a full 40HQ container (1,807 cartons * 2,500 pcs = 4,517,500 pcs)
    full_40hq_units = 1807 * pcs_per_ctn
    amortized_shipping_per_unit = round(ocean_freight_40hq_usd / full_40hq_units, 4)

    return {
        "quantity": quantity,
        "total_cartons": total_cartons,
        "total_cbm": total_cbm,
        "total_weight_kg": total_weight_kg,
        "20gp_utilization_percent": min(twenty_gp_utilization, 100.0),
        "40hq_utilization_percent": min(forty_hq_utilization, 100.0),
        "full_40hq_amortized_unit_freight_usd": amortized_shipping_per_unit
    }

if __name__ == "__main__":
    import sys
    test_qty = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
    res = calculate_shipping_breakdown(test_qty)
    print("=== Shipping Economics Breakdown ===")
    for k, v in res.items():
        print(f"{k}: {v}")
