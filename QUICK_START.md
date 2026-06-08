
# Kiire testijuhend

## 1. Ava projekt
Paki ZIP lahti ja mine kausta.

## 2. Käivita Streamlit demo
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 3. Testi otsingut
Proovi neid sisendeid:
- aknatihendit vaja
- terrassile puidu alla kummi
- sadamasse fenderit vaja
- betooni vuugi tihend
- lund lükata
- õlipaagi tihend

## 4. PostgreSQL laadimine
Sea env muutujad:
- PGHOST
- PGPORT
- PGDATABASE
- PGUSER
- PGPASSWORD

Seejärel:
```bash
python load_to_postgres.py
python normalize_to_pg.py
```

## 5. Kontrolli tulemusi
Vaata tabelid:
- categories
- materials
- material_properties
- use_cases
- use_case_rules
- staging_products
