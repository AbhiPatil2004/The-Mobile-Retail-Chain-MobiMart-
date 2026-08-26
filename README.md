# MobiMart — Central Inventory Intelligence & Allocation Engine

An algorithmic inventory planning and capital optimization engine designed for **MobiMart**, a retail chain of 25 mobile phone stores across Karnataka (8 Bangalore Flagship stores and 17 Tier-2/3 regional outlets).

This system solves the core retail challenge: **"Capital locked in the wrong phones in the wrong stores"** while strictly respecting a **₹4.00 Crore chain-wide working capital constraint**.

---

## 📌 Problem Overview & Constraints

* **Store Diversity:** Bangalore flagship outlets demand ₹40,000–₹1,50,000 flagships, whereas Tier-2/3 stores (Hubli, Mysore, Davangere) require fast-moving ₹6,000–₹15,000 budget models.
* **Working Capital Cap:** A strict chain-wide ceiling of **₹4.00 Crore** per weekly allocation cycle.
* **Asymmetric Stockout Penalties:** Budget phone stockouts lead to immediate churn (customers buy next door); flagship customers have higher tolerance/wait times.
* **End-of-Life (EOL) Lifecycle:** Rapid product lifecycle (8–10 week peaks) requiring algorithmic markdown vs. inter-store transfer decisions.

---

## 🛠 Tech Stack

* **Backend / Core Engine:** Python 3.11+, Django 5.x
* **Data Processing & Optimization:** NumPy, Pandas
* **Frontend:** Django Templates, Bootstrap 5
* **Database:** SQLite / PostgreSQL

---

##  Key Features

1. **₹4 Crore Constrained Greedy Allocation Engine:**
   * Computes store-level demand scores weighted by margins, category velocity, and opportunity cost.
   * Allocates units dynamically with Rupee justifications.

2. **End-of-Life (EOL) & Transfer Optimization:**
   * Evaluates cost tradeoff: `Inter-store transfer cost (₹300–₹800/unit)` vs. `Markdown liquidation loss (15–30%)`.

3. **Executive Dashboard:**
   * Real-time visibility into deployed capital, remaining buffers, at-risk inventory, and weekly Monday allocations.

---

## ⚙️ Installation & Local Setup

### 1. Clone the repository
git clone https://github.com/<your-username>/mobimart-optimizer.git
cd mobimart-optimizer


### 3. Set up virtual environment
# Windows
python -m venv env
env\Scripts\activate

# Linux / macOS
python3 -m venv env
source env/bin/activate

### 3. Install dependencies
pip install django numpy pandas

### 4. Database Setup & Seeding
python manage.py makemigrations
python manage.py migrate

# Seed 25 Stores and 60 Phone Models
python manage.py shell

Inside Django shell:
from core.services.data_generator import seed_database
seed_database()
exit()


### 5. Run the application
python manage.py runserver
Open [http://127.0.0.1:8000/](https://www.google.com/search?q=http://127.0.0.1:8000/) in your browser.

##  Allocation Engine Logic

The engine prioritizes allocation by computing an Expected Margin Yield per Rupee invested:

$$\text{Allocation Priority Score} = \frac{\text{Expected Demand} \times \text{Unit Margin}}{\text{Unit Cost Price}}$$

Allocations execute iteratively until the cumulative weekly cost reaches the **₹40,000,000** limit.

```

```
