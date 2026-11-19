
**Data Flow:**
1. **Extract:** Read raw CSV data containing edge cases (nulls, duplicates, bad data)
2. **Transform:** Clean data using PySpark (drop duplicates, handle nulls, cast types, calculate revenue)
3. **Load:** Write aggregated results to optimized Parquet format

## 🛠️ Tech Stack

- **Python 3.9** - Core programming language
- **PySpark 3.5.0** - Distributed data processing framework
- **Docker** - Containerization for reproducibility
- **Parquet** - Columnar storage format for analytics

## 📊 What the Pipeline Does

### Input: Raw Sales Data
The pipeline processes a CSV file with intentional data quality issues:
- Missing values (null quantities)
- Invalid data ("N/A" instead of numeric values)
- Duplicate rows
- Mixed data types

### Transformation Logic
1. **Remove duplicates** - Ensures data integrity
2. **Handle missing values** - Fills nulls with appropriate defaults
3. **Data type casting** - Converts strings to proper numeric types
4. **Business logic** - Calculates revenue (quantity × price)
5. **Aggregation** - Groups by product and sums total revenue

### Output: Clean Analytics Data
Final Parquet file contains:
- Product-level revenue aggregations
- Sorted by total revenue (descending)
- Optimized for fast queries

## 🚀 How to Run

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) installed on your machine

### Step-by-Step Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd pyspark-etl-docker
