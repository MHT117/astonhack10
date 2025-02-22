from flask import Flask, render_template, request

app = Flask(__name__)

def basic_budget_allocation(annual_income, essential_pct=50, discretionary_pct=30, savings_pct=20):
    essential = annual_income * (essential_pct / 100)
    discretionary = annual_income * (discretionary_pct / 100)
    savings = annual_income * (savings_pct / 100)
    return {"essentials": essential, "discretionary": discretionary, "savings": savings}

def advanced_wealth_expenditure(net_worth, annual_income, risk_profile):
    if risk_profile.lower() == 'low':
        savings_rate = 0.30
        discretionary_rate = 0.10
        essentials_rate = 0.60
    elif risk_profile.lower() == 'moderate':
        savings_rate = 0.25
        discretionary_rate = 0.15
        essentials_rate = 0.60
    elif risk_profile.lower() == 'high':
        savings_rate = 0.20
        discretionary_rate = 0.20
        essentials_rate = 0.60
    else:
        raise ValueError("Risk profile must be 'low', 'moderate', or 'high'")
    
    savings = annual_income * savings_rate
    discretionary = annual_income * discretionary_rate
    essentials = annual_income * essentials_rate
    
    return {
        "net_worth": net_worth,
        "annual_income": annual_income,
        "allocations": {
            "essentials": essentials,
            "discretionary": discretionary,
            "savings": savings
        }
    }

def expenditure_advisor(annual_income, current_expenses, savings_rate_goal):
    total_expenses = sum(current_expenses.values())
    current_savings = annual_income - total_expenses
    current_savings_rate = current_savings / annual_income
    
    if current_savings_rate < savings_rate_goal:
        message = (
            f"Your current savings rate is {current_savings_rate:.2%}. "
            f"Consider reducing discretionary expenses to reach your goal of {savings_rate_goal:.2%} savings."
        )
    else:
        message = "Your current savings rate meets or exceeds your goal."
    
    return {
        "current_savings_rate": current_savings_rate,
        "savings_rate_goal": savings_rate_goal,
        "message": message
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        annual_income = float(request.form.get('annual_income', 0))
        net_worth = float(request.form.get('net_worth', 0))
        risk_profile = request.form.get('risk_profile', 'moderate')
        
        basic_result = basic_budget_allocation(annual_income)
        advanced_result = advanced_wealth_expenditure(net_worth, annual_income, risk_profile)
        
        essentials_expense = float(request.form.get('essentials', 0))
        discretionary_expense = float(request.form.get('discretionary', 0))
        current_expenses = {
            "essentials": essentials_expense,
            "discretionary": discretionary_expense
        }
        savings_rate_goal = float(request.form.get('savings_rate_goal', 0.25))
        advisor_result = expenditure_advisor(annual_income, current_expenses, savings_rate_goal)
        
        return render_template('results.html', basic=basic_result, advanced=advanced_result, advisor=advisor_result)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
