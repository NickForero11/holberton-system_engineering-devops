# Create a file called holberton with certain requirements.

$owner = 'www-data'
file { 'holberton':
  ensure  => present,
  path    => '/tmp/holberton',
  mode    => '0744',
  owner   => $owner,
  group   => $owner,
  content => 'I Love Puppet',
}
