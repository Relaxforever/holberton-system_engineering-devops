# kill a process with puppet
exec { 'killmenow':
  path    => '/usr/bin',
  command => 'pkill -f killmenow',
  }

