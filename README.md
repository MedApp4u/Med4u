# DoctorsWebApp

## Instructions

Before pushing any code remember to make a new branch and create a pull request and ask a review from ANY two members (preferably one backend and one frontend member) and then merge it into the master just to maintain the code quality.

Follow these Steps :
1) Clone this repository into your local machine using :
    `git clone https://github.com/MedicalAppInfibeam/DjangoApp.git`

2) Create a branch separate from your master branch using :
    `git checkout -b <branch-name>`

3) Once this is done and ONLY when you write this command, then make changes to your cloned repo.

4) After changes has been made type these three commands :
    `git add *`
    `git commit -m "some comment on whatever you did"`
    `git push -u origin <branch-name>`


5) Remember whenever you want to make a change ALWAYS be in your own branch and not the master one.

6) Once you have pushed the code open your github account and go the go to our org home page where you'll see an option `Compare and pull request`. Press this and make a pull request. On the right now you'll see an option called reviewers where assign any two reviewers. Wait till they review. 

7) You can start with more changes but make sure you are on the branch other than the master. You can checnk which branchyou are on by :
    `git branch`
To change branch type: 
    `git checkout <branch_you_want_to_change_to>`

8) To update your master branch do these :
    `git checkout master`
    `git fetch origin`
    `git merge origin/master`
    `git checkout -b <branch-name>`
    
    
