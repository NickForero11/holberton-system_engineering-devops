# Check the configuration of a ssh-client verifying certain parameters
# and adding these if they aren't present.

file_line { 'Use of private key ~/.ssh/holberton':
  ensure             => present,
  line               => 'IdentityFile ~/.ssh/holberton'
  append_on_no_match => true,
  path               => '/etc/ssh/ssh_config',
}

file_line { 'Refuse to authenticate using a password':
  ensure             => present,
  line               => 'PasswordAuthentication no',
  append_on_no_match => true,
  path               => '/etc/ssh/ssh_config'
}
