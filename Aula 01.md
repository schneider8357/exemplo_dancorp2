## Manual git
man git
man git-add
git -h
git --help

## Inicializar repositório
mkdir exemplo_dancorp
cd exemplo_dancorp/
ls -la
git --help
git init
ls -la
tree .git

## Primeiro commit
vim README.md
ls -la
git status
git add README.md 
git status
git commit -m "initial commit"

## git log - historico de commits
git status
git log

# git config
git config --global user.email schneider8357@hotmail.com
git config --global user.name schneider8357

## Subir alterações para remote github
git remote add origin https://github.com/schneider8357/exemplo_dancorp.git
git push --set-upstream origin main

## Segundo commit
vim README.md 
git status
git add README.md 
git status
git commit -m "segundo commit"
git push