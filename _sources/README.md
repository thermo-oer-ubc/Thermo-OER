## 0. Install a terminal app on Windows:

- If you are a Windows 11 user, please install Windows terminal (wt) from the Microsoft store. This will help with interfacing bash (a linux shell) with Windows.

- Here is a cheatsheet to help you with simple commands in the terminal: [Link](https://www.guru99.com/linux-commands-cheat-sheet.html)

- Next, we need to install `git` in Windows from here: https://gitforwindows.org/

## 1. Installation and adding code to content website:

Installation steps to edit some of the contents for the website:

  - Clone this repo by running: `git clone https://github.com/thermo-oer-ubc/Thermo-OER`
    
  - Next, do a git "fetch" operation to get the latest files from this repo (other users will have contributed some changes to the codebase):
     `git fetch origin` [Please remember do this everytime you make a contribution; you should first fetch and then push]
 
  -  You should now see the same directory contents in your personal laptop/PC as in this repository.


  - use the `environment.yaml` file to create a seperate anaconda environment, run:

  `conda env create --name OER --file environment.yml --force`


  - Once you have the environment installed, activate it: `conda activate OER`
 
  -  You are now ready to make changes.

## 2. Pushing changes to this GitHub repository

- Like making regular edits on your computer, you edit your source files (Jupyter notebooks) in this repo.

- Once you are making changes, run the bash file in the root directory: `bash run.sh`; this basically "builds" your Jupyter book and creates the HTML files for the website.

- Need to add your changes using `git`, use: `git add *`

- Getting personal access tokens in GitHub: Click your profile photo, then click Settings. Then, on the left sidebar, you should click on Developer settings and then Personal access tokens. Click "Generate new token" and provide a short description in the "Note" field.
  
- Now, get ready to commit your changes:`git commit -m "type your commit message here"` (you should use personal token that you get from your GitHub profile; its a long list of alpha numeric characters)


- Finally, to push the changes: `git push origin`; the prompt will ask for an username, supply `thermo-oer-ubc` and then copy-paste the Github personal token

- Additionally, there is a GitHub pages packages that depolys the workflow for creating the website using HTML you just created using Jupyter book. Use this command:
  `ghp-import -n -p -f _build/html/`; this should now create a "branch" called gh-pages apart from the main branch. This will take a few miniutes for the workflow to render the website.

- Website can be found here: `https://thermo-oer-ubc.github.io/Thermo-OER/intro.html`

  ## Issues facing at the moment:
  
- For Windows users, there doesn't seem to a reliable BASH terminal to use for curating your conda environments. For now, options are:

  - MINGW terminal (comes as a bundle with Git Bash)
  - Windows Powershell (this is native in Windows; doesn't necessarily follow bash syntax)
  - Terminal inside Anaconda Navigator (this is too bloaty!)

- Really need to come up with a good alternative.
  
 
    
