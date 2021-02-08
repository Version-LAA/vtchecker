# vtChecker Version 1
A quick script to aid in Virustotal IP lookups using their free api key

This script is aimed at utilizing your free API key from VirusTotal and providing intel lookups on the provided IP's to provide information on:

- Potential Owner/Organization
- Hosting Country of IP Address
- Number of malicious detections VirusTotal has for a given IP address.
  


# Installation/Running

1.  To properly run the scrip, you will need to change two variables within the script with your API KEY, and the name of the file containing your list of IP addresses. 

- **Important Notice** File must be in CSV format.
- Example: If filename is maliciousip.csv, the variable within the script should be set to **file_name = 'maliciousip.csv'** ( Be sure to to include open/close '')

### Variables Example
![variables Examples](https://github.com/cybersecurebyte/vtchecker/blob/main/variables.png)

2. For ease of use, place CSV file in the same folder as script.



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

![Terminal Output ](https://github.com/cybersecurebyte/vtchecker/blob/main/terminal.png)

### CSV Output Example
![CSV Outputt ](https://github.com/cybersecurebyte/vtchecker/blob/main/csv.png)






  


