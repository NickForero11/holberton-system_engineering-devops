# 0x0B. SSH

## Description

What you should learn from this project:

* What is a server
* Where servers usually live
* What is SSH
* How to create an SSH RSA key pair
* How to connect to a remote host using an SSH RSA key pair
* The advantage of using  #!/usr/bin/env bash instead of /bin/bash

---

### [0. Use a private key](./0-use_a_private_key)

* Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/holberton with the user ubuntu.

### [1. Create an SSH key pair](./1-create_ssh_key_pair)

* Write a Bash script that creates an RSA key pair with this requirements:

  * Name of the created private key must be holberton

  * Number of bits in the created key to be created 4096

  * The created key must be protected by the passphrase betty

### [2. Client configuration file](./2-ssh_config)

* Share your SSH client configuration in your answer file with this requirements:

  * Your SSH client configuration must be configured to use the private key ~/.ssh/holberton

  * Your SSH client configuration must be configured to refuse to authenticate using a password

### [4. Client configuration file (w/ Puppet)](./4-puppet_ssh_config.pp)

* Check your SSH client configuration with this requirements:

  * Your SSH client configuration must be configured to use the private key ~/.ssh/holberton

  * Your SSH client configuration must be configured to refuse to authenticate using a password

* If the configuration file don't accomplish the requirements it will change it to enable the correct configuration

---

## Author

* **Nicolas Forero Puello** - [NickForero11](https://github.com/NickForero11)
