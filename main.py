def love_calculator():
    name1 = input("Enter the first name: ").lower()
    name2 = input("Enter the second name: ").lower()

    combined_name = name1 + name2

    love_score = 0

    for char in combined_name:
        love_score += ord(char)

    love_percentage = love_score % 101

    print(f"The love percentage between {name1.capitalize()} and {name2.capitalize()} is {love_percentage}%.")

if __name__ == "__main__":
    love_calculator()