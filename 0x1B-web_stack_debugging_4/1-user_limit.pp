#Update hard and soft file limit for holberton user

#hard file limit
exec { '/usr/bin/env sed -i "/^holberton hard/s/5/4096/" /etc/security/limits.conf': }

#soft file limit
exec { '/usr/bin/env sed -i "/^holberton soft/s/4/4096/" /etc/security/limits.conf': }
