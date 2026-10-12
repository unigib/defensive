from validation import parse_count

while True:
    raw = input("Count (1-10): ")

    try:
        count = parse_count(raw)
    except ValueError as error:
        print(error)
        continue

    print(f"Accepted: {count}")
    break
