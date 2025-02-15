def pirate_ship():
    capacity, num_items = map(int, input().split())
    items = []
    for _ in range(num_items):
        name, weight, value = input().split()
        weight, value = float(weight), float(value)
        if weight <= capacity:
            value_per_unit = value / weight
            items.append((name, weight, value, value_per_unit))

    if not items:
        print("")
        return
    items.sort(key=lambda x: (-x[3], -x[2]))
    
    loaded_items = []
    current_weight = 0

    for name, weight, value, value_per_unit in items:
        if current_weight + weight <= capacity:
            loaded_items.append((name, weight, value))
            current_weight += weight
        else:
            remaining_capacity = capacity - current_weight
            if remaining_capacity > 0:
                partial_weight = remaining_capacity
                partial_value = remaining_capacity * value_per_unit
                loaded_items.append((name, partial_weight, partial_value))
            break

    for name, weight, value in loaded_items:
        print(f"{name} {weight:.1f} {value:.2f}")

if __name__ == "__main__":
    pirate_ship()