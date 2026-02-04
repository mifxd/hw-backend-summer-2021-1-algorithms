__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    second = seconds % 60

    res = f"{second:02}s"

    if minutes > 0 or hours > 0 or days > 0:
        res = f"{minutes:02}m" + res
    if hours > 0 or days > 0:
        res = f"{hours:02}h" + res
    if days > 0:
        res = f"{days:02}d" + res

    return res
