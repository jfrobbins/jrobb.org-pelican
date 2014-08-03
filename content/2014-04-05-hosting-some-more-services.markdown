Title: Hosting some more services
Date: 2014-04-05 12
Modified: 2014-04-05 12
Category: archive
Tags: hosting,software,owncloud,mediagoblin,pumpio,xmpp
Slug: hosting-some-more-services
Authors: Jon Robbins
Summary: I have had a [vps](/2013/03/12/i-got-a-vps/) for some time now, and I use it for hosting my [pump.io](http://pump.io) node and website mainly.


I have had a [vps](/2013/03/12/i-got-a-vps/) for some time now, and I use it for hosting my [pump.io](http://pump.io) node and website mainly.
Then, I fired up a [minecraft server](http://mc.jrobb.org) that I play on occasionally, and it runs there also.

I've grown tired of depending on SMS, facebook, or gTalk for chat communications so I decided to finally get around to installing an XMPP server.
I found [this link](https://help.ubuntu.com/community/SettingUpJabberServer) and the installation was pretty simple. 
The only problem was when starting the service, it was trying to bind to port 7777 on my first IP (of the two on the VPS), and this was already being used by [hastebin](http://hastebin.com/about.md).
Easy enough, once I found this out with a `netstat -lnp -t tcp` -- I could not config ejabberd to use a different port in the config file (that I could find, anyway!) so I just changed the hastebin config to use a different port.
That was it!  Then the XMPP server was up and running, and I created accounts for my wife and me.

So that was great, I did that yesterday.

The previous weekend, I was wanting my own solution to host some media and obviously there is [mediagoblin](http://mediagoblin.org/) for that.
After [figuring out a few problems](https://io.jrobb.org/jrobb/note/gdrW3Ex9ReWL7bzMf-JzAg) and then [setting up ssl certs](https://io.jrobb.org/jrobb/note/BQHIdrI0QImuqQCWOm9OsA), my mediagoblin was up and running.  
This service is NOT on my VPS-- I had an olderish desktop that was not being used, so I set it up and this actually runs from my home.

I figured while I have this server in my home, I may as well use it for a few more things.  Oh yeah, and I was tired of using Dropbox...

[Enter Owncloud](http://owncloud.org/)!
This setup went very easily, and in no time I had everything up and running, and syncing across my laptop, android phone, and tablet. I had [one mishap](https://io.jrobb.org/jrobb/note/IR8owy-3Rle5MCiNpmaz-A) where I had turned the "sync" setting to "ON" under android account settings, and that killed my battery-- but aside from that it has been great!


I think those are all of the services that I have running at the moment, but it definitely feels good to be able to depend entirely on myself and [free software](https://www.gnu.org/philosophy/free-sw.html) instead of large corporate entities (which are constantly harvesting whatever information that we provide).

