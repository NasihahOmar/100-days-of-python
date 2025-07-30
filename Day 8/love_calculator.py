def calculate_love_score(name1, name2):
    combined_names = name1 +name2
    combined_names = combined_names.Lower()
    true_count = sum(combined_names.count(char) for char in "true")
    print(f"total = {true_count}")

    love_count = sum(combined_names.count(char) for char in "love")
    print(f"total = {love_count}")

    total_score = int(str(true_count) + str(love_count))
    print(f"love score = {total_score} ")
