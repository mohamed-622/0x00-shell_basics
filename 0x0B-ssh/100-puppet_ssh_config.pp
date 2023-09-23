file_line{'name':
  path => '/etc/ssh/ssh_config',
  line => 'Host 54.236.24.105',
}
file_line{'host name':
  path => '/etc/ssh/ssh_config',
  line => '    HostName 54.236.24.105',
}
file_line{'user name':
  path => '/etc/ssh/ssh_config',
  line => '    User ubuntu',
}
file_line{'identity file':
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/school',
}
file_line{'password authentication':
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
}
