# PathwayTools-MetabolicCompare
Compare pathways and reactions from pathwayTools metabolism reconstruction (PGDBs) between species. You could compare between 2, 3, 4, 5, and even 6 species at the same time. The result is the comparison analysis of pathways and reactions sets as a Venn diagram.

### Usage
1) Run pathwayTools on python-server mode:
```
        pathway-tools -python
```
&nbsp; &nbsp; &nbsp; &nbsp; Or run:

```python
        python runpt.py
```

2) Choose the organisms id that you want to compare and then execute:
```python
        python main.py organism1 organism2 organismn ...
```
  To know all the organisms metabolic reconstruction ids that are depositated in PathwayTools run:
```python
        PGDBconsult.py
```
### Requierementes
* [pythoncyc](https://github.com/latendre/PythonCyc) python library

* [Pathway-Tools](http://bioinformatics.ai.sri.com/ptools/installation-guide/released/index.html) installed

### Results

Comparing 6 PGDBs(The most complex example):

Each PGDB have a unique code, (000001, 000010, etc), to make easier the visualization of the comparison.
The comparison between each PGDB could be see, for example the 000001 between the 000010 as the 000011:#,  been # the numeric result of the comparison.

You will have two output files,"pathways_groups.txt" and "reactions_groups.txt", in which are listed the elements that are shared by each PGDB.
For example:
Here is the a piece of the pathways_groups.txt file:
```
#000011
#000110
#000111
#101101
PWY0-43	conversion of succinate to propanoate;conversion of succinate to propionate
PWY0-44	D-allose degradation;D-allose catabolism
PROUT-PWY-I	PROUT-PWY-I
PWY0-1495	PWY0-1495
```
The comparison between, 000001 and 000010 doesn't have any match.
But the comparison between 100000, #001000, 000100 and 000001 results in a list of pathways.

You will have two png files images("vennPathways.png" and "vennReactions.png).

Pathways
![alt text](https://github.com/AgustinPardo/PathwayTools-MetabolicCompare/blob/master/vennPathways.png)

Reactions
![alt text](https://github.com/AgustinPardo/PathwayTools-MetabolicCompare/blob/master/vennReactions.png)
