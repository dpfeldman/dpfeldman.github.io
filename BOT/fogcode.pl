#!/usr/bin/perl
#the previous line may need to be changed for different systems


# This program will create sentences from a selection of phrases.
# The idea is based on a program by John Lawler, and this code was designed
# in collaboration with him. This whole thing was Lawler's idea :-)
#
# (actually, I got the Chomsky phrases from Anthony Aristar, who
#  got them from somebody else, and doesn't remember who, and
#  I just ported them to my previous program FOGGY, which
#  already had phrase collections from Software Engineering and
#  Folklore Research.  But it *was* my idea to do it on the Web.
#  -j :-)
#
# This program is copyright Kevin McGowan, 1995.
# Please send questions or comments to: clunis@umich.edu
# This code may be freely copied and modified for satiric purposes,
# but please do not delete these lines. . .
# Thank You.

srand; # This invokes perl's random number generator

# Customize the following pathnames for your local system.
$intro_file = "chomsky.1";
$subject_file = "chomsky.2";
$verb_file = "chomsky.3";
$object_file = "chomsky.4";

# Print out a content-type for HTTP/1.0 compatibility
print ("Content-type: text/html\n\n");

# Print Web Formatting
print ("<HTML>\n<HEAD><TITLE>The Chomskybot</TITLE>\n</HEAD>");
print ("<BODY>\n<FONT SIZE=4><FONT SIZE=6>L</FONT>ook ");
print ("<FONT SIZE=6>O</FONT>n <FONT SIZE=6>M</FONT>y ");
print ("<FONT SIZE=6>W</FONT>ords, <FONT SIZE=6>Y</FONT>e ");
print ("<FONT SIZE=6>M</FONT>ighty, <FONT SIZE=6>A</FONT>nd ");
print ("<FONT SIZE=6>D</FONT>espair<FONT SIZE=6>!</FONT>\n<P>\n");

# Load datafiles into arrays, remove new-line markers at end of strings
open (INTROFILE, $intro_file) || die "Sorry, I couldn't open $intro_file. Perhaps it is missing. Error";
push (@introductions,<INTROFILE>);
chop (@introductions);
close (INTROFILE);

open (SUBJECTFILE, $subject_file) || die "Sorry, I couldn't open $subject_file. Perhaps it is missing. Error";
push (@subjects,<SUBJECTFILE>);
chop (@subjects);
close (SUBJECTFILE);

open (VERBFILE, $verb_file) || die "Sorry, I couldn't open $verb_file. Perhaps it is missing. Error";
push (@verbs,<VERBFILE>);
chop (@verbs);
close(VERBFILE);

open (OBJECTFILE, $object_file) || die "Sorry, I couldn't open $object_file. Perhaps it is missing. Error";
push (@objects,<OBJECTFILE>);
chop (@objects);
close(OBJECTFILE);

# Use a while loop to make it generate 5 sentences.

while ($paragraph < 5)  {

# Here we select random phrases from the loaded arrays

       $intros= rand(@introductions);
       $subs= rand(@subjects);
       $vp= rand(@verbs);
       $obs= rand(@objects);

# The following lines ensure that a phrase will not be used more than once.
$adverbial     = splice(@introductions,$intros,1);
$noun_phrase   = splice(@subjects,$subs,1);
$verb_phrase   = splice(@verbs,$vp,1);
$object_phrase = splice(@objects,$obs,1);

# The following lines send output to the the Web browser.

if ($paragraph eq "0") {
# indent the paragraph:
print ("&#160;<tt> </tt>&#160;<tt> </tt>&#160;<tt> </tt>&#160;<tt> </tt>");
# (a nice HTML hack borrowed with thanks from
#  Jutta Degener's Interesting Times)
       print ("$adverbial $noun_phrase $verb_phrase $object_phrase\n");
} else {
       print ("$adverbial $noun_phrase $verb_phrase $object_phrase\n");

   }
$paragraph += 1;
}

# that completes the Chomskybot output; now add the formatting
# at the bottom of the page.  First, the line:
print ("\n</P>\n<P><HR>\n</p>\n</FONT>\n");
# then the repeat button, which will work for some but not all:
print ("<b><A HREF=\"http://stick.us.itd.umich.edu/cgi-bin/chomsky.pl\">Next paragraph</a></b>");
# issue a warning if it doesn't work:
print (" &#160;<tt> </tt>(Use <b>RELOAD</b> if the button doesn't work)<br>");
# then point to the FAQ:
print ("<b><A HREF=\"http://stick.us.itd.umich.edu/jlawler/foggy.faq.html\">What is this all about?</a></b>");
# space out the buttons:
print ("&#160;<tt> </tt> &#160;<tt> </tt> &#160;<tt> </tt>");
print ("&#160;<tt> </tt> &#160;<tt> </tt> &#160;<tt> </tt>");
# finally, point to the second question in the FAQ:
print ("<b><A HREF=\"http://stick.us.itd.umich.edu/jlawler/foggy.faq.html#how\">How does it work?</a></b><br>");
# now wrap the page and quit
print ("</BODY>\n</HTML>\n");






