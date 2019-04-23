# BioinformaticsNLP
These codes are to help streamline and organize XML files from PubMed's Open Access Subset to help find interactions between two bacterias in the oral microbiome. 

**System requirements:**

- Anaconda/Python 4.3.1 or higher
- Natural Language Processing Toolkit 
- Stanford Parser


**Steps**

Download this folder (BioinformaticsNLP)

Download comm_use.A-B.xml.tar.gz from ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/ and place in directory BioinformaticsNLP/.

Make a sub directory in your current directory by running the command:

> mkdir ABxmlpapers


Given articles.A-B.xml.tar.gz tar file in the folder, we can unzip the tar file in the ABxmlpapers directory by running the commands:

> mv comm_use.articles.A-B.xml.tar.gz ABxmlpapers/

> nohup tar -C /ABxmlpapers -xvf comm_use.articles.A-B.xml.tar.gz &

Return to the original directory by 

> cd ..


