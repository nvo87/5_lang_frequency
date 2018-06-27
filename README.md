# Frequency Analysis of Words

This script counts words using frequency and sort it out in ascending order. You may change words amount to output.

# How to start

Script requires you Python 3.5  
Start on Linux

```bash
$ python lang_frequency.py <filepath/to/.txt> -n
```
**For example**, 
```bash
$ python lang_frequency.py lt1.txt -words_amount 5
```
Just put your .txt to project folder.   
`-words_amount` isn't necessary. You may miss it, then words amount will be 10, by default.  
For example, you may download "War and peace" by L. Tolstoy from [here](http://www.knigitxt.com/download/8762.html).  

**lang_frequency.py** returns:
```
and 21422 
in 11134
not 8780 
what 5350 
he 1121 
```

Start on windows is the same.

For more information, type
```bash
$ python lang_frequency.py -h
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
