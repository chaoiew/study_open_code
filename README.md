…or create a new repository on the command line
``` bash
echo "# study_open_code" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:chaoiew/study_open_code.git
git push -u origin main
```
…or push an existing repository from the command line
``` bash
git remote add origin git@github.com:chaoiew/study_open_code.git
git branch -M main
git push -u origin main
```
