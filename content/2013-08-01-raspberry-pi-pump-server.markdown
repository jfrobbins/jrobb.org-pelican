Title: Raspberry Pi Pump Server
Date: 2013-08-01
Modified: 2013-08-01
Category: archive
Tags: raspi, pump, raspberry, pi, pump.io
Slug: 2013-08-01-raspberry-pi-pump-server
Authors: Jon Robbins


My favorite and most-used social network right now is [Pump.io](http://pump.io/), which is created by [e14n](https://github.com/e14n).
Or, mostly it is by [Evan](https://github.com/e14n).
Evan is the creator of famed [StatusNet](http://status.net) software which [identi.ca](https://identi.ca) used to run before its pump conversion, and sites like [quitter.se](http://quitter.se) still run.

![Raspberry Pi Pump (with LCD screen)]({filename}/images/rasPiPump.jpg)

Like most of the people on the pump.io network, I started on one of the e14n servers from the [tryit](http://pump.io/tryit.html) link on the main project page (where there are several to choose from).
Because this software is designed from the ground up to be federated, there are many different servers which all talk to each other (much like when you email someone, it doesn't matter who your email provider is).
Federation is great because even if one of these servers go down, the rest are still up and communicating--compare that to when something like twitter goes down and no on can access the service.

After a while of mooching off of Evan's servers, I decided to start my own pump on my VPS.  
This [turned out badly for me](http://www.jrobb.org/blog/2013/07/05/vps-hackeraging/) due to some hacking nonsense that wiped my server.
So I set up again on my VPS after it was rebuilt, at a different subdomain (so as to not confuse the webfingers).  
After this, there was a bug that caused my pump to not receive any notices...which isn't very social.  (note: that bug is now fixed)

##The Pi##
Around this time I figured I could try to set up my Raspberry Pi and see how well it worked out, a few other guys had done it at this point ([like sazius](https://pi.saz.im/) and didn't have too many problems.

I set my Pi up such that it has a 4GB SD card that it boots on, which contains the `/boot` and `/` partitions.
I then have a 32GB USB drive (that I found under the TV where my kids had hidden it some time ago) which is mostly used as `/home`, and 2GB used as `swap`.

I ran the `sudo raspi-config` to setup things like:

- memory split: I turned the GPU down to 16, since I'm not using the video output at all
- overclocking: I did "modest", it seems stable but clocks a little faster than the default
- changed root pw, keymaps, all that stuff

I also did some normal things:

- created a new user for me to login as, and added it to the sudoers file (but requires pw)
- uploaded my [ssh keys](https://wiki.archlinux.org/index.php/SSH_Keys#Simple_method)
- installed fail2ban
- disabled root and pw login in sshd
- setup a fixed IP on my local network
- forwarded ports 80 and 443 on my router to the Pi
- forwarded port 22 on the router as well, so that I can ssh in (or use [mosh](http://mosh.mit.edu/))
- decided on a subdomain (make sure of this before you start following people, as webfinger is particular)
- created [SSL certificates](https://www.startssl.com/) for the subdomain I was going to use. [How-to](https://github.com/e14n/pump.io/wiki/StartSSL-Free-Certificate)
- created a non-priveledged user with no password just for pump.io (I think "pumpio")
- I am planning to run my pump binding directly to ports 80 and 443--if you have multiple machines using these ports  you may want to look into a [proxy setup](http://whird.jpope.org/2013/03/27/pump/).

##Node##
*Luckily*, there already exists a nodejs binary package for the Raspberry Pi--otherwise it would take forever to compile.

	wget http://nodejs.org/dist/v0.10.2/node-v0.10.2-linux-arm-pi.tar.gz

Obviously sub your desired version in there.

#Get Pumpin#
It is possible that you can install Pump.io from npm like this:

	cd /srv/
	mkdir pump.io && cd pump.io/
	npm install pump.io

However, this version can lag behind a bit--the master branch is the place to be:

	cd /srv/
	git clone https://github.com/e14n/pump.io.git
	cd pump.io

###Config ###

Then it is time to setup the [config file](http://bin.jrobb.org/pipump.io.json). 
Well, I guess you could do it later, but I'll talk about it here. 
I'll summarize some things, but most of this and more is laid out in the [Pump.io README](https://github.com/e14n/pump.io/blob/master/README.md).

    {
        "driver":  "redis",
        "params":  {"port":6379,"database":0},
        "secret": "something secret",
        "noweb":  false,
        "site":  "jrobb/pi",
        "owner":  "jrobb",
        "ownerURL":  "http://pi.jrobb.org/",
        "port":  443,
        "hostname":  "pi.jrobb.org",
        "address":  "0.0.0.0",
        "nologger":  false,
        "serverUser":  "pumpio",
        "uploaddir": "/path/to/pump.io/uploads",
        "debugClient": false,
        "bounce": true,
        "compress": true,
        "key": "/path/to/pump.io/ssl/ssl.key",
        "cert": "/path/to/srv/pump.io/ssl/ssl-unified.crt",
        "disableRegistration": true,
        "noCDN": true,
        "firehose": "ofirehose.com"
    }

###DB Driver###

As you can see here, I'm saying I'll use the redis driver.  

- I tried using leveldb, but this failed some self tests and caused problems
- The disk driver saves everything to disk, and is probably awful speed-wise
- With the memory driver, nothing is retained at shutdown
- MongoDB isn't currently available on the Pi
- Redis is pretty easy to configure and use

I haven't had problems yet using Redis, but the memory usage is crawling up so it may be an issue on the 512MB RAM Pi at some point in the future.

###Secret###

This is what the pump uses to create a hash or something for the web sessions stuff. I'm not exactly sure, but don't change this.
And if you migrate your pump, keep this phrase if you want to use the same webfinger address, and maybe things will work out.


###Address###
IP address to bind to. In my case of using a dynamic IP, `0.0.0.0` is the way to go.


##Install##
After the config is setup, we need to install. This involves the databank you setup in the config.

	cd /srv/pump.io/node_modules/databank/
	npm search databank
	npm install databank-redis
	cd /srv/pump.io/
	npm install

There is also the `-g` option, which is a global install.  I opted for the local install.
At this point, we should be good to go and ready to start the pump.  Or try to.

	cd /srv/pump.io/bin/
	sudo ./pump -c pump.io.json

I run with sudo, but you could run it as root as well. 
As long as you've created the non-priveledged user and set it up in the config, it should drop down to that after binding to the port(s).
If you don't see any errors here, and you get a webpage loading at your web address, we're in business.

One thing to note that is probably obvious: initially you'll need to have the config "disableRegistration" set to `false` so that you can create an account.
If you change it, you'll need to restart the pump (ctrl+C, and repeat the above).

After the config is all set up and everything is working, I use forever to keep my node scripts running.

	sudo npm -g install forever

And then to start the pump I do this (I have it in a bash file called `startpump.sh`) :

	sudo forever -a -e /srv/pump.io/log/pump-err.log start /srv/pump.io/bin/pump -c /srv/pump.io/pump.io.json

And, that is about all there is to it.  
Find a [good client](https://github.com/e14n/pump.io/wiki/Clients) and some people to [follow](https://github.com/e14n/pump.io/wiki/Follow-a-person), and start pumping with [a note](https://github.com/e14n/pump.io/wiki/Post-a-note) or [an image](https://github.com/e14n/pump.io/wiki/Post-an-image) or even [a reply](https://github.com/e14n/pump.io/wiki/Reply).

####A few more things####

- Jpope made a bash script to [crosspost to all the places](http://whird.jpope.org/2013/07/27/crossposting-to-all-the-places/) like Pump, SN, and Diaspora.
- Check out the [Pump.io Wiki](https://github.com/e14n/pump.io/wiki)
- [Pump.io website](http://pump.io/)
- [my pump](https://pi.jrobb.org)



##Commentationing##
I welcome comments/suggestions/criticisms/questions/whatever :

There is a pump.io thread [here](https://pi.jrobb.org/jrobb/note/y6D7oxgYRymgjwAnxQal8w)
and a StatusNet thread [here](http://quitter.se/notice/2095525)
