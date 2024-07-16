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

GOALS
once external links are found, recursively visit each link

TODO
-color code different file types , logging module
-argument to download all files, backward or forward