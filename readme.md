<p align="center">
  <img width="275px" height="100px" src="https://raw.githubusercontent.com/kazewaze/assets-holder/main/CooLTooL.svg" alt="Pilly Logo"/>
</p>

## A TooL too CooL for school that automatically comments-out all exercises except the current one for running and testing the output. It also runs the file for you like an all-in-one TooL. Pretty CooL.

## How does it work?
-------
This CooL TooL reads and saves the contents of the original lab file your working on and edits the contents by commenting-out the exercises that you don't want to run and only leaves the current exercise untouched so only that exercise runs when the file runs. It also doesn't change the original file at all and creates a new file called "runme.py" and then executes the runme file when you run CooLTooL so you can see the selected exercise's output. Once your done with the lab file just it's ready to go untouched and you can either delete the runme file or just let CooLTooL overwrite the file when you start working on another lab file! Thats it! Eazy Peazy.

## Example Usage:
Be sure to always name the lab files with this format: lab_[lab number].py
Like the file in examples dir: lab_7.py
```
kazewaze > python cooltool.py [lab-file-#] [exercise-#]
```

## Actual Usage:
7 - Selects the lab_7.py file in examples folder.
3 - Selects Exercise 3 in the lab_7.py file.
```
kazewaze > python cooltool.py 7 3
```