# Update the ulimit value in the nginx configuration file after backing up the file

$ulimit_value = 4096


# Backup the original nginx configuration file
file { '/etc/default/nginx.backup':
    ensure => 'file',
    source => '/etc/default/nginx,
}

# Update the ulimit value
exec { 'update_ulimit':
    command  => "sed -i 's/^ULIMIT=\"-n [0-9]*\"/ULIMIT=\"-n ${ulimit_value}\"/' /etc/default/nginx",
    unless   => "grep -q '^ULIMIT=\"-n ${ulimit_value}\"' /etc/default/nginx",
    require  => File['/etc/default/nginx.backup'],
}