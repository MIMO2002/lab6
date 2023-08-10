Git Basic Command
=================
### Global Configuration
    # to set the global configuration
    git config --global user.name "your username"
    git config --global user.email "your email address"

    # to check global configuration
    git config user.name: check global config user name
    git config user.email: check global config user email
### Add Remote To Your Git Repository To Github or Any Git Server
- Go to Github and sign up your git account Create a new repository with any name Find remote url

      git remote add origin your_github_remote_url
- Use git remote to show remote name
        
      git remote
- Use git remote -v to show the remote of origin's urls
      
      git remote -v
### Initialize the git folder
By default, your directory is not tracked by git, type git init to initialize an empty git repository in your machine

    git init
### Pull
    # Syntax
    git pull remote_name branch_name
    # Example
    git pull origin master
### Push
- Check status
      
        git status
- Add changes to git staging

        # add all files changed
        git add .
        # In case we need to remove a specific file from stage
        git rm --cached filename
- Commit from git staging to repository

        git commit -m "Initial Commit"
- Push to remote repository branch
        
        # Syntax
        git push remote_name branch_name
        # Example
        git push origin master
### Show current branch
    git branch --show-current
### Switch branch in repository
    git checkout -b new_branch
### Throws away all uncommitted changes (reset)
    git reset --hard cedc856
    git push --force origin master