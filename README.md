# Extract text information from tax return in image format

This is a work I did to help a professor in her research of financial incentivization in NGO. 

There were about 750 scanned tax returns in image form with about 100 pages each. This requires the OCR (optical character recognition) step to be automated so I can just leave the computer to run on its own. This step uses the Python file #1, which process all files in bulk. 

After the OCR step, I have to put all the text into text files and extract the needed chunk of information. I extracted information from the Supplementary page of Schedule J, which specifies how NGO's employees are incentivized for their work. This step poses some challenges as I have to nail down the correct "hooks" on all pages with multiple trial-and-errors. The biggest challenge was to detect a 'hidden character' ('nse') that only showed up when I processed the text file as ACSII and not as Unicode.  Yet, this hidden character was an important hook for the computer to detect the target page. 

Below is an example of the target page. 
![37-0](https://user-images.githubusercontent.com/45189309/72385470-65f8eb00-36d4-11ea-9659-4a80d1e619fd.jpg)
