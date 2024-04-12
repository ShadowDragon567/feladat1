import yfinance as yf
import matplotlib.pyplot as plt

# Bekérjük a felhasználótól a ticker nevét
ticker = input("Adja meg a ticker nevét: ")

# Lekérjük az adott ticker elmúlt egy évben történt ármozgásának adatait
data = yf.download(ticker, period="1y")

# Kirajzoljuk az ármozgást
data['Adj Close'].plot(title=f"{ticker} részvény árának alakulása az elmúlt egy évben")
plt.xlabel("Dátum")
plt.ylabel("Ár (USD)")
plt.show()

