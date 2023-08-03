#!/usr/bin/env ruby
Sender = ARGV[0].scan(/from:(.*?)\]/).join(',')
Receiver = ARGV[0].scan(/to:(.*?)\]/).join(',')
Flags = ARGV[0].scan(/flags:(.*?)\]/).join(',')
puts "#{Sender},#{Receiver},#{Flags}"
