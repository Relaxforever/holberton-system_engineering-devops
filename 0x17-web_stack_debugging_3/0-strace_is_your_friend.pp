# Fixes a wrong call to a unknown file
exec { "Replace Bad instances":
command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
path    => ['/bin', '/usr/bin']
}
