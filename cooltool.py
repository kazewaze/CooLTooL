'''
-----------------
          {}{}==
CooL TooL  <
         -----
-----------------
Author: Kaycee Ingram <kazewaze> 10/21/2023
'''

import sys
from os import path

# Command-Line Args (exclude current filename at sys.argv[0]).
cmd_args = sys.argv[1:len(sys.argv)]

# Main: Create and Execute runme file (with changes).
def cooltool():
    # Get user input. (This is mainly for others use, but not mine.)
    # notebook_info = get_user_input()

    # Create runme.py
    make_changes(cmd_args[0], cmd_args[1])
    # Execute that bad boy.
    exec(open('runme.py').read())

# Comments-out everything but the current exercise we are working on.
def make_changes(file, exercise_num):
    status = False
    # Make it easier on the user so they only have to use lab-# for file name.
    file = 'lab_' + file + '.py'
    file_content = get_file_contents(file)

    for idx in range(0, len(file_content)):
        char_list = split_chars(file_content[idx])

        # Account for newlines in between ([] throws error on char_list[0] condition).
        if (char_list != []):
            # Set (status = True) if we are on the current exercise.
            if (char_list[0] == '#' and char_list[len(char_list)-1] == str(exercise_num)):
                status = True
            # If (status = True) and we have not reached next exercise.
            elif (status == True and char_list[0] == '#' and char_list[len(char_list)-1] != str(exercise_num)):
                status = False

            # Comment-out every line that isn't the current exercise.
            if (status == False and char_list[0] != '#'):
                file_content[idx] = '# ' + file_content[idx]

    # Write changes to runme file and then close it.
    file_open = open('runme.py', 'w')
    file_open.write('\n'.join(file_content))
    file_open.close()

# Open file, get contents, return contents and close file.
def get_file_contents(file):
    # The preferred dir for lab files when using CooLTooL.
    if (path.exists('labs') and path.isdir('labs')):
        dir_name = 'labs/'
    elif (path.exists('examples') and path.isdir('examples')):
        dir_name = 'examples/'

    open_file = open(dir_name + file.lower(), 'r')
    contents = open_file.read().split('\n')
    open_file.close()
    return contents

# Get user input on name and section number for notebook file. 
def get_user_input():
    notebook_info = [input("Enter first and last name (no spaces): ") or "KayceeIngram", get_lab_num(), input("Enter section number: ") or "521"]

# Extract lab number from lab_file.
def get_lab_num():
    lab_file_name = sys.argv[1]
    file_chars = split_chars(lab_file_name)

    for idx in range(0, len(file_chars)):
        if (file_chars[idx] == '_'):
          lab_num = ''.join(file_chars[idx+1:len(file_chars)])
          if (lab_num.isdigit()):
              return lab_num
              

# Utility function for splitting a str-list into single chars.
def split_chars(target):
    result = []

    for k in target:
        result.append(k)
    
    return result

# Run it.
cooltool()