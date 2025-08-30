#!/usr/bin/env python3

from datetime import datetime, timedelta
import os

def get_input(prompt) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print ("Please enter a whole number.\n")

def resolve_date(month: int, day: int) -> datetime:
    now = datetime.now()
    current_year = now.year

    if now.month in (1, 2) and month in (11, 12):
        year = current_year - 1
    else:
        year = current_year

    return datetime(year, month, day)

def date_suffix(n: int) -> str:
    if 11 <= n % 100 <= 13:
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")


def main():
    mileage = 0
    print("Week of expenses:\n")
    month = get_input("Month: ")
    day = get_input("Day: ")
    expense_date = resolve_date(month, day)
    mon_expense_date = expense_date - timedelta(days=expense_date.weekday())

    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    print("\nMileage for the week: \n")
    daily_miles = []
    for name in day_names:
        miles = get_input(f"{name}: ")
        daily_miles.append(miles)
        mileage += miles

    comp_up_to_225 = 0.00000
    comp_over_225 = 0.00000
    if mileage > 225:
        comp_up_to_225 = 131.625
        comp_over_225 = (mileage - 225) * .26
    elif mileage <= 225:
        comp_up_to_225 = mileage * .585
    comp = comp_up_to_225 + comp_over_225
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    subdir = os.path.join(script_dir, "mileage")
    filename = expense_date.strftime("output_%Y_%m_%d.txt")
    if not os.path.exists(subdir):
        os.mkdir(subdir)
    file_path = os.path.join(subdir, filename)
    with open(file_path, "w") as f:
        print(f"\n\nFor week of {expense_date.date()}")
        print(f"\n\nFor week of {expense_date.date()}", file=f)
        for i, miles in enumerate(daily_miles):
            d = mon_expense_date + timedelta(days=i)
            suf = date_suffix(d.day)
            date_str = d.strftime(f"%A, %B {d.day}{suf} %Y")
            print(f"{date_str}: {miles} miles")
            print(f"{date_str}: {miles} miles", file=f)
        print(f"\nMileage total: {mileage}")
        print(f"\nComp for mileage over 225: ${comp_over_225:.2f}", file=f)
        print(f"\nMileage total: {mileage}", file=f)
        print(f"Total compensation: ${comp:.2f}")
        print(f"Total compensation: ${comp:.2f}", file=f)
        print(f"\nMileage (over 225): {mileage - 225}")
        print(f"\nMileage (over 225): {mileage - 225}", file=f)
        print(f"\nComp for mileage over 225: ${comp_over_225:.2f}")
        print(f"\nComp for mileage over 225: ${comp_over_225:.2f}", file=f)
        print("\nDate Created:", datetime.now().strftime("%B %d, %Y %I:%M %p"), file=f)

if __name__ == "__main__":
    main()
