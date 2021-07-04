from flask import Flask, jsonify, render_template, request
import requests
import json
import pandas as pd 

app = Flask(__name__)

"""@app.route('/',methods=['GET'])
def poke_names():
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151%27')
    data = response.content
    json_data = json.loads(data)
    result = json_data['results']
    df = pd.DataFrame(result) 
    df = df.drop(['url'], axis = 1)
    #poke_desc()
    return render_template('index.html',data=df.to_html(index=False))
"""

@app.route('/',methods=['GET'])
def poke_desc():
    pokemons = []
    number = 0
    while (number < 21):
        number = number + 1
        baseapi = f'https://pokeapi.co/api/v2/pokemon/{number}'
        r = requests.get(baseapi).json()
        d = {
            'number': number,
            'name': r['name'].upper(),
            'speed': r['stats'][-1]['base_stat'],
            'defense': r['stats'][2]['base_stat'],
            'special_defense': r['stats'][4]['base_stat'],
            'attack': r['stats'][1]['base_stat'],
            'special_attack': r['stats'][3]['base_stat'],
            'hp': r['stats'][0]['base_stat'],
            'weight': r['weight'],
            #'image_url': r['sprites']['other']['dream_world']['front_default']
        }
        pokemons.append(d)
    desc_results = pokemons
    pkdf = pd.DataFrame(desc_results)
    pkdf.columns = ['No','NAME','SPEED','DEFENCE','SPECIAL_DEFENCE','ATTACK','SPECIAL_ATTACK','HP','WEIGHT']
    return render_template('result.html',data=pkdf.to_html(index=False)) 

if __name__ == "__main__":
    app.run(debug=True)
