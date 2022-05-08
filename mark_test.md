# Recursive python script over html files for get data.
---
Title: Recursive python script over html files for get data.
UID: [[20220101]]()
Tags: [#bash](), [#python](), [#html]()
Origin UID: [[2022010100]]()
Origin Title: [Bash script]()
Date: 2022-05-06 03:39:02

---
### Main Content
**Description of the problem**

I have a script, that script receive a document in html via ```sys.argv```, but I have 10k of html.
I tried to run a pipe with ```find *.html | script.py``` Didn't work.

**Solution** [^1] 

```
for i in *.html 
    ./script.py $i
```

[^1]: [Linux](https://linuxhint.com/loop-through-files-bash/)
