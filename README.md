Zak the bot
Simple chatbot for fun and useful stuff
You must install the "t-gram"-bot-api python wrapper from:
https://github.com/datamachine/twx.botapi


The History of Zak
==================
Zak the chat bot was born during a 24 hr hackathon at Ericsson. We (a bunch of dudes) always had problems deciding on where to have lunch. We were often chatting on the chat at telegram.org. So the idea was that Zak would suggest places and look up menus and present them in the chat. Zak is a member of a group chat so unless triggered by key phrases he remains quiet.

As another hacker had created a lunch menu aggregation web-page (for the Ericsson location) this page is rather convenient to parse for the daily lunch info. Unfortunately the page is only available inside the Ericsson internal network. So for testing purposes, when the aggregator page is unavailable, Zak grabs the menu locally from res/menus.html.

Eventually Zak evolved towards fun without any strengthening of the original lunch-negotiating purpose. He is a rather odd personality. He is normally very cheerful, and loves to call his closest friends by a large number of different nicknames. And he loves to make fun of pepole if they ask for lunch during off hours. But if you try to call him by any nickname such as Zakk, Zacky, Z!ak, Za?k, he gets rather grumpy!

Dizclaimer
==========
The bot code is in a constant state of partial refactoring. Hence the response-lookup is rather inconsistent, for example where all calls to phrases/fixAliasOld() should have been changed to phrases/fixAlias(). The same sort inconsistency is true for  the "phrase understanding" statements [direct and via the "check...()"] in the main loop which should all be wrapped. 