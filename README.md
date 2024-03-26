# DNS Checker

This project aims to test DNS servers for reachability and speed

There are 2 python scripts to choose from
    dns_test.py is the simpler of the two, where dns_test2.py is a bit more involved and interactive

I welcome anyone to help out with that issue, but becasue everything still just works, I am not to fussed about the error and have no plans on reworking the scripts just to avoid the issue ... for now

Enjoy, and if you are so inclined, buy me a coffee for the effort. <https://mtnsolutions.pro/coffee/>

It is advised to run these scripts in a virtual environment. You will need to install dnspython in the virtual environtnet. To do that, enter the following:

        python3 -m venv my_dns_test_env

        source my_dns_test_env/bin/activate
        (or on Windows: dns_test_env\Scripts\activate)

        pip3 install dnspython

For dns_test.py, you can pass an argument to use a list of pre-defined DNS server by running this script like this

        python3 dns_test.py --use-predefined

Edit the files to change the DNS servers to your liking