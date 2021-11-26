# Python-Coding-Lab

This is the place where we will have our code for the course. You can download it and practice!

## Installing Visual Studio Code extensions

Execute the corresponding commands in your command line in order to install VS Code extensions:

- Windows:
> $files = Get-Content -Path extensions.txt
> ForEach ($file in $files) { code --install-extension $file }
- Mac:
> cat extensions.txt | xargs -L 1 code --install-extension
