# andre3000
Manipulating the ssh config feature for obfuscation (*could be used for DoS attack but very slow so far*)
This tool is used to take advantage of the ssh config file and obfuscate ssh connections to targets.


`Usage: python3 andre3000.py [-w windows] [-l linux]  [-hc chrono order] [-hr random order] [-n # of repeated connections] -a [address] -A[address file][-u username] [-p port]`
## Requirements

Authorized keys must be present and actively used on the target.
Required packages:
- import os
- import sys
- import getpass

## License

MIT License
