# PathwayTools-MetabolicCompare
Compare pathways and reactions from pathwayTools metabolism reconstrucion(PGDBs) between especies. You could compare between 2, 3, 4, 5, and even 6 species at the same time. The result is the conjunction of those pathways and reactions.

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

Each PGDB have a unique code, (000001, 000010, etc), to mqake easi the visualization of the comparison.
Whe you compare for example the 000001 between the 000010 you will have the 000011:#, been # the result of the comparison.

Pathways
![alt text](https://github.com/AgustinPardo/PathwayTools-MetabolicCompare/blob/master/vennPathways.png)

Reactions
![alt text](https://github.com/AgustinPardo/PathwayTools-MetabolicCompare/blob/master/vennReactions.png)
