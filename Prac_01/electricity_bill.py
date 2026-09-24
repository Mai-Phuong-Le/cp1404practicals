"""Electricity Bill estimator"""
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
print("Electricity Bill Estimator 2.0")
print("Which tariff? 11 or 31", end="")
if int(input()) == 11:
    tariff = TARIFF_11
elif int(input()) == 31:
    tariff = TARIFF_31
daily_use_in_kWh = float(input("Enter daily use in kWh: "))
number_of_billing_days = float(input("Enter number of billing days: "))
estimated_bill = tariff * daily_use_in_kWh * number_of_billing_days
print(f"Estimated bill: ${estimated_bill:.2f}")
