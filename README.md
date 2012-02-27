Librato API
===========

Usage
=====

Set up your Librato account

    from librato.connection import LibratoConnection

    connection = LibratoConnection("email@example.com","APIKEYHEREDEADBEEF")

	gauge = connection.get_or_create_gauge('my.gauge.name',description="an example gauge")
	for item in range(0,20):
	    gauge.add(item)
	
That's it