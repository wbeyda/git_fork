# git fork app

## How to install
- Ensure you have Docker Desktop installed 
- https://www.docker.com/products/docker-desktop/
- clone this repo locally. Either through git or downloading the zip file
- In a terminal `cd` into this directory
- run `docker compose up`
- wait for docker to finish this should end with a line like this:
```
git-fork-web-1  | Starting development server at http://0.0.0.0:8000/
```
--- 

### In a browser navigate to the address and fill out the form
---

### account 
- the github account to fork FROM
- Example `octocat`
### repo 
- the github account to fork TO your account
- Example `Hello-World`
### new_repo 
- the name of the repo on your account
- Example `Hello-Octocat`
### your_account 
- your github account user name
- Example `wbeyda`
### token
- your github access token
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

---

### You should see a link to your github account with the new repo that has been forked 