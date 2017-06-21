# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a code of conduct, please follow it in all your interactions with the project.

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
    `git checkout <branch_you_want_to_change_into>`

8) To update your master branch do these :
    `git checkout master`
    `git fetch origin`
    `git merge origin/master`
    `git checkout -b <branch-name>`
    
## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at [INSERT EMAIL ADDRESS]. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/
