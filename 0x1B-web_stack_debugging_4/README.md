# 0x1B. Web stack debugging #4

## Description

Learning objectives of this project:

* How to see error logs of Nginx.
* What is ulimit?
* How linux handles the opened files per process.
* How linux handles the limits of every process.

---

### [0. Sky is the limit, let's bring that limit higher](./0-the_sky_is_the_limit_not.pp)

* The Nginx server is failing handling 2000 requests with 100 requests at a time, the error is `socket() failed (24: Too many open files)`, make a Puppet manifest to solve this problem and handle all the requests.

### [1. User limit](./1-user_limit.pp)

* There is a problem when switching to the user holberton using `su - holberton` because there are too many opened files, make a Puppet manifest to fix the number of opened files, then login with the holberton user and open a file without any error message.

---

## Author

* **Nicolas Forero Puello** - [NickForero11](https://github.com/NickForero11)
