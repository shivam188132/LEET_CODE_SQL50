import ast

def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i.get('job') == 'Director':
            L.append(i['name'])
    return L

# Example usage:
raw_data = '[{"credit_id": "52fe48009251416c750acaaf", "department": "Directing", "gender": 2, "id": 2710, "job": "Director", "name": "James Cameron"}, {"credit_id": "52fe48009251416c750acaaf", "department": "Directing", "gender": 2, "id": 2711, "job": "Assistant Director", "name": "John Doe"}]'

directors = fetch_director(raw_data)


