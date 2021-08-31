import urllib.request, os, time, urllib.parse
import pandas as pd

# Download the latest list of phishing websites from PhishTank

class phishTank:

    def __init__(self,url):
        self.url=url

    def check(self):
    	return self.check_site(self.url)

    def get_phish_list(self):
        urllib.request.urlretrieve ('http://data.phishtank.com/data/24d4a2596683b35021085b8043dbda93cc3306a6e5f36f86cdc5b28bf35e2427/online-valid.csv', "phish.csv")

    # Check if phish lists exists (and get it if it doesn't) and update if older than 60 minutes
    def update_phish_list(self,file):
        if not os.path.exists(file):
            self.get_phish_list()
            return True # Return True if csv was updated
        if (time.time() - os.path.getmtime(file)) > 3600*24:
            self.get_phish_list()
            return True # Return True if csv was updated
        return False # Return False if csv was not updated
        
    # Import the csv
    def import_phish_list(self,csv_file):
        return pd.read_csv(csv_file)
        
    # Check if a site is flagged as phishing
    def check_phish(self,site, phish_lst):

        for i in range(len(phish_lst.url)):
            if site in phish_lst.url[i]:
                print(site,phish_lst.url)
                return 1 # Return True if the site is flagged as phishing
        return 0 # Return False if the site is not flagged as phishing

    # Check if the site is https


    # Full check of http and phishing record
    def check_site(self,site):
        self.update_phish_list("phish.csv")
        phishList = self.import_phish_list("phish.csv")
        isPhish = self.check_phish(site, phishList)
        
        return isPhish

