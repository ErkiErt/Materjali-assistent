
CREATE TABLE IF NOT EXISTS categories(code text primary key, name text not null);
CREATE TABLE IF NOT EXISTS materials(code text primary key, name text not null, family text not null, description text, oil_resistance text, fuel_resistance text, uv_resistance text, temp_min int, temp_max int, hardness int);
CREATE TABLE IF NOT EXISTS chemicals(code text primary key, name text not null, phase text, hazard_class text);
CREATE TABLE IF NOT EXISTS compatibility(material_code text references materials(code), chemical_code text references chemicals(code), rating char(1) not null, temp_c int not null, note text, primary key(material_code, chemical_code, temp_c));
CREATE TABLE IF NOT EXISTS synonyms(term text primary key, normalized text not null);
CREATE TABLE IF NOT EXISTS products(sku text primary key, name text not null, category text references categories(code), material_code text references materials(code), technical jsonb not null, search_terms jsonb not null);
