# Consolidate excel and csv files

This code is just for consolidating multiple csv and excel files which have the completely same schema.

## Getting Started

Need to install all dependent modules by pipenv.
Modules are glob, pandas, argparse, os and xlrd.

You need to prepare the folder to run the code in advance.
The folder has 2 folders, named input and output.

## Running the tests
You run the code with the command as below.
```
python consolidate.py 'YOUR FOLDER LOCATION'
```

If the code finished successfuly, "all_data.csv" is available from your 'output' folder.
