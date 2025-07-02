import subprocess
import random as r
import sys
import os

def randomFileChange(fileName):
    alphaList = list("abcdefghijklmnopqrstuvwxyz")
    word = f"{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}{r.choice(alphaList)}"
    str = f"str = '{word}'\nprint(str)"
    with open(f"{fileName}.py", "w+") as f:
            f.write(str) 

def runCommand(command):
    """Run a shell command and return its output, or exit on error."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"\033[91m[ERROR]\033[0m {result.stderr.strip()}")
        sys.exit(1)
    return result.stdout.strip()

def switchBranch(branch):
    """Switch to the target branch."""
    print(f"\033[96mSwitching to branch:\033[0m {branch}")
    runCommand(f"git checkout {branch}")

def hasChanges():
    """Check if there are changes to commit."""
    return bool(runCommand("git status --porcelain"))

def commitAndPush(branch, message):
    """Add, commit, and push changes to the given branch."""
    print("\033[94mStaging changes...\033[0m")
    runCommand("git add main.py data.txt")
    
    print("\033[94mCommitting...\033[0m")
    runCommand(f'git commit -m "{message}"')
    
    print("\033[94mPushing to remote...\033[0m")
    runCommand(f"git push origin {branch}")

    print("\033[92m✔ Git changes pushed successfully!\033[0m")

def main():

    randomFileChange("main")
    
    with open("data.txt", "r") as f:
        number = f.read()

    with open("data.txt", "w") as f:
        f.write(f"{int(number)+1}")


    branch, message = "main", f"commit no. {number}"
    switchBranch(branch)

    if not hasChanges():
        print("\033[93mNo changes to commit.\033[0m")
        return

    commitAndPush(branch, message)

if __name__ == "__main__":
    main()