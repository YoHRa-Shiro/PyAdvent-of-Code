def snake_to_tile_case(snake_string: str) -> str:
    return snake_string.replace("_", " ").replace(".py", "").title()
