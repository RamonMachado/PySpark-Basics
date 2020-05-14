# Writing Parquet File

The main objective of this exercise is to learn how to write a data frame into a parquet file in disk.
In this exercise, I load a csv file with a list of meteors registered by NASA. Then I filter and write the new dataframe as parquet.

## Dependencies
- Python 3.7+
- Virtualenv 16.7.9+

## Installation and Execution

In the main directory just run the makefile. It will create the virtual environment and install PySpark.
You can run it by typing in your terminal:

```
$ make install
```

To run, first you need to start your virtual environment by typing:

```
$ source venv/bin/activate
```

And then you can run the code typing:

```
$ python main.py
```


## Uninstall

To uninstall the venv, just open the terminal and type:

```
$ make clean
```

