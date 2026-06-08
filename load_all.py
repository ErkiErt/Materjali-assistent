
import json
import os
from pathlib import Path
import psycopg2
from psycopg2.extras import Json

BASE = Path(__file__).parent
DB = dict(host=os.getenv('PGHOST','localhost'), port=int(os.getenv('PGPORT','5432')), dbname=os.getenv('PGDATABASE','your_db'), user=os.getenv('PGUSER','your_user'), password=os.getenv('PGPASSWORD','your_password'))

def read(name):
    return json.loads((BASE/'data'/name).read_text(encoding='utf-8'))

def main():
    conn = psycopg2.connect(**DB)
    try:
        with conn:
            with conn.cursor() as cur:
                for row in read('categories.json'):
                    cur.execute('INSERT INTO categories(code,name) VALUES (%s,%s) ON CONFLICT (code) DO NOTHING', (row['code'], row['name']))
                for row in read('materials.json'):
                    cur.execute('INSERT INTO materials(code,name,family,description,oil_resistance,fuel_resistance,uv_resistance,chemical_resistance,temp_min,temp_max,hardness) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (code) DO NOTHING', (row['code'], row['name'], row['family'], row['description'], row['oil_resistance'], row['fuel_resistance'], row['uv_resistance'], row['chemical_resistance'], row['temp_min'], row['temp_max'], row['hardness']))
                for row in read('chemicals.json'):
                    cur.execute('INSERT INTO chemicals(code,name,phase,hazard_class) VALUES (%s,%s,%s,%s) ON CONFLICT (code) DO NOTHING', (row['code'], row['name'], row['phase'], row['hazard_class']))
                for row in read('compatibility.json'):
                    cur.execute('INSERT INTO compatibility(material_code,chemical_code,rating,temp_c,note) VALUES (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING', (row['material_code'], row['chemical_code'], row['rating'], row['temp_c'], row['note']))
                for row in read('synonyms.json'):
                    cur.execute('INSERT INTO synonyms(term,normalized) VALUES (%s,%s) ON CONFLICT (term) DO NOTHING', (row['term'], row['normalized']))
                for row in read('search_rules.json'):
                    cur.execute('INSERT INTO search_rules(rule_code,category,synonyms,must_have,exclude_categories) VALUES (%s,%s,%s::jsonb,%s::jsonb,%s::jsonb) ON CONFLICT (rule_code) DO NOTHING', (row['rule_code'], row['category'], Json(row['synonyms']), Json(row['must_have']), Json(row['exclude_categories'])))
                for row in read('products.json'):
                    cur.execute('INSERT INTO products(sku,name,category,material_code,technical) VALUES (%s,%s,%s,%s,%s::jsonb) ON CONFLICT (sku) DO NOTHING', (row['sku'], row['name'], row['category'], row['material_code'], Json(row['technical'])))
        print('loaded')
    finally:
        conn.close()

if __name__ == '__main__':
    main()
