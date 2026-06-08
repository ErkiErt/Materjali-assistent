
# Audit Overview

## What is included
- Streamlit demo app.
- JSON seed data.
- PostgreSQL staging loader.
- PostgreSQL normalization script.
- Normalized schema.
- README usage guide.

## Current data status
- Categories exist for window seals, terrace, marine, construction, snow plowing.
- Seed data includes representative items for those categories.
- Staging ingestion uses JSONB for technical and tag fields.
- Normalized tables exist for categories, materials, material_properties, use_cases, and use_case_rules.

## What is still missing
1. Full technical coverage for every product line.
2. Consistent numeric technical limits for all items.
3. Better synonym and category mapping for free-text queries.
4. Real chemical resistance matrix.
5. A complete fallback ranking table for alternatives.
6. Validation rules before insert for all numeric ranges.
7. More robust indexes for search and filtering.
8. Export/import scripts for production deployment.

## Recommendation
Treat this bundle as a working prototype for testing search, ingestion, and normalization. It is not yet a finished production catalog.
