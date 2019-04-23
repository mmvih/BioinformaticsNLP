# BioinformaticsNLP
These codes are to help streamline and organize XML files from PubMed's Open Access Subset to find interactions between two bacterias in the oral microbiome. 

**System requirements:**

- Anaconda/Python 4.3.1 or higher
- Natural Language Processing Toolkit 
- Stanford Parser


**Steps**

Make a sub directory in your current directory by running the command:

> mkdir ABxmlpapers


Given articles.A-B.xml.tar.gz tar file in the folder, we can unzip the tar file in the ABxmlpapers directory by running the commands:

> mv articles.A-B.xml.tar.gz ABxmlpapers/

> tar -C /ABxmlpapers -xvf articles.A-B.xml.tar.gz &

- The "&" allows the folder to be unzipped in the background
