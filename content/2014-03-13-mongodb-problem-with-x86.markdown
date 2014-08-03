Title: mongodb problem with x86
Date: 2014-03-13 23
Modified: 2014-03-13 23
Category: archive
Tags: pumpio
Slug: mongodb-problem-with-x86
Authors: Jon Robbins
Summary: Very recently [Dr. Sekula](https://hub.polari.us/steve) had posted on pumpio that his mongodb pumpio backend needed to be upgraded because of a crash.


Very recently [Dr. Sekula](https://hub.polari.us/steve) had posted on pumpio that his mongodb pumpio backend needed to be upgraded because of a crash.
Turns out, once db size becomes large enough, the x86 mongodb doesn't support it and will just crash -- and apparently this was a design choice.

Maybe a day or two after this happened to him, my own pump (which runs on my vps) crashed and could not recover.
My vps was running Debian 7 x86.

I made some backups and figured I'd just rebuild it with a 64-bit version.
The images that my host (ChicagoVPS) has for x64 debian 7 are badly mangled and is riddled with dependency problems.
While I could've installed Debian 6 x64 and then upgraded, I didn't really feel like it.

I should mention that by this point I had rebuilt the server probably 5 times trying to fix the dep problems.

I looked through the other build options:  many CentOS which is ok, couple of gentoos, the debians, fedora, and then some ubuntus.
I decided to go with Ubuntu x64, and the newest version available was 12.10.

After getting it all set up, I went to restore my backups.  Which is when I discovered that I had backed-up the wrong directory, and my backup only consisted of a bunch of symlinks and no real data.
bummer.

Luckily, I had an encrypted file with my pumpio passphrase in it, and I also had a mongodb backup from a couple of days prior.
These two things are the secret sauce to make the pump work without just rebooting the whole thing with a new domain and such.

I removed apache, which is weird and tries to bind to all of my IPs (I have two), and I installed nginx instead.
Got mongodb running, and then installed my ssl cert stuff.  Then got the pump up and going after `git fetch`ing the latest.

All went well.

Then later that night I realized that 12.10 was pretty old, and after looking it up I saw that support runs out in 2-3 weeks.  d'oh!

The next day I ran the ubuntu upgrade cli tool and everything upgraded without a hitch, nothing was broken.
It's been up and running ever since.

Oh, and I've corrected my backup script so I'm not just grabbing a bunch of symlinks now. :-)

I'm super tired, so I'm going to head off to bed before I doze off.  It's Friday!


PS.

[Here is a pumpio thread](https://io.jrobb.org/jrobb/note/Y_tRIULDRe-e1lN9_UhXDg) for commentation and such.
