Title: Installing Chromium on Fedora 14
Date: 2011-01-31
Modified: 2011-01-31
Category: archive
Tags: jbs, filename, chromium, chrome, firefox, fedora
Slug: 2011-01-31-installing-chromium-on-fedora-14
Authors: Jon Robbins


This is very easy...actually I think it is too easy to even blog about... but anyway.
I just went here: [repos.fedorapeople.org/repos/spot/chromium](http://repos.fedorapeople.org/repos/spot/chromium/ ) and then added the repos file to my /etc/yum.repos.d/ directory.

[code]
#filename: fedora-chromium.repo
# Place this file in your /etc/yum.repos.d/ directory
[fedora-chromium]
name=Chromium web browser and deps
baseurl=http://repos.fedorapeople.org/repos/spot/chromium/fedora-$releasever/$basearch/
enabled=1
gpgcheck=0

[fedora-chromium-source]
name=Chromium web browser and deps - Source
baseurl=http://repos.fedorapeople.org/repos/spot/chromium/fedora-$releasever/SRPMS/
enabled=0
gpgcheck=0
[/code]


After that, ran a "yum update" and "yum install chromium", and that was it!
easy as pie.  now, it's not [Iron](http://www.srware.net/en/software_srware_iron.php), but still it is faster than firefox.  
The downside is that google knows all, I guess.  

I never thought I would see the day I would be using some other browser besides firefox, but I guess that day has come.
Goodbye, Firefox.  Maybe I'll be back one day when there have been some improvements, but thanks for everything!

#chromium #chrome #firefox #fedora

 original filename: 162