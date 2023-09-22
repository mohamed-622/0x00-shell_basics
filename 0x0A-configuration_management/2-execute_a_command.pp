# Kill the "killmenow" process without checking if it exists
exec { 'kill_killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/bin', # Specify the path to pkill
}
