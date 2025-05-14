#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import htpasswd


with htpasswd.Basic("user.db") as userdb:
    userdb.pop("bob")
    userdb.add("bob", "1p")
    print(userdb.new_users["bob"])
