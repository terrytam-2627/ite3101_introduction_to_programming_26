def shut_down(s: str) -> str:
    if s == "yes":
        return "shutting down"
    elifif s == "no":
        return "shoutdown aborted"
    else:
        return "sorry"
   