# MultiMap
 
Perform multiple NMap scans simultaneously. This works perfectly on Windows 10, testing on Linux results in a lot of errors. I'm currently working on a version that will work perfectly and just as good as it does on Windows for Linux.

```
Usage: MMap.py [OPTIONS] HOSTS

Options:
  -ns, --no-save           Prevents MultiMap from saving output to files.
  -oh, --output-here       Create output files in your current directory.
  -fn, --folder-name TEXT  Choose the name of the folder that will contain the
                           output files.
  -y, --yes                Skip the y/n prompt at the beginning.
  -Pn                      Run ping scans instead of normal NMap scans.
  --help                   Show this message and exit.
```
