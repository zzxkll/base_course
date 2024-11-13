symbols = 'Python'
symbols_codes = [ord(symbol) for symbol in symbols]
print(symbols_codes)
    
symbols = 'Shake'
symbols_codes = (ord(symbols) for symbol in symbols)
print(symbols_codes)