# jsclub-django
## Step 1: Install virtual environment (virtualenv)
```
pip3 install virtualenv
```
## Step 2: Create a virtual environment for our project
Place the virtual environment folder right next to our project folder.
```
cd ..
virtualenv myvenv
```
## Step 3: Activate the virtual environment
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
## Step 4: Install the require plugin
```
cd jsclub-django
pip install -r requirements.txt
```
## Step 5: Running the server
```
python manage.py runserver
```
### Start developing!

### Development Process
I presumely that everything has been set up properly, during the development, when comes to my phase, I have installed several a package named Popper, the description for installion can already be found here, install this package manager with the commands:
```
# With npm
npm i @popperjs/core

# With Yarn
yarn add @popperjs/core
```
