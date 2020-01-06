# Manifest that install Nginx and configures:
#   a simple default page.
#   a custom header with the server hostname.

package { 'Install Nginx':
  ensure => installed,
  name   => 'nginx'
}

file {'Add default page':
  path    => '/var/www/html/index.html',
  content => 'Holberton School',
  require => Package['Install Nginx']
}

file_line {'Add custom header':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'sendfile on;',
  line    => 'add_header X-Served-By $hostname;',
  require => Package['Install Nginx']
}

file_line { 'Add redirectme':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;'
  require => Package['Install Nginx']
}

service { 'Check Nginx service':
  ensure  => 'running',
  enable  => true,
  name    => 'nginx',
  require => Package['Install Nginx']
}
