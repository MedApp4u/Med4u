# DjangoApp

Hello!

## Instructions

Before pushing any code remember to make a new branch and create a pull request and ask a review from ANY two members (preferably one backend and one frontend member) and then merge it into the master just to maintain code quality.

Follow these Steps :
1) Copy files from the `virtual env files` folder into your local Virtual Environment.

2) Clone this repository into your local machine.

3) Create a branch separate from your master branch using :
    `git checkout -b <branch-name>`

4) Once this is done and ONLY when you write this command, then make changes to your cloned repo.

5) After changes has been made type these three commands :
    `git add *`
    `git commit -m "<whatever> you want to did"`
    `git push -u origin <branch-name>`


6) Remember whenever you want to make a change ALWAYS be in your own branch and not the master one.

7) Once you have pushed the code open your github account and go the go to our org home page where you'll see an option `Compare and pull request`. Press this and make a pull request. On the right now you'll see an option called reviewers where assign any two reviewers. Wait till they review. 

8) You can start with more changes but make sure you are on the branch other than the master. You can checnk which branchyou are on by :
    `git branch`
To change branch type: 
    `git checkout <branch_you_want_to_change_to>`

6) To update your master branch do these :
    `git checkout master`
    `git fetch origin`
    `git merge origin/master`
    `git checkout -b <branch-name>`
