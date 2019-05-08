# Red_Hat

Description:
Python script that searches one or more named input files

(standard input if no files are specified, or the file name '-' is given) for

lines containing a match to a regular expression pattern (given on command line as well).

 
Assume that input is ascii, you don't need to deal with different encoding.

 
If a line matches, print it. Please print the file name and the line number for every match.

 
Script accept list optional parameters which are mutually exclusive:

-u ( --underscore ) which prints '^' under the matching text

-c ( --color ) which highlight matching text

-m ( --machine ) which generate machine readable output

                 format: file_name:no_line:start_pos:matched_text

 
Multiple matches on single line are allowed, without overlapping.


