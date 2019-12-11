# Check the configuration of a ssh-client verifying certain parameters

file_line { 'Use of private key ~/.ssh/holberton':
  ensure => present,
  line   => 'IdentityFile ~/.ssh/holberton',
  path   => '/etc/ssh/ssh_config'
}

file_line { 'Refuse to authenticate using a password':
  ensure => present,
  line   => 'PasswordAuthentication no',
  path   => '/etc/ssh/ssh_config'
}
