#!/usr/bin/env python3

# standard library
import json
import os
from datetime import date

# 3rd party library
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DATA_FILE = 'data.json'

def load_data():
    """Load data from JSON file or create default structure."""
    if not os.path.exists(DATA_FILE):
        default_data = {
            "Sample List": [
                {
                    "title": "sample title", 
                    "date": date.today().isoformat(),
                    "url": "https://github.com/thesheff17/sheff-ll",
                    "text": "sample data"
                }
            ]
        }
        save_data(default_data)
        return default_data
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    """Save the dictionary data to disk."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def sort_entries_by_date(entries):
    """Sort entries in-place from newest date to oldest date."""
    entries.sort(key=lambda x: x.get('date', ''), reverse=True)

@app.route('/')
def index():
    data = load_data()
    active_list = request.args.get('list')
    if not active_list or active_list not in data:
        active_list = list(data.keys())[0] if data else None
    
    if active_list and active_list in data:
        sort_entries_by_date(data[active_list])

    today_date = date.today().isoformat()
    return render_template('index.html', data=data, active_list=active_list, today_date=today_date)

# --- List Operations ---

@app.route('/add_list', methods=['POST'])
def add_list():
    list_name = request.form.get('list_name', '').strip()
    data = load_data()
    if list_name and list_name not in data:
        data[list_name] = []
        save_data(data)
    return redirect(url_for('index', list=list_name))

@app.route('/delete_list/<list_name>', methods=['POST'])
def delete_list(list_name):
    data = load_data()
    if list_name in data:
        del data[list_name]
        save_data(data)
    return redirect(url_for('index'))

# --- Item Operations ---

@app.route('/add_item/<list_name>', methods=['POST'])
def add_item(list_name):
    title = request.form.get('title', '').strip()
    entry_date = request.form.get('date', date.today().isoformat())
    url = request.form.get('url', '').strip()
    text = request.form.get('text', '').strip()
    data = load_data()
    
    if list_name in data and (title or text or url):
        data[list_name].append({
            'title': title, 
            'date': entry_date, 
            'url': url, 
            'text': text
        })
        sort_entries_by_date(data[list_name])
        save_data(data)
        
    return redirect(url_for('index', list=list_name))

@app.route('/edit_item/<list_name>/<int:item_id>', methods=['POST'])
def edit_item(list_name, item_id):
    title = request.form.get('title', '').strip()
    entry_date = request.form.get('date', date.today().isoformat())
    url = request.form.get('url', '').strip()
    text = request.form.get('text', '').strip()
    data = load_data()
    
    if list_name in data:
        sort_entries_by_date(data[list_name])
        if 0 <= item_id < len(data[list_name]):
            data[list_name][item_id] = {
                'title': title, 
                'date': entry_date, 
                'url': url, 
                'text': text
            }
            sort_entries_by_date(data[list_name])
            save_data(data)
        
    return redirect(url_for('index', list=list_name))

@app.route('/delete_item/<list_name>/<int:item_id>', methods=['POST'])
def delete_item(list_name, item_id):
    data = load_data()
    if list_name in data:
        sort_entries_by_date(data[list_name])
        if 0 <= item_id < len(data[list_name]):
            data[list_name].pop(item_id)
            save_data(data)
        
    return redirect(url_for('index', list=list_name))

if __name__ == '__main__':
    app.run(debug=True)
