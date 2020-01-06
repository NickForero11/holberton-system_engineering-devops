# Manifest that install Nginx and configures:
#   a simple default page.
#   a custom header with the server hostname.

package { 'Install Nginx':
  ensure => installed,
  name   => 'nginx'
}

-> file_line {'Add default page':
  ensure             => 'present',
  path               => '/var/www/html/index.nginx-debian.html',
  line               => 'Holberton School',
  append_on_no_match => true
}

-> file_line {'Add custom header':
  ensure             => 'present',
  path               => '/etc/nginx/nginx.conf',
  after              => 'sendfile on;',
  line               => '	add_header X-Served-By $hostname;',
  append_on_no_match => true
}

-> file_line { 'Add redirectme':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;'
}

service { 'Check Nginx service':
  ensure  => 'running',
  enable  => true,
  name    => 'nginx',
  require => Package['Install Nginx']
}
