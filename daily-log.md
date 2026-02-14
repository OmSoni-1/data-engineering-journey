# Daily Learning Log – Data Engineering Journey

---

## Day 1 – Python CSV ETL

### What I built
- A Python ETL script that reads CSV input data
- Applied business rules using pandas
- Generated a clean output CSV after transformation

### Concepts learned
- ETL structure in Python (Extract, Transform, Load)
- pandas CSV handling
- Using pathlib for clean file paths

### Output
- Filtered completed orders from 2024 onwards

### Time spent
- ~2 hours

-------------------------------------------------------------------------------------------

## Day 2 – Pandas GroupBy on Sales Data

### What I built
- A pandas aggregation pipeline on transactional sales data
- Generated regional revenue and quantity metrics

### Business Logic Applied
- Filtered only completed orders
- Considered data from 2026 onwards
- Aggregated sales metrics by region

### SQL Concepts Applied
- WHERE
- GROUP BY
- COUNT, SUM, AVG

### Concepts learned
- Handling dates in pandas
- Multi-metric aggregations
- Translating business rules into code

### Output
- Regional sales summary CSV

### Time spent
- ~2 hours

### Repo Improvement
- Refactored folder structure to separate daily projects
- Organized Week 1 work into day-wise pipelines

Note: Reduced intensity due to fever. Focused on cleanup and structure. But I did show up. Keep it up!

-------------------------------------------------------------------------------------------

## Day 3: IPL Data Analysis - Complete mini-project
**Time spent:** 3 hours
**What I learned:** 
- Complex groupby operations
- Multiple aggregations in one query
- Combining data from different analyses
- Creating professional README
- Project structure best practices
**What I built:** 
- Complete data analysis pipeline
- 4 different analysis outputs
- Professional documentation
**GitHub commits:** 1
**Files created:** 3 Python scripts, 2 CSV inputs, 4 CSV outputs, 1 README
**Blockers:** None
**Key insight:** Pandas groupby() is incredibly powerful - just like SQL GROUP BY but more flexible!
**Tomorrow's goal:** Connecting Python to PostgreSQL

-------------------------------------------------------------------------------------------

## Day 4 – Environment-Based Configuration (dotenv)

### What I Built
- Introduced `.env` file for dynamic configuration
- Removed hardcoded year and status filters
- Made the sales pipeline environment-driven

### Key Changes
- Loaded environment variables using `python-dotenv`
- Explicitly resolved `.env` path from repo root
- Converted environment year filter to proper datetime
- Fixed variable naming and load-order bugs

### Debugging Lessons
- Environment variables must be loaded before `os.getenv()`
- Comparing datetime with string causes dtype errors
- `Path.parent` vs `Path.parents` difference

### Engineering Upgrade
- Pipeline is now configurable
- Logic separated from environment
- Reduced hardcoding
- More production-ready structure

### Time Spent
- ~60 minutes (including debugging and venv recovery)

-------------------------------------------------------------------------------------------


## Day 5 – Consolidation & Modular Architecture

### What I Did
- Refactored sales pipeline into modular structure:
  - `config.py` → environment handling
  - `pipeline.py` → ETL logic
  - `run.py` → execution entrypoint
- Centralized environment variable loading
- Enforced numeric validation for `DATA_YEAR`
- Debugged import chain failure caused by config errors
- Fixed logical date filtering bug (`>=` vs `==`)

### Key Engineering Lessons
- Module import chains fail silently if a dependency raises errors
- Environment variables must be validated and type-casted
- Separation of concerns improves maintainability
- Refactoring often reveals hidden logical bugs
- Running scripts from correct working directory matters

### Conceptual Consolidation
- ETL structure
- dotenv configuration
- pathlib usage
- pandas date handling
- Python module mechanics
- Defensive validation

### Why This Matters
- Code is now scalable and production-ready
- Cleaner architecture for future upgrades
- Stronger debugging instincts developed

### Time Spent
- ~1 hour consolidation session

-------------------------------------------------------------------------------------------


## Day 6 – Introduction to Unit Testing (pytest)

### What I Built
- Added pytest-based unit tests for the modular sales pipeline
- Created `tests/test_pipeline.py`
- Validated transformation logic and filtering behavior

### Debugging & Fixes
- Resolved import path issues for tests
- Learned to run pytest using `python -m pytest`
- Fixed column typo in test data (`order_is` → `order_id`)
- Understood how missing schema causes aggregation failure

### Concepts Reinforced
- Unit testing fundamentals
- Testing business logic independently of execution
- DataFrame-based test case construction
- Understanding implicit schema contracts
- Reading and interpreting pytest stack traces

### Why This Matters
- Prevents regressions during refactors
- Validates business logic deterministically
- Increases confidence in code changes
- Moves project toward production engineering standards

### Time Spent
- ~1 hour (late night light session)

-------------------------------------------------------------------------------------------