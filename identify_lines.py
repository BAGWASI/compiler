def identify_lines(lines):
    result = []

    for line in lines:
        # Check if the line contains a comment
        if "#" in line or "'''" in line or '"""' in line:
            result.append("Comment: " + line)
        else:
            result.append("Not a comment: " + line)

    return result


# Read the script from file
with open("rental_estimator.py", "r") as file:
    script_lines = file.readlines()

# Identify lines as comments or not
results = identify_lines(script_lines)

# Display the results
for result in results:
    print(result)
