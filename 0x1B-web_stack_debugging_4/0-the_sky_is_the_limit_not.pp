# Change the limit of open files per worker process in Nginx.

$limit_regexp='ULIMIT="-n [0-9]*"'
$desired_limit='ULIMIT="-n 262144"'
$operation="'s/${limit_regexp}/${desired_limit}/g'"
$command="sudo sed -i ${operation} nginx ; sudo service nginx restart"

exec { 'Increase limit of open files':
    command => $command,
    path    => '/usr/bin',
    cwd     => '/etc/default'
}
