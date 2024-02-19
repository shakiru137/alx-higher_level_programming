#!/bin/bash

# If no commit message is provided as an argument, prompt the user
if [ $# -eq 0 ]; then
    read -p "Enter commit message: " commit_message
else
    commit_message="$*"
fi

# Add all changes
git add .

# Commit changes with the provided message
git commit -m "$commit_message"

# Push changes to the 'origin' remote repository (change 'origin' to your remote name if needed)
git push origin main  # Replace 'main' with your branch name if it's different

# Check the exit status of the previous command (git push)
if [ $? -eq 0 ]; then
    echo "Changes successfully pushed to GitHub."
else
    echo "Failed to push changes to GitHub."
fi
