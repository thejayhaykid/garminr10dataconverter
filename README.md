# Garmin Approach R10 Data Converter

Small, simple script to convert Garmin R10 data extracts from json files to Excel compatible \*.csv files.

## Why

As of now, Garmin does not provide any meaningful way of exporting the data from your Golf (simulator) sessions performed with the R10 launch monitor device. Yet, sometimes it might be beneficial to gain deeper insights by slicing & dicing your data according to your own needs. I therefore searched for a way to obtain my session data and export it into an easy-to-use format (here, .csv which could also be used with Excel etc.).
Please note, that I show you a way to work around Garmin's limitations when it comes to analyzing your own session data. This is in no way any official or to Garmin related procedure. The script is provided as-is and without any support. Adapt it to your needs if required.

## How to use the script

### Installing Locally outside of the virtual environment

If you wish to just use this package without changing the code, there are only a couple of steps.

**Requirement**: You must have Python 3.8^ installed, I have not tested on anything less

1. Go to www.garmin.com -> log into your account -> go to "Account" -> click on "Export Your Data" -> click on "REQUEST DATA EXPORT". The web page responds with a green highlighted "Your request has successfully been submitted."
2. Wait for an email to arrive at your email address registered with Garmin (delivery of the mail might vary from a few minutes to - according to garmin - up to 30 days)
3. Follow the instructions from the email to download your compiled data history from Garmin
4. Clone this git repo locally
5. In a terminal navigate to the root folder of the repo
6. Enter `pip install .` into the terminal and let the install complete
7. Either navigate to the top level folder of the downloaded and unzipped folder, or include a `-i=/path/to/folder` flag in the CLI
8. Result is a new \_.csv file containing all data from your Golf simulator session (including driving range). This file will be saved in whatever folder you are executing the command from
9. Have fun analyzing your data

---

## Usage Instructions

This project was tested on Linux and macOS only (**_NOTE: On my MacBook, I had to use `$ python3` and `$ pip3` to get the correct versions as Python 2 is preinstalled_**), the process for virtualenv is [a little different for Windows](https://python.land/virtual-environments/virtualenv).

Open a terminal window and navigate to the root folder of this project

```bash
$ cd /path/to/root/garminr10dataconverter
```

Virtualenv is required with Python 3.6, if you do not have virtualenv installed, run this command:

```bash
$ pip install -U virtualenv
```

_Note: if you have Python 2 and Python 3 installed, you may need to use `pip3` instead or enter the command like `$ python3.8 -m pip install -U virtualenv`_

With virtualenv installed, create a virtualenv while remaining in the root folder:

```bash
$ virtualenv venv
```

Activate virtualenv:

```bash
$ source ./env/bin/activate
```

Then install needed packages:

```bash
(venv) $ pip install -r requirements.txt
(venv) $ pip install -e .
```

_The second command installs the local package, allowing use with the `gar10` CLI while in the virtualenv._

After that you should be able to run the main.py file `(venv) $ gar10`.

With the Paypr CLI, you can use the following flags:

- `--help` -- Will pull up a well formatted listing of all of the flags
- `-i`, `--input TEXT` - The input file, must be an image. [required]
- `-s`, `--size [HD|FHD|WUXGA|QHD|2K|UHD|4K|5K]` -- The output size for the wallpaper. Format options are HD, FHD, WUXGA, QHD, 2K, UHD, 4K, and 5K

Any of the two flags not accounted for will receive a prompt to enter the value.

When done, exit the virtualenv with:

```bash
(venv) $ deactivate
```
