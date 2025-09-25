import array

def wholesaler_order_picker():
    # --- 1. Integers: generate or input integer values (e.g. order quantities) ---
    # Suppose we have 5 orders with picked quantities (units) for a wholesaler:
    picked_quantities = [120, 85, 150, 100, 95]  # integers
    
    total = sum(picked_quantities)
    average = total / len(picked_quantities)
    minimum = min(picked_quantities)
    maximum = max(picked_quantities)
    
    # --- 2. Strings: create a formatted string report using f-strings ---
    report_header = f"Wholesaler Order Picker Report\n" \
                    f"Number of orders: {len(picked_quantities)}"
    report_stats = (f"Total picked quantity = {total}, "
                    f"Average per order = {average:.2f}")
    
    # More lines
    detail_lines = []
    for idx, qty in enumerate(picked_quantities, start=1):
        detail_lines.append(f"  Order {idx}: {qty} units")
    report_details = "\n".join(detail_lines)
    
    full_report = "\n".join([report_header, report_stats, report_details])
    print(full_report)
    
    # --- 3. Booleans: threshold check on average with compound condition ---
    threshold = 110
    # Use a compound boolean: average > threshold OR maximum > threshold * 1.2
    if (average > threshold) or (maximum > threshold * 1.2):
        print("Status: Above Standard")
    else:
        print("Status: Below Standard")
    
    # --- 4. Lists: maintain a list of items or records ---
    # Let's maintain a list of SKUs (by name) that were processed:
    sku_list = ["SKU-A", "SKU-C", "SKU-B", "SKU-D"]
    print("Before modification, SKU list:", sku_list)
    
    # Add a new element:
    sku_list.append("SKU-E")
    # Remove one based on a condition: remove any SKU whose name contains 'C'
    sku_list = [sku for sku in sku_list if "C" not in sku]
    print("After removal, SKU list:", sku_list)
    
    # Sort and display:
    sku_list.sort()
    print("Sorted SKU list:", sku_list)
    
    # --- 5. Arrays: use Python’s array module for a fixed-size numeric subset ---
    # Use a small subset, say first 3 picked quantities
    arr = array.array('i', picked_quantities[:3])  # type 'i' for signed int :contentReference[oaicite:0]{index=0}
    arr_sum = sum(arr)
    list_sum = sum(picked_quantities[:3])
    print("Array subset:", list(arr))
    print(f"Sum via array = {arr_sum}, sum via list slice = {list_sum}")
    
    # Compare sums:
    if arr_sum == list_sum:
        print("Array sum matches list sum.")
    else:
        print("Mismatch in sums!")
    
    # --- 6. Dictionaries: build list of dicts, update, delete, compute total value field ---
    records = [
        {"id": 1, "name": "Order1", "value": 500},
        {"id": 2, "name": "Order2", "value": 300},
        {"id": 3, "name": "Order3", "value": 450},
    ]
    # Update one record: increase value of id=2
    for rec in records:
        if rec["id"] == 2:
            rec["value"] += 50  # now value becomes 350
    
    # Delete one record: remove id=3
    records = [rec for rec in records if rec["id"] != 3]
    
    # Compute total of “value” fields
    total_value = sum(rec["value"] for rec in records)
    print("Remaining records:", records)
    print(f"Total value across records = {total_value}")
    

# Run the function
if __name__ == "__main__":
    wholesaler_order_picker()


