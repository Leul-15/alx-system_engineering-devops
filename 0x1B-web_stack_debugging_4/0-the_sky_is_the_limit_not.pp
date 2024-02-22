# Increases the amount of traffic an Nginx server can handle

exec { 'fix_error':
  command => "/bin/sed -i 's/15/4096/g' /etc/default/nginx; ; sudo service nginx restart",
}
