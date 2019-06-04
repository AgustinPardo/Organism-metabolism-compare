# PathwayTools-RetrieveData
Compare pathways and reactions from pathwayTools metabolism reconstrucion between especies. You could compare between 2, 3, 4, 5, and even 6 species at the same time.

### Usage
1) Run pathwayTools on python-server mode:
```
        pathway-tools -python
```
&nbsp; &nbsp; &nbsp; &nbsp; Or run:

```python
        python runpt.py
```

2) Choose the organisms id that you want to compare and then excute:
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
