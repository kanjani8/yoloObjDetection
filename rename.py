# For rename the png& txt annotation file
# the path should be change
import os

# Define the path to the folder containing the files
folder_path = 'C://Users/Minji/humanDetection/darknet/data/humanData'  # Example folder path

# Check if the folder exists
if not os.path.exists(folder_path):
    print(f"The folder '{folder_path}' does not exist.")
else:
    # List all the png and txt files in the folder
    png_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    
    index = 0
    # Process each png file
    for png_file in png_files:
        index = index + 1
        base_name = os.path.splitext(png_file)[0]
        corresponding_txt_file = f"{base_name}.txt"
        
        # Check if the corresponding txt file exists
        if corresponding_txt_file in txt_files:
            # Count the number of lines in the txt file
            txt_file_path = os.path.join(folder_path, corresponding_txt_file)
            with open(txt_file_path, 'r') as file:
                lines_count = sum(1 for line in file)
            
            # Generate the new name
            new_name = f"people_{index}_{lines_count}"
            new_png_file_path = os.path.join(folder_path, f"{new_name}.png")
            new_txt_file_path = os.path.join(folder_path, f"{new_name}.txt")
            
            # Rename both the png and txt files
            os.rename(os.path.join(folder_path, png_file), new_png_file_path)
            os.rename(txt_file_path, new_txt_file_path)
            
            print(f"Renamed '{png_file}' and '{corresponding_txt_file}' to '{new_name}.png' and '{new_name}.txt'.")
        else:
            print(f"No corresponding txt file found for '{png_file}'.")