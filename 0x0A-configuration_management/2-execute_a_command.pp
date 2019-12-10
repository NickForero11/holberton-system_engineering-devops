# Kills certain process
# the name of the process should be stored in the process variable.

$process = 'killmenow'
exec { 'kill process':
  command => "pkill ${process}",
  path    => '/usr/bin/'
}
