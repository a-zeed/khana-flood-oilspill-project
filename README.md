# Khana Flood & Oil-Spill Exposure Project

**Which settlements in Khana Local Government Area, Rivers State, sit on low-lying land near watercourses — areas more exposed to oil spill spread and flooding?**

Built over twelve months with GeoDev Lab Africa, Cohort One. Khana sits at the heart of Ogoniland, an area with a long history of oil spill contamination and ongoing cleanup (UNEP's 2011 assessment, the HYPREP programme). This project screens which communities sit in terrain that makes them more exposed when spills or floodwater spread.

## Answer so far (Month 1)

Of the 1,815 settlement blocks mapped in Khana LGA, **100 (about 5.5%) sit within 200 metres of a mapped river or stream.** This is far lower than the 25–40% expected going in — see `month-1-summary.md` below for why that gap itself is a real finding, not an error. This answers the "near watercourses" half of the project question. The "low-lying land" half still needs elevation data, which is the next planned step.

## screenshot 
![Week 4 map — settlements near waterways](./week%204/Week4_Map2.png)

## How this repository is organised

| Week | What it covers | Files |
|---|---|---|
| **Week 1** | The question, the study area, and a source link for every dataset needed | [`project-brief.md`](./project-brief.md) |
| **Week 2** | What was downloaded, from where, feature counts, columns, and gaps found in each dataset | [`data-notes.md`](./data-notes.md) |
| **Week 3** | Reprojecting to the correct CRS (EPSG:32632), clipping to Khana, and the five data quality checks | [`week3-crs-notes.md`](./week3-crs-notes.md), plus the analysis-ready files: `study_area_utm32.gpkg`, `settlements_khana_utm32.gpkg`, `waterways_lines_utm32.gpkg`, `waterways_points_utm32.gpkg` |
| **Week 4** | The first real analysis: buffering waterways and finding which settlements fall inside | [`month-1-summary.md`](./month-1-summary.md), [`expectation.txt`](./expectation.txt) (written before the result was known), the result map (PNG), and `waterways_buffer_200m.gpkg` / `settlements_near_waterways.gpkg` |

## The story, start to finish

1. **Week 1** — chose the question and confirmed every dataset it needs actually exists and is downloadable, before committing to it.
2. **Week 2** — downloaded LGA boundaries and settlement extents (GRID3) and waterway lines/points (OpenStreetMap via QuickOSM), and documented exactly what each one contains and where it falls short (e.g. most waterways have no name field, settlements are building-blocks rather than named places).
3. **Week 3** — put everything in the correct coordinate system for measuring distance in this part of Nigeria (EPSG:32632, UTM zone 32N — corrected after an initial wrong-zone attempt), clipped it all to Khana LGA, and ran five quality checks on the prepared data.
4. **Week 4** — ran the first real spatial operation: a 200 m buffer around every waterway, then selected which settlement blocks fall inside it. Checked the result four ways (map, count, hand verification, empty geometry) before trusting it.

   ## Month 2: Development environment and early Python
   Week 5: set up Python, VS Code and the terminal. hello.py runs.
