# Media Manager

## Setup

### Set Alias

```bash
source ./alias.sh
```

## Commands

### Rewrite names

```bash
# run with alias
rewrite --prefix="Text_to_Remove"

# run with python
python rewrite_names.py
python rewrite_names.py --prefix="[Some Thing]" --dir="/usr/local/bin"
```

### Transfer

Transfer a directory (and all subdirectories) to one or many targets.

```bash
# run with alias
tran "/absolute/source/dir/path"

# run with python
python transfer.py "/absolute/dir/path"
```

```python
# transfer.py
target_list = ["/Volumes/HDD/videos", "/Volumes/SDD/videos/movies"]
```
