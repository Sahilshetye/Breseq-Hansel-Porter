Breseq extractor

==================================

this is a simple data extractor for breseq built using
-Beautifull soup
-Cython
-VCF Reader
-Samtools(specially tabix)


=================================================================
 The tool was written with a basic intent of extracting data
 from breseq  output file

 The Colum data was picked up and compared to our existing
 databases in the local network for further processing


 =====================================================================
 Further Improveent:

 1. Ading Unit test
 2. Adding ability to export data in CSV
 3. Extending Soup to  out output.html in breseq (Currently only supports  index.html )
 4. Improving the logging of the file
 5