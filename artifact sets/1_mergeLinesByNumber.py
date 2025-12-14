from collections import defaultdict

# Create a default dictionary to store the merged content
merged_lines = defaultdict(str)

# Open the file and read the lines
with open('1_artifacts.txt', 'r') as file:
    for line in file:
        # Strip newline and any leading/trailing whitespace
        line = line.strip()
        if not line:
            continue  # Skip empty lines

        # Split the line into the number and the content
        number, content = line.split('. ', 1)

        # Add the content to the corresponding number in the dictionary
        merged_lines[int(number)] += content + " "  # Add a space for separation

# Now write the merged lines back to a file (could be the same or a new file)
with open('2_artifactsMerged.txt', 'w') as file:  # Change 'artifacts_merged.txt' to '1_artifacts.txt' to overwrite
    for number in sorted(merged_lines):
        # Write the merged content to the file, remove trailing space and add a newline
        file.write(f"{number}. {merged_lines[number].strip()}\n")

print("Merging completed. Output is in '2_artifactsMerged.txt'.")