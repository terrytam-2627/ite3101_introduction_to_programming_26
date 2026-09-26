def shut_down(s: str) -> str:
    if s == "yes":
        return "shutting down"
    if s == "no":
        return "shoutdown aborted"
    return "sorry"
   