def generate_message(theme, target_audience, level):
    message = (
        f"Theme: {theme}\nTarget Audience: {target_audience}\nLevel: {level}\n"
    )

    if level.lower() == "for a 5-year-old child":
        message += "This is a simple and fun introduction to the chosen theme, suitable for a young child."

    elif (
        level.lower()
        == "for a middle-aged lady with a doctorate in astrophysics"
    ):
        message += "This content is designed to provide an intellectually stimulating exploration of the chosen theme, catering to someone with a strong background in astrophysics."

    else:
        message += "Custom message for the specified theme, target audience, and level."

    print(message)


# Example usage:
generate_message(
    "Space Exploration", "5-year-old child", "for a 5-year-old child"
)
generate_message(
    "Astrophysics",
    "Middle-aged lady",
    "for a middle-aged lady with a doctorate in astrophysics",
)
generate_message("Custom Theme", "Custom Audience", "Custom Level")

while True:
    user_input = input("Enter something: ")
    print("You entered:", user_input)
    if user_input == "PAU":
        break
