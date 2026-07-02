from typing import Dict, Any

class ShippingEstimatorClient:
    def estimate_shipping(self, weight_lbs: float, source_zip: str, dest_zip: str) -> Dict[str, Any]:
        # Simple distance logic
        zone = abs(int(source_zip[:3]) - int(dest_zip[:3])) // 100
        zone = max(1, min(8, zone))
        
        base_rate = 5.00 + (weight_lbs * 0.75)
        rates = {
            "Standard": round(base_rate + (zone * 0.50), 2),
            "Expedited": round((base_rate * 1.5) + (zone * 1.00), 2),
            "Next-Day": round((base_rate * 3.0) + (zone * 2.00), 2)
        }
        return {"delivery_estimates": rates, "shipping_zone": zone}
