This is a webcrawler written in python.

You can use it to crawl a domain and get all subdomains, sites, files hosted on it.

to be used purely for educational purposes.

will call it timmy.


issues during development--
[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:997)')))

raise IOError("Could not find a suitable TLS CA certificate bundle, "
OSError: Could not find a suitable TLS CA certificate bundle, invalid path: ca_bundle.crt

program runs into error if certificate is not trusted in all browsers according to sslshopper.com works on sites without any errors on sslshopper.com

16-7-2024
ssl issue doesnt arise anymore, i did not fix it, i do not know how it works now. all i know is it works


15-7-2024
MAJOR refactoring
cleaned the entire code up and put everything in litlle functions

development will be done on develop branch


24-7-2024
added additional features, forward and backward parser
added function to buffer output to external file
    error when using { https://youtube.com/ }, so use { https://youtube.com }, no backslash
added time flag, script will only run for specified time in seconds
used threading

the codebase is a MESS. it looks ugly, but it works so i dont want to change a lot right now.
next task is to maybe draw out a flowchart of script execution, map out exactly what is being done, because right now, i, the guy who wrote this is very confused and then clean the code up. maybe put it all in different modules
after doing this, will push to main


GOALS
once external links are found, recursively visit each link

TODO
-color code different file types (do i have to do this?)
-
