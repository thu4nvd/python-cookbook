#!/usr/bin/python3

user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
username, email, *phone_numbers = user_record
print(email)
print(phone_numbers)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(current)
print(trailing)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)

record = ('ACME', 50, 123.45, (12, 18, 2012))
nom, *_, (*_, year) = record
print(nom)