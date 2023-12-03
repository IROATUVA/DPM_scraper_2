# DPM_scraper_2

## About

This code was taken from the initial repository called Venmo_scraper written by Mohit, but changed up a little bit so the output prints in a pretty manner in the console, rather than sending it to the secretary. It shows all the current DPMs, how much they've paid, and also money made from dues this semester/this year. Unfortunately, while this code works locally on your computer, it can't be put on the [new treasurer website](https://iro-treasurer.herokuapp.com/). A new updated DPM scraper will (hopefully) be written later to solve this.
THanks! Charlie Meyer

## Experienced programmers quickstart

Clone this repo and open it any ide, run the file `myscraper.py`. follow the google authentication flow by logging in to treasurer@iroatuva.org. Output is in the console.

## How to use - no coding experience necessary

To run this script, first make sure that you have python installed. To check whether you have python installed or not, open a terminal and type `python --version` If you have python installed you'll see something like "Python 3.x.x"; version doesn't (really) matter. If not, you'll get some error message. If you don't have python installed, click [here](https://www.python.org/downloads/). Once you have python installed, open a terminal. 

### Prerequisites to cloning a repository
To clone a repository, you must have git installed which also requires pip to be installed. **IF YOU HAVE A MACBOOK, PIP AND GIT ARE MOST LIKELY AUTOMATICALLY INSTALLED**. Pip usually works once you have python installed, but if you don't have pip, look [here](https://pip.pypa.io/en/stable/installation/). Then, type `pip install git` and press "enter" to install git. If the installer asks you any Y/N questions during the installation, just type "Y" and press enter. Once this is done and no errors occur, move on to the next step.

### Cloning this repository.

For anyone else new to cloning repositories - Once you have all things installed, go onto your desktop and make a new folder. For macs, literally go to your desktop and click "new folder" and make one. Call it something you'll remember, like "TreasurerScraper." Then, click on the folder and COPY it to your clipboard. Then, go to the terminal. To run the program you just cloned, you need to be in that directory. To do this, type "cd" then click CMD+V (paste) - this should then paste a filepath to the folder you just made. It might look something like this: `cd /Users/charlie/Desktop/TreasurerScraper`. Click enter to move into that directory. Then, go to this repository and clone it by typing `git clone https://github.com/IROATUVA/DPM_scraper_2.git`. You have now moved the files to that local repository. Congrats!!

Also sometimes it just crashes on the first attempt to run (idk why), just run it again. 

### Running the script

Once you have the repository cloned onto your local device, type first move in to the new sub-folder created when you cloned the repository within "TreasurerScraper" by typing`cd DPM_scraper_2`. If you do not have `ezgmail` installed, please run `pip install ezgmail`. Then, run the python script. You can do this by simply typing `python myscraper.py` or `python3 myscraper.py`. Alternatively, you can just run it using whatever flavor of IDE you have installed. (If you want to open a folder in vscode from the terminal, just type `code .`). Then, google will prompt you to log in to an account - log in to treasurer@iroatuva.org. The script will run, and you'll see the output in the console! 

### A note about errors, etc

Note that this script is not perfect. This only considers Venmo as a source of dues, and does not include people whose dues have been waves or paid through other means (cash, check, Zelle, CashApp). It is up to the treasurer to account for these people manually. 

Furthermore, it isn't perfect. Sometimes you might see payments of $30 for someone, and that's just something that you need to verify manually by looking in Gmail. 

