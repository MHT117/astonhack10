CREATE TABLE IF NOT EXISTS user_finances (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_name TEXT NOT NULL,
    annual_income REAL NOT NULL,
    net_worth REAL NOT NULL,
    risk_profile TEXT NOCASE CHECK(risk_profile IN ('low', 'moderate', 'high')) NOT NULL,
    essentials_expense REAL NOT NULL,
    discretionary_expense REAL NOT NULL,
    savings_rate_goal REAL NOT NULL
);


