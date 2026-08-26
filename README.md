# Sheff ll

A python flask app to organize data.  

## running
make a virtualenv and run the app.
```bash
 # create if it does not exist
mkdir ~/.virtualenvs
mkdir ~/git

cd ~/.virtualenvs
python3 -m venv sheff-ll
source sheff-ll/bin/activate
cd ~/git/
git clone https://github.com/thesheff17/sheff-ll
cd sheff-ll
pip install -r requirements.txt
python app.py

# visit http://127.0.0.1:5000 to run app

# run on all IP's
flask run --host=0.0.0.0
```

## Don't we have a thousand apps to store data at this point?

Yes we do but I don't think any are like this. Here is why I think this one is a little different.

* I'm tired of every company scraping my data for AI training and/or advertising.
* I wanted it self hosted.
* I wanted it super simple.  I don't want some complicated database backend setup to manage.
* I wanted something that is a [one to many data model](https://en.wikipedia.org/wiki/One-to-many_(data_model)).
* Fuzzy searching.
* Links should open in new tab.
* Default to today date but also allow you to change it.
* Dark/Light mode.
* Scroll to top button.
* No external 3rd party javascript libraries.
* Supper fast website.

## How do I backup the data?

Everything is written to `data.json` copy this file somewhere for backups.

## Peformance 
Benchmark it for yourself with your hardware. Feels pretty snappy to me.

```bash
./sample_data.py # generates 365 json entries for running for the last year.
cp data.json data_backup.json # make a backup if you have data
cp sample_data.json data.json # copy over sample data file 

# visit http://127.0.0.1:5000 to test app
```

If I had to guess the reading/writing the json is the slowest part. I would try to run this on a ssd with good read/write endurance and speed.  Also swapping in a faster json parser might help like [orjson.](https://github.com/ijl/orjson) Let me know if you see any issues.

### What does the app do not so well?

I would not use the app across multiple browsers at the same time to edit data.  Reading and searching data is completely fine across multiple browser tabs.  This in fact what I use it for 99% of the time.  If you are changing `data.json` automatically be careful also not be editing data in the browser tab at the same time.  A page reload will always cause `data.json` to be read again.  I also don't sanitize any text for this app.  I also left `app.run(debug=True)` on right now as I'm troubleshooting things.  Turn this is off in `app.py` if you don't want it.  Let me know if you see any issues.

### Did I use AI for this tool?

Yes I used google gemini for some help on writing the front end.  I always had this idea how to organize data but the front end structure is hard to get correct.  I also did not want to use any 3rd party javascript libraries to manage this.  I felt like this is a good compromise between the 2.  I have 0 external javascript libraries in this project.