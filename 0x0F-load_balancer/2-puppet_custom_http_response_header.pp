# Install Nginx
class { 'nginx':
  ensure => 'installed',
}

# Create a custom HTTP response header file
file { '/var/www/html/custom_header.html':
  ensure  => 'file',
  content => "X-Served-By: ${hostname}\n",
  require => Class['nginx'],
}

# Reload Nginx to apply the new configuration
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/var/www/html/custom_header.html'],
}
