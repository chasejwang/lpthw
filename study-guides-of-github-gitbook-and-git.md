### GitHub Guideline

### 

### 

### 

### 

### 

### 

### 

### 

### 

### 

### Git Guideline

Resource Links:  [https://git-scm.com/doc](https://git-scm.com/doc)

Reading "Documentation" Section.

**1.1  Getting Started -About Version Control**

**Background Info**

About Version Control

definition: Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later.

Its function is like "time machine" on mac, keeping every version of files, so you can recall each of them when modifications were made.

Local Version Control Systems\(LVCS\):

The characteristic:

copy files into another directory.

| Pros | Cons |
| :--- | :--- |
| Common | incredibly error prone |
|  | easy to forget which location the copied directory is in. |

Solutions to cons: develop VCSs that have a simple database that kept all the changes to files under revision control.

![](/assets/local.png)

Examples :

RCS \(one of the most popular VCS tools\)

Mac OS X \( installed with the developer Tools\)

Centralized Version Control Systems\(CVCS\):

CVCS is developed to solve the problem that people need to collaborate with developers on other systems.

Examples: CVS, Subversion, and Perforce \( a number of clients can check out files from one central place\)

![](/assets/centralized.png)

| Pros \(over local VCSs\) | Cons |
| :--- | :--- |
| everyone knows a certain degree what everyone else on the project is doing | That centralized severs down for an hours, nobody can collaborate at all or save versioned changes to anything they are working on |
| Administrators have fine-grained control over what can do what | the hard disk on database becomes corrupted, iif without proper backup, you lose everything. \( the same disadvantage can also happen to Local VSC |
| easier to administer a CVSCs than it is to deal with local databases on every clients |  |

Distributed Version Control Systems\(DVCSs\)

Its advantages: it solves the problem of CVCS:

1. Thus if any server dies, and these systems were collaborating via it, any of the client repositories can be copied back up to the server to restore it. Every clone is really a full backup of all the data.

   1. You can collaborate with different groups of people in different ways simultaneously within the same project. This allows you to set up several types of workflows that aren’t possible in centralized systems, such as hierarchical models.

Example: Git, Mercurial, Bazaar, or Darcs

![](/assets/distributed.png)

2.1 Setting up Git

What's Git?

At the heart of GitHub is an open source version control system \(VCS\) called Git. Git is responsible for everything GitHub-related that happens locally on your computer.

Setting up Git:

Download git:

Open Terminal

Type command in Terminal like below telling your name so your commits will be properly labeled:

Type the command to associate your email address with your git com

Getting a Git Repository:

The first thing is first.

```
# git init  #initiate a Repository in an existing directory
```

### Practices:

Setting up Git

Create a Repository

Clone a Repository

Be Social

