# Write your function below!

form typing  List


def fizz_count(words: List[str]) -> int:
    count = 0
    for word in words:
        if word == "fizz":
            count += 1
            return count
