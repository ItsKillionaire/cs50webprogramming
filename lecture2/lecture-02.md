Git and GitHub Essentials

Git is a command-line tool for version control, crucial for tracking code changes and collaboration. It allows saving code snapshots (commits), synchronizing work among multiple people via an online repository, testing new features safely on separate branches, and reverting to previous versions if needed.

GitHub is a popular online platform for hosting these Git repositories, offering a web interface to manage your code and collaborate.

Core Git Operations

= Creating & Getting Code =
git clone [repository URL] : Downloads a repository from GitHub to your local machine.
ls : Lists files/folders in the current directory.
cd [directory-name] : Navigates into a specified directory.
touch [filename] : Creates a new, empty file.

= Managing Changes =
git status : Shows current repository status (modified, staged, untracked files).
git add [filename] : Stages a specific file for the next commit.
git add . : Stages all modified and new files in the current directory.
git commit -m "Your message" : Saves staged changes with a descriptive message.
git commit -am "Your message" : Stages all modified (tracked) files and commits them in one step.

= Synchronizing with Remote =
git push : Uploads your local commits to the remote GitHub repository.
git pull : Downloads and integrates the latest changes from the remote repository.

Handling Conflicts

A merge conflict occurs when Git can't automatically reconcile differing changes to the same file part. This typically happens during git pull or git merge. Git marks conflicts within the file (e.g., <<<<<<< HEAD, =======, >>>>>>>). You must manually resolve these conflicts by editing the file, removing markers, and then committing the resolution:
git commit -am "Fix merge conflict"

Advanced Git: History & Branches

= Viewing History =
git log : Displays a chronological list of all commits, including hashes, authors, dates, and messages.

= Reverting Changes =
git reset --hard [commit-hash] : Reverts the repository to the state of a specific past commit.
git reset --hard origin/master : Resets your local master branch to match the remote GitHub version.

= Branching & Merging =
Branches let you work on separate features or fixes in parallel.
git branch : Lists all local branches, marking the current one with \*.
git checkout -b [new-branch-name] : Creates a new branch and switches to it.
git checkout [existing-branch-name] : Switches to an existing branch.
git merge [source-branch-name] : Integrates changes from the source-branch-name into your current branch.

GitHub-Specific Collaboration

    Forking: Creates your own independent copy of another's GitHub repository, useful for contributing to open-source projects.

    Pull Requests: After making changes in a forked repository, you submit a "pull request" to the original maintainers, asking them to review and merge your code. This is key for community-driven development.

    GitHub Pages: A free service to host static websites directly from a GitHub repository (e.g., yourusername.github.io). Push your HTML/CSS/JS, and it's live.
