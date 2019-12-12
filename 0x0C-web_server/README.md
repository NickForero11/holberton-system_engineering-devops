# 0x0C. Web server

## Description

What you should learn from this project:

* What is the main role of a web server

* What is a child process

* Why web servers usually have a parent process and child processes

* What are the main HTTP requests

* What is a DNS?

* Which are the DNS records?

* What is TLD provider/server?

* What is Nginx?

* How to configure a Nginx server?

* What is HTTP?

* Which are the HTTP response codes?

---

### [0. Transfer a file to your server](./0-transfer_file)

* Bash script that transfers a file from our client to a server:

### [1. Install nginx web server](./1-install_nginx_web_server)

* Bash script that configure a basic nginx server with certain parameters.

### [2. Setup a domain name](./2-setup_a_domain_name)

* File that contains the Domain name of the IP address of the nginx server.

### [3. Redirection](./3-redirection)

* Bash script that configure a nginx server as in task 1, but also add a route /redirect_me that is redirecting to another page.

### [4. Not found page 404](./4-not_found_page_404)

* Bash script that configure a nginx server as in task 3, have a custom 404 page that contains the string Ceci n'est pas une page and return an HTTP 404 error code

### [6. Install Nginx web server (w/ Puppet)](./7-puppet_install_nginx_web_server.pp)

* Puppet manifest to install and configure a nginx server as in task 4.

---

## Author

* **Nicolas Forero Puello** - [NickForero11](https://github.com/NickForero11)
