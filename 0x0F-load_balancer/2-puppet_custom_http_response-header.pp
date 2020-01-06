# Manifest that install Nginx and configures:
#   a simple default page.
#   a custom header with the server hostname.

package { 'Install Nginx':
  ensure => installed,
  name   => 'nginx'
}
-> exec { 'Allow Nginx http over the firewall':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/sbin/'
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

-> service { 'Check Nginx service':
  ensure => 'running',
  enable => true,
  name   => 'nginx'
}
