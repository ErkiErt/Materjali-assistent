
CREATE TABLE categories(code text primary key, name text not null);
CREATE TABLE materials(code text primary key, name text not null, family text not null, description text, oil_resistance text, fuel_resistance text, uv_resistance text, chemical_resistance text, temp_min int, temp_max int, hardness int);
CREATE TABLE chemicals(code text primary key, name text not null, phase text, hazard_class text);
CREATE TABLE compatibility(material_code text references materials(code), chemical_code text references chemicals(code), rating char(1) not null, temp_c int not null, note text, primary key(material_code, chemical_code, temp_c));
CREATE TABLE synonyms(term text primary key, normalized text not null);
CREATE TABLE products(sku text primary key, name text not null, category text references categories(code), material_code text references materials(code), technical jsonb not null);
CREATE TABLE search_rules(rule_code text primary key, category text references categories(code), synonyms jsonb not null, must_have jsonb not null, exclude_categories jsonb not null);
CREATE INDEX idx_products_category ON products(category);
CREATE INDEX idx_products_material ON products(material_code);
CREATE INDEX idx_synonyms_normalized ON synonyms(normalized);
CREATE INDEX idx_compat_material ON compatibility(material_code);
CREATE INDEX idx_compat_chemical ON compatibility(chemical_code);
CREATE INDEX idx_search_rules_category ON search_rules(category);
