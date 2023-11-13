# Update the ulimit value
exec { '/usr/bin/env sed -i s/15/4096/ /etc/default/nginx': }
-> exec { '/usr/bin/env service nginx restart': }
