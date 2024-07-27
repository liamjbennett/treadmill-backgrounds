import os
import glob
import random
import shutil

# Make sure to use the correct path on your system, and be careful with the use of the script since it involves file deletion.
TARGET_DIR = os.path.expanduser('~/Library/Containers/com.microsoft.teams2/Data/Library/Application Support/Microsoft/MSTeams/Backgrounds')

# Define the list of files to be replaced
files_to_replace = [
    'feelingDreamy2Animated_v=0.1.mp4',
    'feelingDreamy4Animated_v=0.1.mp4',
    'feelingDreamy5Animated_v=0.2.mp4',
    'feelingDreamy7Animated_v=0.1.mp4'
]

# Get the list of .mp4 files in the current directory
current_directory = os.getcwd()
mp4_files = glob.glob(os.path.join(current_directory, '*.mp4'))

# Check if there are enough files to replace
if len(mp4_files) < 4:
    print("Not enough mp4 files found to perform the replacement.")
else:
    # Select 4 random mp4 files from the list
    selected_files = random.sample(mp4_files, 4)

    # Create the target directory if it doesn't exist
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)

    # Perform the file replacement
    for i, target_file in enumerate(files_to_replace):
        source_file = selected_files[i]
        target_file_path = os.path.join(TARGET_DIR, target_file)


        # Delete the target file if it exists
        if os.path.exists(target_file_path):
            os.remove(target_file_path)
        else:
            print(f"Target file {target_file} does not exist. It will be created.")

        # Copy the new file to the target location
        try:
            shutil.copy2(source_file, target_file_path)
            print(f"Replaced {target_file} with {source_file}.")
        except Exception as e:
            print(f"Failed to replace {target_file} with {source_file}. Error: {e}")

print("Replacement complete.")

