#This file creates a holberton file in /tmp/holberton
file { 'holberton':
  path    => '/tmp/holberton',
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  }
