def calculate_resources_per_turn(field_type):
    # We assume that that
    if field_type == "1":
        return 10, 0 # 10 wood, 0 iron

    elif field_type == "2":
        return 0, 10 # 0 wood, 10 iron

    else:
        return 5, 5 # 5 wood, 5 iron