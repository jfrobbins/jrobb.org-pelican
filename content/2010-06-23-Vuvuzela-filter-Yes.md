Title: Vuvuzela filter Yes
Date: 2010-06-23
Modified: 2010-06-23
Category: archive
Tags: jbs, news, linux
Slug: vuvuzela-filter-yes
Authors: Jon Robbins


From[ DistroWatch Weekly](http://distrowatch.com/weekly.php?issue=20100621#news" target="_blank):

 <blockquote>Finally, somewhat off-topic, but sometimes it can't hurt to add an amusing twist to the serious world of free software. During the last couple of weeks the infamous vuvuzela, obnoxiously accompanying every single match at the ongoing football world cup in South Africa, has become a source of irritation to many football fans around the world. The sound of the tuneless horn is reportedly not so bad when absorbing it in a stadium, but it tends to spoil the experience for those who watch the spectacle on TV. If you are among those who can't stand the racket but enjoy watching sporting events on a computer, a number of solutions exist to help you keep sane during the matches. [Fedora](http://distrowatch.com/fedora) users can filter the unpleasant sound by following [this simple guide](http://fetzig.org/2010/06/13/vuvuzela-filter-using-fedora/), while Ubuntu fans could use a VLC plugin called [VuvuzeLAUTLOS](http://www.ind.rwth-aachen.de/en/research/tools/vuvuzelautlos/). There is also a [devuvuzelator](http://isophonics.net/content/whats-all-about-vuvuzela) for Mac OS X users. But perhaps the most elegant solution has been provided by Andr Dieb who [suggests an excellent one-liner](http://genuinepulse.blogspot.com/2010/06/vuvuzela-filter.html) (for GStreamer on Debian-based distributions to filter out the unpleasant sound frequencies. The code looks like this:

 gst-launch-0.10 autoaudiosrc ! audioconvert ! audiochebband mode=band-reject lower-frequency=223 upper-frequency=243 type=2 ripple=50 ! audiochebband mode=band-reject lower-frequency=456 upper-frequency=476 type=2 ripple=50 ! audiochebband mode=band-reject lower-frequency=922 upper-frequency=942 type=2 ripple=50 ! audiochebband mode=band-reject lower-frequency=1854 upper-frequency=1874 type=2 ripple=50 ! audioconvert ! autoaudiosink

 We haven't tried this solution so use at your own risk! Now, does anybody have a solution to filter out the poor performances of some of the star-studded teams that play at the tournament? ;-)</blockquote>




tags: #linux 


Published Date: Wed, 23 Jun 2010 13:44:04 +0000 

[Original URL](http://factorq.net/2010/06/23/vuvuzela-filter-yes/) | [Original guid](http://factorq.net/?p=303) | PostID= 303

 original filename: 115