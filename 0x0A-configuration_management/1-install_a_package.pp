# Install puppet-lint 2.1.1 as a ruby gem
# after updating package cache.

package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
    before => Exec['update packages'],
}

exec { 'update packages':
  command => '/usr/bin/apt-get update',
}
