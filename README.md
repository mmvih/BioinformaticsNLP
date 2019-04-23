# BioinformaticsNLP
These codes are to help organize the XML files from PubMed's Open Access Subset.  The methods explained below can be used to help find information on the interactions between bacterias in the oral microbiome by finding all the sentences that mention any two bacteria within the list of given bacterias. 
- The sentences are taken from the Front (Abstract and Introduction), Body (Materials/Methods), and Back (Results, Discussion, and Conclusion) of the paper. It does not include the title or references.
- There is additional code to turn most of those sentences into a .to_dot() format using Stanford's Parser to look at the Dependency Structure of the sentences

**Warning**
These codes have a high time and space complexity. 


**System requirements:**

- Anaconda/Python 4.3.1 or higher
- Natural Language Processing Toolkit (part of Anaconda)
- Stanford Parser


**STEPS**

Download this folder (BioinformaticsNLP)

Download comm_use.A-B.xml.tar.gz from ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/ and place in directory BioinformaticsNLP/.

Make a sub directory in your current directory by running the command (name of directory must be consistent):

> mkdir ABxmlpapers


Given articles.A-B.xml.tar.gz tar file in the folder, we can unzip the tar file in the ABxmlpapers directory by running the commands:

> mv comm_use.articles.A-B.xml.tar.gz ABxmlpapers/

> nohup tar -C /ABxmlpapers -xvf comm_use.articles.A-B.xml.tar.gz &

Optional: For testing purposes, you can remove the number of directories in the downloaded tar file from PubMed's Website after it has been unzipped to reduce the cost of time. To remove the subdirectories, you can use the commands:

> rm -rf [directoryname]/ 

Return to the original directory by 

> cd ..

**Step 1**

The step1.sh script creates three new directories with subdirectories (abxmlwords, abxmlsentences, SpeciesP3).  It tokenizes all the XML papers into words and sentences.  The tokenized words are placed in one output (wordPMC[PMC id].txt) and copied into the abxmlwords/ directory and the tokenized sentences (sentPMC[PMC id].txt) are copied into the abxmlsentences/ directory.  The SpeciesP3 directory is compromised of subdirectories that are named after the bacterias listed in speciesjoined.txt. If the XML paper mentions any bacteria in the list, then both outputs are copied into the respective subdirectories of SpeciesP3.  If any bacteria listed in speciesjoined.txt is not found in any of the papers, then that subdirectory is removed.

Additional notes
- In sentPMC[PMC id].txt, if the bacteria is mentioned by its first intial Genus name and full species name (_G. species_), then it is converted to its full genus and species name concatenated by an underscore so that it is treated as one entity (Genus_species).
- In wordPMC[PMC id].txt, all the stop words are removed. 

Compile the script and run it with the commands:

> chmod u+x step1.sh

> nohup ./step1.sh &

**Step 2**

The step2.sh script creates a new directory, spesets/.  It takes the remaining species left in SpeciesP3/ and creates combinations of 2 amongst them. Each combination has a unique Id, which can be found in bactsets.txt.  The subdirectories in spesets/ are named after those unique ids.  If any two bacteria is mentioned in a paper, then it copies the .nxml file, sentPMC.txt file, and wordPMC.txt file into its respective subdirectory in spesets/.
Compile the script and run it with the commands:

> chmod u+x step2.sh

> nohup ./step2.sh &

**Step 3**

The step3optionl.sh script takes the bacterias in the SpeciesP3/ directory and finds the frequency of the number of times the bacteria was mentioned in each paper.  It appends the outputs all into one .txt file and keeps it in its respective directories named as freq.txt  
Compile the script and run it with the commands:

> chmod u+x step3optional.sh

> nohup ./step3optional.sh &

**Step 4**

The step4.sh script goes through the directory spesets/ and appends all the sentences that mentioned both bacterias into a text file called bothsentbact.txt and all the tokenized words into a text file called bothwordsbact.txt.  If there are no sentences that mention both the bacterias in all the papers that mention both bacterias, then the corresponding subdirectory in speset/ is deleted. 

Compile the script and run it with the commands:

> chmod u+x step4.sh

> nohup ./step4optional.sh &

**Step 5**

The script step5optional.sh takes all the tokenized words in each bothwordsbact.txt file and does a frequency analysis on all the words.  The output, pval.txt, is then moved to its respective subdirectory 

Compile the script and run it with the commands:

> chmod u+x step5optional.sh

> nohup ./step5optional.sh &

**Step 6** 

The script step6optional.sh takes all the tokenized sentences in bothsentbact.txt file and breaks down all the sentences into a .to_dot() format.  The output, broken.txt, is then moved to its respective subdirectory. 

  - Possibility of UnicodeDecodeError & OSError

Compile the script and run it with the commands:

> chmod u+x step6optional.sh

> nohup ./step6optional.sh 




