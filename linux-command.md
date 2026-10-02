# Linux Commands Cheat Sheet

This file documents the Linux commands I have learned and practiced. 
Each command includes a brief explanation of what it does.

## Navigation
- `pwd` : Print Working Directory – shows the folder you are currently in.
- `ls` : List – shows files and folders in the current directory.
- `cd <folder>` : Change Directory – moves you into a specified folder.
- `cd ..` : Moves up one folder level.

## File & Folder Management
- `mkdir <name>` : Make Directory – creates a new folder.
- `touch <name>` : Creates a new, empty file.
- `cp <source> <destination>` : Copy – copies a file or folder.
- `mv <source> <destination>` : Move – moves or renames a file or folder.
- `rm <name>` : Remove – deletes a file.
- `rm -r <folder>` : Remove recursively – deletes a folder and everything inside it.

## Permissions
- `chmod <permissions> <file>` : Change Mode – changes who can read, write, or execute a file. (Example: `chmod 755 script.sh`)
- `chown <user> <file>` : Change Owner – changes the owner of a file.

## System Information
- `whoami` : Shows the current logged-in user.
- `uname -a` : Shows system and kernel information.
- `df -h` : Disk Free – shows available disk space in human-readable format.
- `free -h` : Shows available memory (RAM).

## Process Management
- `ps aux` : Shows all running processes.
- `top` : Shows real-time running processes (press `q` to quit).
- `kill <PID>` : Kills a process using its Process ID (PID).

*Last updated: September 2026*
