
AAPL (Apple Inc.):
Number of Shares: 150
Purchase Price per Share: $160
Current Market Price per Share: $180
Total Value: $27,000
Unrealized Gain/Loss: +$3,000
HD (The Home Depot, Inc.):
Number of Shares: 100
Purchase Price per Share: $220
Current Market Price per Share: $240
Total Value: $24,000
Unrealized Gain/Loss: +$2,000
V (Visa Inc.):
Number of Shares: 80
Purchase Price per Share: $190
Current Market Price per Share: $200
Total Value: $16,000
Unrealized Gain/Loss: +$800
VGT (Vanguard Information Technology ETF):
Number of Shares: 50
Purchase Price per Share: $250
Current Market Price per Share: $280
Total Value: $14,000
Unrealized Gain/Loss: +$1,500
VUG (Vanguard Growth ETF):
Number of Shares: 120
Purchase Price per Share: $180
Current Market Price per Share: $200
Total Value: $24,000
Unrealized Gain/Loss: +$2,400





# chi-lab
## Test data format
Current Portfolio Holdings:
- Stock A: 100 shares
- Stock B: 200 shares
- Bond Fund C: $50,000
- ETF D: 300 units

Portfolio Allocation Goals:
- Stocks: 60%
- Bonds: 30%
- Cash: 10%

Investment Goals:
- Long-term growth with moderate risk tolerance
- Outperform the market benchmark by X% annually

Risk Tolerance:
- Moderate

Market Conditions:
- Bullish stock market with expectations of continued growth
- Rising interest rates impacting bond prices

Constraints/Preferences:
- Avoid investing in high-risk speculative stocks
- Prefer dividend-paying stocks for income generation
## Example code
import openai

# Set up OpenAI API key
openai.api_key = 'your_openai_api_key'

def suggest_portfolio_rebalancing(input_data):
    # Call OpenAI API to generate suggestions for portfolio rebalancing
    response = openai.Completion.create(
        engine="davinci",
        prompt=input_data,
        max_tokens=150
    )

    # Extract suggestions from the response
    suggestions = response.choices[0].text.strip()

    return suggestions

def main():
    # Define input data
    portfolio_data = """
    Current Portfolio Allocation:
    - Stocks: 60%
    - Bonds: 30%
    - Cash: 10%

    Current Market Conditions:
    - Stock market: Bullish
    - Bond market: Bearish
    - Interest rates: Rising

    Investment Goals:
    - Long-term growth
    - Moderate risk tolerance
    """

    # Invoke GPT-3 to suggest portfolio rebalancing
    rebalancing_suggestions = suggest_portfolio_rebalancing(portfolio_data)

    # Process and display the suggestions
    print("Portfolio Rebalancing Suggestions:")
    print(rebalancing_suggestions)

if __name__ == "__main__":
    main()
