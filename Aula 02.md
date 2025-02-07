

Aprender

API
deploy
docker
automação
boas praticas (systems design)
dashboards
pandas mais aprofundado



## Git

```bash
# Listar todas as branches 
git branch -a

# Criar nova branch
git checkout -b classe_velha

# Fazer commit
git status
git add velha.py 
git commit -m "mudar velha para usar classe"

# Push e cria branch no remote
git push --set-upstream origin classe_velha

# Volta para main e synca com remote
git checkout main
git pull

# Commit na
git status
git add velha.py 
git commit -m "alteracao na main"
git push
```