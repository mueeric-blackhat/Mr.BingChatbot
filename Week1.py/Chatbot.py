import random

# Predefined crypto dataset
crypto_data = {
    "Bitcoin": {
        "price_trend": "up",
        "price_change_7d": "+5%",
        "energy_consumption": "high",
        "sustainability_score": 3,
        "description": "The OG crypto, but drinks energy like coffee"
    },
    "Ethereum": {
        "price_trend": "up",
        "price_change_7d": "+8%",
        "energy_consumption": "medium",
        "sustainability_score": 6,
        "description": "Smart contract king, trying to go green"
    },
    "Cardano": {
        "price_trend": "sideways",
        "price_change_7d": "-1%",
        "energy_consumption": "low",
        "sustainability_score": 9,
        "description": "The academic crypto, loves proof-of-stake"
    },
    "Solana": {
        "price_trend": "up",
        "price_change_7d": "+12%",
        "energy_consumption": "low",
        "sustainability_score": 8,
        "description": "Speedy Gonzalez of blockchains"
    },
    "Algorand": {
        "price_trend": "sideways",
        "price_change_7d": "+2%",
        "energy_consumption": "very low",
        "sustainability_score": 10,
        "description": "The tree-hugger of cryptos, carbon negative!"
    }
}

# Fun responses
greetings = [
    "Hey there crypto explorer! Let's find you a green and growing digital treasure!",
    "Ahoy investor! Ready to navigate the crypto seas with Captain Bing?",
    "Greetings earthling! Let's analyze some alien technology called blockchain!"
]

jokes = [
    "Why did the crypto investor break up with his girlfriend? He wanted to HODL!",
    "What do you call a crypto miner in a Lamborghini? A temporary situation.",
    "Why don't cryptocurrencies get cold? They always have a lot of blocks!"
]

# Helper functions
def get_trending_coins():
    return [coin for coin, data in crypto_data.items() if data["price_trend"] == "up"]

def get_most_sustainable():
    return max(crypto_data.items(), key=lambda x: x[1]["sustainability_score"])

def get_coin_info(coin):
    return crypto_data.get(coin, None)

def bing_response():
    return random.choice([
        "Bing bong!",
        "According to my highly sophisticated algorithms...",
        "Let me consult my crypto crystal ball...",
        "*beep boop* Processing... *beep*",
        "Interesting question! My circuits indicate..."
    ])

# Main chatbot
print("🌟 Welcome to Mr. Bing - Your AI-Powered Financial Sidekick! 🌟")
print(random.choice(greetings))
print("Type 'help' for options or 'exit' to quit.")

while True:
    user_input = input("\nYou: ").lower()
    
    if user_input == 'exit':
        print("Mr. Bing: Until next time, remember: don't invest what you can't afford to lose! *mic drop*")
        break
        
    elif user_input == 'help':
        print("\nMr. Bing: Here's what I can help with:")
        print("- Which crypto is trending up?")
        print("- What's the most sustainable coin?")
        print("- Tell me about [coin name]")
        print("- Tell me a joke")
        print("- exit (to quit)")
        
    elif 'trend' in user_input or 'up' in user_input:
        trending = get_trending_coins()
        response = bing_response()
        print(f"\nMr. Bing: {response} These coins are trending up:")
        for coin in trending:
            data = crypto_data[coin]
            print(f"📈 {coin}: {data['price_change_7d']} this week - {data['description']}")
        print("\nRemember: Past performance doesn't guarantee future results!")
        
    elif 'sustain' in user_input or 'green' in user_input:
        coin, data = get_most_sustainable()
        response = bing_response()
        print(f"\nMr. Bing: {response} The most sustainable coin is {coin} with a score of {data['sustainability_score']}/10!")
        print(f"🌱 {coin}: {data['description']}")
        print(f"Energy consumption: {data['energy_consumption']}")
        print("\nThis one's so green it makes kale jealous!")
        
    elif 'joke' in user_input:
        print(f"\nMr. Bing: {random.choice(jokes)} 😆")
        
    elif 'tell me about' in user_input:
        coin = user_input.replace('tell me about', '').strip().capitalize()
        data = get_coin_info(coin)
        if data:
            response = bing_response()
            print(f"\nMr. Bing: {response} Here's the scoop on {coin}:")
            print(f"📊 Price trend: {data['price_trend']} ({data['price_change_7d']} this week)")
            print(f"⚡ Energy: {data['energy_consumption']}")
            print(f"🌍 Sustainability: {data['sustainability_score']}/10")
            print(f"ℹ️ {data['description']}")
        else:
            print("\nMr. Bing: Hmm, I don't have data on that one. Maybe it's too new or too... questionable?")
            
    else:
        print("\nMr. Bing: Sorry, I didn't catch that! Try asking about trending cryptos, sustainable coins,")
        print("or ask for a joke to lighten the mood! Type 'help' for options.")