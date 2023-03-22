#!/usr/bin/env perl

## The sink we are interested in should be given as the
## 1st argument to the script.
die("Need a source name as the first argument\n") if @ARGV < 1;
my $sink=$ARGV[0];

## Run the pactl command and save the output in
## ther filehandle $fh
open(my $fh, '-|', 'pactl list sinks');

## Set the record separator to consecutive newlines (same as -000)
## this means we read the info for each sink as a single "line".
$/="\n\n";

## Go through the pactl output
while ($l = <$fh>) {
    ## If this is the sink we are interested in
    if ($l =~ /#$sink/) {
        ## Extract the current colume of this sink
        my ($volume) = ($l =~ m/Volume:.*?(\d+)%/);
        my ($muted) = ($l =~ m/Mute:.*?(no|yes)/);
        ## If the script has been run with a second argument,
        print "VOLUME: $volume%\n";
        print "MUTE:   $muted\n";
    }
}
