# Releases the work processes from little work to a lot of workes.
exec {'adds more workers to the system so the processes dont failed':
  command  => "sed -i 's/worker_processes 4;/worker_processes 100;/g' /etc/nginx/nginx.conf && sudo service nginx restart",
  provider => 'shell',
}
