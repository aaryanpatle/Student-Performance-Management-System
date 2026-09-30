def findtotal(marks):
    total = 0

    for mark in marks:
        total = total + mark

    return total


def find_percentage(marks):
    total = findtotal(marks)
    percentage = total / len(marks)

    return percentage