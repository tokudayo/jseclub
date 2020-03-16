
# First-time installation
PLEASE check out ALL the steps below upon setting up your runtime for the first time
## Step 1: Install virtual environment (virtualenv) if you haven't done so
```
pip3 install virtualenv
```
### Step 1.1: Create a virtual environment for our project
Place the virtual environment folder right next to our project folder.
```
cd ..
virtualenv myvenv
```
### Step 1.2: Activate the virtual environment
For Mac:
```
source myvenv/bin/activate
```
For Window:
```
cd myvenv/Scripts/activate
```
If you're using Git Bash on Window:
```
source myvenv/Scripts/activate
```
Make sure you see (myvenv).
## Step 2: Install required plugins
```
cd jseclub
pip install -r requirements.txt
```
## Step 3: Run the server
```
python manage.py runserver
```
### Start developing!
**Notes:** 

To test the project locally, make sure to switch ```DATABASES``` in jsclub/settings.py

Commit changed files (except settings.py) only

### Development Process
I presumely that everything has been set up properly, during the development, when comes to my phase, I have installed several a package named Popper, the description for installion can already be found here, install this package manager with the commands:
```
# With npm
npm i @popperjs/core

# With Yarn
yarn add @popperjs/core
```
