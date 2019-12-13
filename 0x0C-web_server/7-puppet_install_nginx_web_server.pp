#!/usr/bin/env bash
# Puppet manifest that installs Nginx and configures:
#   a simple default page.
#   a /redirectme page that redirects to a 301 moved permanently.

package { 'Check nginx installed':
  ensure => installed,
  name   => 'nginx',
  before => Exec['update packages']
}

file { 'Check home page':
  ensure  => file,
  path    => '/var/www/html/index.html',
  content => 'Holberton School',
}

exec { 'Configure redirect and restart':
  provider => shell,
  command  => 'sudo sed -i "/server_name _;/a \\\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}\n" /etc/nginx/sites-enabled/default; sudo service nginx restart'
}

exec { 'update packages':
  command => '/usr/bin/apt-get update',
}
