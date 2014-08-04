Title: My Irssi setup
Date: 2013-07-20
Category: archive
Tags: 
Slug: 2013-07-20-my-irssi-setup
Authors: Jon Robbins


I've never been much of a chat person, even IRC.  Typically I would just pop in when I'm having problems.
Lately I've been getting on IRC a bit more, initially to chat with people about [pump.io](http://pump.io) bugs and problems, and then just to chat because there are some cool people there.

Anyway, I was using XChat to begin with, because it was installed by default on my [LMDE](http://www.linuxmint.com/download_lmde.php) install, and it is easy to use.
XChat is great, however in the past I used [irssi](http://www.irssi.org/) quite a bit and remembered liking it, so I thought I would give it a go.

And, the default configuration kind of sucks. XChat really has me spoiled with features.
*Luckily* someone has already done all of this custimization work, so I can copy what [other people](http://www.antonfagerberg.com/archive/my-perfect-irssi-setup) have done and just grab the bits that I like.

I'll never remember all this, so I am making a blog post if I need to set it up again later.

## Installation & Getting Started ##
I use LMDE, so the normal debian way works.
    sudo apt-get install irssi screen

I may be interested in some of the other things from the link above at some point, but I haven't installed them yet.
For instance otr:
    sudo apt-get install irssi-plugin-otr

To learn how to use irssi including basic usage, their site goes about explaining a lot of it somewhere [around here](http://www.irssi.org/documentation/startup#c3).
Some basics to get started:
    /nick mynick
    /server ADD -auto -network NetworkName irc.host.com 6667
    /channel ADD -auto #channel NetworkName password

Pretty easy. I switch channel windows with CTRL + left / right arrow, or CTRL + window number.
Save your setup:
    /save

There's a good start to a config file. (which is in ~/.irssi/).


    
## Themes ##

So there really are a ton of [themes](http://irssi.org/themes), I haven't even begun to look through them all.
I just went with the standard one from the post I was reading, [http://irssi.org/themefiles/xchat.theme](http://irssi.org/themefiles/xchat.theme).  Hey, XChat is comforting.
I saved that file into ~/.irssi/ and loaded it with:
    /set theme xchat
Then to save the setup, I believe it is:
    /layout save



## Scripts ##
This is where things get interesting. Basically, all of the cool things that XChat does for you that we all know and love...
irssi does not do.  By default, that is.
There are a ton of scripts available to do a myriad of things, but I'll only barely scratch the surface here.
You can find a lot of scripts on Irssi’s official script site: [http://scripts.irssi.org/](http://scripts.irssi.org/)

You can load scripts if you load the script into your ~/.irssi/scripts/ dir:
    /script load myscript.pl
or, if you put them in your ~/.irssi/scripts/autorun/ dir like me:
    /run autorun/somescript.pl

## Nicklist ##
Not having a nicklist along the side was driving me crazy. There's a fix for that.
There are a few ways to do it, actually, but I'm the most familiar with screen, and this setup is straightforward (and easy).

To start with, I saved the nicklist file from here: [http://scripts.irssi.org/scripts/nicklist.pl](http://scripts.irssi.org/scripts/nicklist.pl) into my ~/.irssi/scripts/autorun/ directory.
Basically you start Irssi inside of a GNU Screen window, then enable the script.  If you don't run it in screen, I don't even know what would happen, but I imagine that it wouldn't work.
    screen irssi
    /nicklist screen

Here is a guide all about using irssi with screen, which is useful for information as well. I'll pull some stuff from here later on: [http://quadpoint.org/articles/irssi](http://quadpoint.org/articles/irssi).

## XChat Nick Color ##
> This script works together with the xchat-theme (as you can find if you scroll up a bit) and does two very important things. First of all, it aligns all nicknames to the right in the chat area which creates a vertical line with the chat messages. This makes it a lot easier to read. And secondly, it will give all nicknames a unique color so it is easier to see who sends what.

Download: [http://dave.waxman.org/irssi/xchatnickcolor.pl](http://dave.waxman.org/irssi/xchatnickcolor.pl)

## Hilight Window ##
Without this, your name (or other words) don't get highlighted so you never really know.
Now, with this plugin, a new irssi window is made and all of these messages are placed in there.
That's ok, but we can also permanently set this window to display over the main chat area like this:
    /window new split
    /window name hilight
    /window size 4
    /hilight -word yournick
    /help hilight
Save setup again:
    /layout save
    /save

Download: [http://scripts.irssi.org/scripts/hilightwin.pl](http://scripts.irssi.org/scripts/hilightwin.pl) More info: http://quadpoint.org/articles/irssi#hilight_window

## Advanced Window List (AWL) ##
This one is pretty great. By default, I never knew what the irssi statusbar was saying--with this script we can change it up and make it decent.
Download [adv_windowlist.pl](http://anti.teamidiot.de/static/nei/*/Code/Irssi/adv_windowlist.pl)
Put the script in ~/.irssi/scripts/autorun and run it:
    /run autorun/adv_windowlist.pl

> Upon loading, AWL will create new statusbars on its own. AWL is an updated version of the older chanact.pl script. AWL has many, many new features developed by Nei. It would be worth your time to read the comments at the top of the script to get a feel for what all you can do with it (an entire article could be written on the features of this script and how to use them).

We don't need the "Act" statusbar thing anymore. It says "(Act: 2)" when activity happens on window 2, which I just found out, but with awl and these changes we won't need that.
    /statusbar window remove act
There are a bunch of settings you can look into, but I am keeping it simple.
    /set awl

The settings I am currently using:
    /set awl_block -14
    /set awl_display_key $Q%K|$N%n $H$C$S
    /set awl_display_key_active $Q%K|$N%n $H%U$C%n$S
    /set awl_display_nokey [$N]$H$C$S

> If you like the setup, type /save to keep it. You can revert to the old act setup using /script unload adv_windowlist and /statusbar window add -after lag -priority 10 act.

## Auto Away ##
Who doesn't want this?  It will mark you as away when Screen detects that you are not active in the session.
Download: http://scripts.irssi.org/scripts/screen_away.pl

    /set screen_away_active ON
    /set screen_away_message
    /set screen_away_nick

This one isn't quite working right for me, though.

## usercount ##
This shows a count of the number of users in the selected channel.
Download: [usercount.pl](http://www.irssi.org/scripts/scripts/usercount.pl)
    /script load usercount.pl
    /statusbar window add usercount
    # You can also add -alignment left|right option

## Conclusion ##

As of today ( July 20th, 2013 ), that is my setup for irssi.  I'm liking it quite a bit again, though I don't know if I will stick with it...
XChat is just so **easy**.  This is nice though, and it is in a terminal, so I could install it on my VPS or any server.

Later on if I try the OTR or other features I will update this post.

## Screenshot ##
Below is a screenshot of the (currently unbusy) *#pump.io*.

- _**GNU Screen** + the **nicklist** script:_ Along the right you see the nicks in the channel
- _**hilight window** script:_ At the top is a mention (note it specifies it was in a separate channel)
- _**awl** script:_ Along the bottom above the entry box it shows the channel windows I have open. Current channel underlined. If another channel has activity, it changes color


![My Irssi Setup ]({filename}/images/irssi_setup.png)


## Conversation ##
I posted this to pump.io, so [the conversation could be here](https://microca.st/jrobb/note/4x5X853dQ3mGKBLxxAdIzA)

