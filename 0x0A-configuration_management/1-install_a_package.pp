#installing flast from pip3 version 2.1.0
package { 'flask' :
  ensure   => '2.1.0',
  provider => 'pipe3',
  require  => Package['python3-pip'], # Ensure pip3 is installed first
}
