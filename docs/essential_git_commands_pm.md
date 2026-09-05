# Essential Git Commands

## 1. Getting Started

- `git init` — Initializes a new, empty Git repository in the current folder.
- `git clone <url>` — Downloads an existing repository from a remote server (like GitHub or GitLab) to your local machine.

## 2. Basic Workflow (Saving Changes)

- `git status` — Displays the state of the working directory and the staging area. It shows which files are modified, staged, or untracked.
- `git add <file>` — Adds a file to the staging area, preparing it for the next commit. Use `git add .` to stage all modified files at once.
- `git commit -m "Your message"` — Records a permanent snapshot of your staged files in the version history, labeled with a descriptive message.

## 3. Branching & Merging

- `git branch` — Lists all local branches in the repository. An asterisk (`*`) indicates the branch you are currently on.
- `git branch <branch-name>` — Creates a new branch but keeps your workspace on the current branch.
- `git checkout <branch-name>` — Switches your workspace to the specified branch. Newer Git versions also support `git switch <branch-name>` for this.
- `git merge <branch-name>` — Combines the specified branch's history into the branch you are currently on.

## 4. Synchronizing with Remote

- `git pull` — Downloads changes from the remote server and immediately merges them into your local working directory.
- `git push` — Uploads your local branch commits to the remote repository.

## 5. Checking History

- `git log` — Shows the chronological commit history for the current branch.

> **Pro Tip:** Always run `git status` right before you commit. It’s the easiest way to ensure you are only saving the files you actually intended to change!
