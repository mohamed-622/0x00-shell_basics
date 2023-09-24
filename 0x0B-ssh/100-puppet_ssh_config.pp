# Client configuration file  (w/ Puppet)
file_line{'Alias name':
  path => '/etc/ssh/ssh_config',
  line => 'Host 54.236.24.105
    HostName 54.236.24.105
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
