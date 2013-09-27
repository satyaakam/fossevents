(Initially taken from https://etherpad.mozilla.org/foss-event-site)

Ways of submitting events:
==========================

0. Authentication
------------------------
Facebook/Twitter/google/openid/persona etc etc
no new signup process

1. Email to a id should automatically post the event (to be present from version 1.0)
-------------------------------------------------------------------------------
    We should have some kind of format, so that processing is easy?
    This is easy, first let's develop the product where a machine-readable format is used
     to put in details at the beginning of the email. After this is stabilised we can find a way to    scan the email for the data
     mail should have a block like:
     
     BEGIN_EVENT
     time: <time>
     date: <date>
     title: <title>
     venue: <venue>
     END_EVENT
     
     After this whatever text follows will be added to event description
     Without this format event won't get posted
     When the product is released, it will automatically detect time/date/venue etc from the text  and fill this format. This format is not for public
      
    Also, how to avoid spam?
    A: Moderation queue (what is that??). All posts go to a moderation queue
    Spam is bigger concern -- no idea, some return mail with captcha or link? Bad idea
    [Honestly, I don't like the post by email idea. Better create apps for various platforms if you don't want to hit the website to post an event -- Kaustav] hmmm - debo

2. By tweet? (to be decided after version 1.0)
------------------
   Maybe later, because tweet is 140 chars only and event needs details.

3. Form on the website (to be present from version 0.1)
---------------------------------
   Of course, the cumbersome way will be there.
   Filling in a fixed structure email will be tougher than that. I would myself forget the structure in a few days.
   I agree with Kaustav here.
   
4. App for mobile etc
------------------------------

How
===

 - API which handles submissions, feeds and various display requests
 - Web frontend can be a client which speaks to the API (+1)
 - Email will submit to a fixed email address. Internally email will be piped to a program that forwards email to the API (sunu suggested a cron job for checking the mailbox)
 
Ways of viewing the site:
==================

* A calendar
* Search by keyword, location etc (like fossjobs.in)
* rss/atom feed
* Email subcription - Atomic subscription for each event. Periodic reminders of new events.
* call-for-proposals and other deadlines calendar (like http://lwn.net/Calendar/Monthly/cfp/)
* automatic post to twitter handle @fosseventsin
* export as ics format?

Future functionality --
* analytics on events in India
* visualisation of event data
* Google calender syncing

