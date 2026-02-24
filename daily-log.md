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

## Day 7: 2026-02-14 (Weekend Session 1)
**Focus:** Production-Ready ETL Pipeline - Cryptocurrency Price Tracker
**Time spent:** 3 hours
**What I learned:** 
- Complete ETL workflow (Extract → Transform → Load)
- Real-time API integration with CoinGecko
- Pandas data transformation techniques
- PostgreSQL bulk loading strategies
- Pipeline orchestration patterns
- Production-grade logging (console + file handlers)
- Professional project structure and documentation
- Environment-based configuration management
- Error handling and recovery strategies
**What I built:** 
- Complete end-to-end ETL pipeline
- 11 production-ready files
- PostgreSQL database with proper schema and indexes
- Comprehensive README with examples
- Modular, testable architecture
**Technologies used:** Python, Pandas, PostgreSQL, REST API, psycopg2, dotenv
**GitHub commits:** 1 major project commit
**Key achievements:**
- ✅ First REAL production-grade ETL pipeline
- ✅ Live data extraction from external API
- ✅ Data successfully transformed and loaded to database
- ✅ Professional documentation and code organization
- ✅ Security best practices with .env
**Lines of code:** ~500+ (hand-typed!)
**Blockers:** None
```
Week 1: Python Fundamentals & ETL Basics ✅

Exercises:
├── Day 1: Python basics & CSV handling ✅
├── Day 2: Pandas GROUP BY operations ✅
├── Day 4: Environment variables ✅
├── Day 5: First ETL Pipeline ✅
└── Day 6: Unit testing basics ✅

Projects:
├── Day 3: IPL Data Analysis ✅
└── Day 7: CRYPTO ETL PIPELINE ✅ 🌟

Streak: 7 DAYS

-------------------------------------------------------------------------------------------

---

## Day 8 – Data Modeling Realization

### Key Insight
- Understood difference between:
  - Historical time-series storage
  - Latest snapshot storage
- Chose to keep timestamp-based uniqueness for analytical purposes
- Planned to introduce separate snapshot table for UPSERT logic

### Concept Learned
- **pandas NaN vs PostgreSQL NULL conversion** (critical bug fix!)
- Data modeling depends on business requirement
- Idempotency vs upsert strategy serve different goals
- Systematic debugging using logs
- Production-ready insert patterns

**Added Idempotency:**
```sql
INSERT INTO crypto_prices (...)
VALUES (...)
ON CONFLICT (crypto_id, extracted_at) DO NOTHING;
```

-------------------------------------------------------------------------------------------

## Day 9 – Dual Storage Strategy

- Extended load logic to support snapshot table
- Maintained append-only history table
- Implemented UPSERT-based latest table
- Designed production-style dual-table architecture

-------------------------------------------------------------------------------------------

## Day 10 – Full Dockerization

- Installed WSL + Docker Desktop
- Created Dockerfile
- Created docker-compose setup (ETL + PostgreSQL)
- Implemented automatic table creation
- Resolved restart loop issue
- Handled API rate limiting during container restart
- Successfully executed ETL inside Docker container

Key Concept Learned:
- Container networking
- Self-initializing infrastructure
- Distributed service debugging
- Rate-limit side effects in restart loops

-------------------------------------------------------------------------------------------

## Day 11 – Batch Insert Optimization

- Replaced row-by-row inserts with execute_batch
- Reduced DB round trips
- Added load phase timing
- Improved scalability of ETL pipeline

Concept Learned:
- Network round trip cost in databases
- Bulk insert optimization techniques
- Scaling ingestion systems

-------------------------------------------------------------------------------------------

## Day 14

Practising what I have done so far. Making small refinements and learning the process better.

-------------------------------------------------------------------------------------------

## Day 15

Worked on refining LinkedIn and Naukri. Practised Python today to fill in the gaps that I was having.

Tomorrow's Goal:
- Get started with the next step.
- Will be learning basics of cloud or start Spark / Airflow.

-------------------------------------------------------------------------------------------

## Day 16

Basically nothing today.

-------------------------------------------------------------------------------------------

## Day 17

Python and Pandas practice on Leetcode.

-------------------------------------------------------------------------------------------