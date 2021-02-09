# vtChecker Version 1
A quick script to aid in Virustotal IP lookups using their free api key

This script is aimed at utilizing your free API key from VirusTotal and providing intel lookups on the provided IP's to provide information on:

- Potential Owner/Organization
- Hosting Country of IP Address
- URLs at this IP address that have at least 1 detection on a URL scan
  


# Installation/Running

1.  To properly run the script, you will need to change two variables within the script with your API KEY, and the name of the file containing your list of IP addresses. 

### **Important Notice Before You Can Run the Script**
  - IP list file must be in CSV format(one IP per line). It is recommended to place csv file in the same parent folder of the program, to eliminate having to reference the entire path.
  - The request rate using the public api key is 4/request/minute, 500 request/day, and 15,000 request/month
  - If you run into a json decoder error, this could mean that you have reached your rate limit. Simply wait 1 minute and try script again.
  
- Placing file name/api key values in script tips:
  - Filename Example: If your filename is maliciousip.csv, the variable within the script should be set to **file_name = 'maliciousip.csv'** ( Be sure to to include open/close '')
  - API Example: You can find your API key within your VirusTotal profile, along with your current api quota and usages.

- Libraries you may need to run program:Pandas and Requests. If script doesn't run successfully, do the following commands in your terminal:
  - pip (or pip3) install pandas
  - pip (or pip3) install requests
  - Additional information on installing and general documentation on pip,pandas, and requests can be found here:
    - https://pip.pypa.io/en/stable/installing/
    - https://requests.readthedocs.io/en/master/
    - https://pandas.pydata.org/getting_started.html
  
  

### Variables Example
![variables Examples](https://github.com/cybersecurebyte/vtchecker/blob/main/stuff/variables.png)



# Syntax

From your terminal, simply run:

 python vtChecker.py 


# Output

version 1.0
- IP address
- Potential Owner/Organization of IP address
- Hosting Country of IP address
- Number of malicious detections VirusTotal has for a given IP address.
  
  
# Sample Output Images

### Terminal Output Example

![Terminal Output ](https://github.com/cybersecurebyte/vtchecker/blob/main/stuff/terminal.png)

### CSV Output Example
![CSV Outputt ](https://github.com/cybersecurebyte/vtchecker/blob/main/stuff/csv.png)








  


