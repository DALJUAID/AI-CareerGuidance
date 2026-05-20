def get_user_choice(prompt, choices, display_choices=True):
    """Gets valid user input."""
    while True:
        if display_choices:
            for i, choice in enumerate(choices, 1):
                print(f"{i}. {choice.capitalize()}")
        user_input = input(prompt)
        if user_input.isdigit() and 1 <= int(user_input) <= len(choices):
            return choices[int(user_input) - 1]
        print(f"Invalid. Choose a number from 1 to {len(choices)}.")

def get_careers(interests, field):
    """Returns career options based on interests and field."""
    careers = {
        ("science", "research"): ["Data Scientist", "Chemist", "Biologist"],
        ("science", "practical"): ["Engineer", "Doctor", "Pharmacist"],
        ("arts", "creative"): ["Graphic Designer", "Musician", "Artist"],
        ("arts", "writing"): ["Writer", "Journalist", "Editor"],
        ("business", "finance"): ["Accountant", "Analyst", "Banker"],
        ("business", "management"): ["Manager", "HR", "Sales"],
        ("technology", "software"): ["Web Developer", "Software Engineer", "App Developer"],
        ("technology", "hardware"): ["Computer Technician", "Network Engineer", "Systems Administrator"],
        ("education", "teaching"): ["Teacher", "Professor", "Trainer"],
        ("education", "administration"): ["School Administrator", "Education Consultant"],
    }
    return careers.get((interests, field), ["No match found"])

def career_guidance():
    """Simple career guidance system."""
    print("Welcome to Career Guidance!")

    interests = get_user_choice(
        "Choose your interest: ",
        ["science", "arts", "business", "technology", "education"],
    )

    if interests in ["science", "arts", "business"]:
        field = get_user_choice(
            "Choose your field: ",
            ["research", "practical", "creative", "writing", "finance", "management"],
        )
    elif interests == "technology":
        field = get_user_choice(
            "Choose your field: ",
            ["software", "hardware"],
        )
    else: # education
        field = get_user_choice(
            "Choose your field: ",
            ["teaching", "administration"],
        )

    careers = get_careers(interests, field)
    print("\nRecommended Careers:")
    for i, career in enumerate(careers, 1):
        print(f"{i}. {career}")

    # Let user pick a career
    if careers != ["No match found"]:
      career_choice = get_user_choice("\nChoose a career: ", careers, display_choices=False) #prevent displaying choices again.
      print(f"\nYou selected: {career_choice}")

career_guidance()
