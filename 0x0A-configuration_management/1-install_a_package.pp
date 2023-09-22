#installing flast from pip3 version 2.1.0

package { 'flask' :
  ensure   => '2.1.0',
  provider => 'pipe3',
}
