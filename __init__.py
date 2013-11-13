#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Richard Kellner

import logger
import notify

def get_client(type_, developerkey='', application=''):
    """Get a pushnotify client of the specified type.

    Args:
        type_: A string containing the type of client to get. Valid
            types are 'nma,' 'prowl,', and 'pushover,' for Notify My
            Android, Prowl, and Pushover clients, respectively.
        developerkey: A string containing a valid developer key for the
            given type_ of client.
        application: A string containing the name of the application on
            behalf of whom the client will be sending messages.

    Returns:
        An nma.Client, prowl.Client, or pushover.Client.

    """

    type_ = type_.lower()

    if type_ == 'log':
        if application == '':
            application = 'broadcaster'
        return logger.Client('/tmp/'+ application +'.log')
    elif type_ == 'push':
        return notify.Client(developerkey, application)
#    elif type_ == 'pushover':
#        return pushover.Client(developerkey, application)


if __name__ == '__main__':
    pass
