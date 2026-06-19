# Job: Geospatial & GIS

**You're about to:** work with maps + spatial data — projections, spatial queries, tiles, interactive maps.

> Reputation pulled live **2026-06-19** via `gh api`.

DB side pairs with [postgresql-database](postgresql-database.md) (PostGIS).

---

## Tier A 🟢 — Canonical

### PostGIS
The spatial extension for Postgres — geometry/geography types, spatial indexes + queries. The GIS-in-SQL standard.
- **source:** https://github.com/postgis/postgis
- **reputation:** **2,143★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** PostgreSQL
- **adapt:** fork your spatial schema + index (GiST) choices.

### GeoPandas
Pandas for spatial data — read/write/analyze vector geodata in Python. The Python GIS workhorse.
- **source:** https://github.com/geopandas/geopandas
- **reputation:** **5,156★** · pushed 2026-06-17
- **last_validated:** 2026-06-19
- **assumes:** Python
- **adapt:** fork your CRS handling + spatial joins.

### MapLibre GL JS
Open-source interactive vector maps in the browser (Mapbox GL fork) — the open web-map standard.
- **source:** https://github.com/maplibre/maplibre-gl-js
- **reputation:** **10,868★** · pushed 2026-06-19
- **last_validated:** 2026-06-19
- **assumes:** JS + tiles/style
- **adapt:** fork your style + layers + sources.
