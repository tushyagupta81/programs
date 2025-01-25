# Programs
>An aggregate of all my programs
---

## Main sepration
- school
    - Stuff i did during my school
- collage
    - Work and labs done for and in collage
- valut
    - private vault for note taking
- projects
    - All the projects i have made fully on my own
- followAlong
    - projects made by following a certain tutorial
- courses
    - any course i am following
---


### How to clone with all submodules
```bash
git clone --recurse-submodules -j8 git@github.com:tushyagupta81/programs.git
```

### Shift all submodules to either main or master
```bash
git submodule foreach "git checkout main || git checkout master || :"
```
