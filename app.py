from flask import Flask, render_template, request
app = Flask(__name__)
EXCHANGE_RATES = {
    ("USD", "EUR"): 0.85,
    ("EUR", "USD"): 1.18,
    ("GBP", "USD"): 1.26,
    ("USD", "GBP"): 0.79,
    ("JPY", "USD"): 0.007,
    ("USD", "JPY"): 142.5,
    ("USD", "CAD"): 1.34,
    ("USD", "EUR"): 0.85,
    ("EUR", "USD"): 1.18,
    ("GBP", "USD"): 1.26,
    ("USD", "GBP"): 0.79,
    ("JPY", "USD"): 0.007,
    ("USD", "JPY"): 142.5,
    ("USD", "CAD"): 1.34,
    ("CAD", "USD"): 0.75,
    ("USD", "AUD"): 1.55,
    ("AUD", "USD"): 0.65,
    ("USD", "INR"): 83.0,
    ("INR", "USD"): 0.012,
    ("EUR", "CAD"): 1.56,
    ("CAD", "EUR"): 0.64,
    ("AUD", "CAD"): 0.86,
    ("CAD", "AUD"): 1.17,
    ("INR", "GBP"): 0.0095,
    ("GBP", "INR"): 105.0,
    ("USD", "NRP"): 132.5,
    ("NRP", "USD"): 0.0075,
    ("INR", "NRP"): 1.6,
    ("NRP", "INR"): 0.625,
    ("EUR", "NRP"): 150.0,
    ("NRP", "EUR"): 0.0067,
}

@app.route("/", methods=["GET", "POST"])
def currency_converter():
    result = None
    if request.method == "POST":
        try:
            amount = float(request.form.get("amount", 0))
            from_currency = request.form.get("from_currency")
            to_currency = request.form.get("to_currency")

            # If same currency, return the same amount
            if from_currency == to_currency:
                result = f"{amount} {from_currency} = {round(amount, 2)} {to_currency}"
            else:
                rate = EXCHANGE_RATES.get((from_currency, to_currency))
                if rate:
                    converted_amount = amount * rate
                    result = f"{amount} {from_currency} = {round(converted_amount, 2)} {to_currency}"
                else:
                    result = "Conversion rate not available for selected currencies."
        except ValueError:
            result = "Invalid amount. Please enter a valid number."

    return render_template("converter.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)