import weechat

weechat.register("bookz", "krzivn", ".01", "bonk", "de-hassle finding books", "bubye", "")

"""
# NOT stand alone, meant to be consumed by weechat.
https://weechat.org/
/script load Downloads/books/bookscript/bookz.py

idea:
- remove the manual bullshit
- enter searchterm
- script issues search command
- accepts the zip results
- handles results
- paints menu I can spacebar select downloads
- handles starting the downloads in a civilized manner
"""

def bubye():
    print("bu-bye")
    return null

def buffer_input_cb(data, buffer, input_data):
    # ...
    return weechat.WEECHAT_RC_OK

def buffer_close_cb(data, buffer):
    # ...
    return weechat.WEECHAT_RC_OK

def connectme():
    weechat.command("", "/connect undernet")
    weechat.command("", "/join "+ joinchan)

def join_cb(data, signal, signal_data):
    # signal is for example: "freenode,irc_in2_join"
    # signal_data is IRC message, for example: ":nick!user@host JOIN :#channel"
    server = signal.split(",")[0]
    msg = weechat.info_get_hashtable("irc_message_parse", {"message": signal_data})
    buffer = weechat.info_get("irc_buffer", "%s,%s" % (server, msg["channel"]))
    if buffer:
        weechat.prnt(buffer, "%s (%s) has joined this channel jsfh sdjskjdf sf!" % (msg["nick"], msg["host"]))
    return weechat.WEECHAT_RC_OK

# it is useful here to use "*" as server, to catch JOIN messages on all IRC
# servers
weechat.hook_signal("*,irc_in2_join", "join_cb", "")


joinchan = "#clingclang"

connectme()

weechat.prnt("", "Hello, from python script! This should be loca only!")

#make a buffer (just a text space)
buffer = weechat.buffer_new("mybuffer", "buffer_input_cb", "", "buffer_close_cb", "")
weechat.buffer_set(buffer, "title", "This is title for my buffer.")
weechat.buffer_set(buffer, "localvar_set_no_log", "1")

weechat.command(buffer, "hello") #command is a literal IRC command; msg, join, whever
weechat.prnt(buffer, "Hello, from python script! AND FUCK OFF")
#

buffer2 = weechat.info_get("irc_buffer", "undernet,#clinkclank")
weechat.command(buffer2, "hello IM A BOT")
weechat.prnt(buffer2, "Hello, from python script! AND FUCK OFF - printed to buffer, ocal only")
weechat.prnt(buffer2, buffer2)

#weechat.hook_signal_send("irc_input_send", weechat.WEECHAT_HOOK_SIGNAL_STRING, "freenode;;priority_low;;/whois FlashCode")

buffer2 = weechat.info_get("irc_buffer", "undernet,#rriiyh7h7d8fg")
weechat.command(buffer2, "hello IM A BOT")
weechat.prnt(buffer2, "Hello, from python script! AND FUCK OFF - printed to buffer, ocal only")
weechat.prnt(buffer2, buffer2)

buffer2 = weechat.info_get("irc_buffer", "undernet,#bookz")
weechat.prnt(buffer2, buffer2)

chans = weechat.infolist_get("irc_channel", "", "")
weechat.prnt(buffer, weechat.infolist_fields(chans))

"""
if chans:
    while weechat.infolist_next(chans):
        name = weechat.infolist_string(chans, "name")
        weechat.prnt(buffer, "buffer: %s" % name)
    weechat.infolist_free(chans)
"""
