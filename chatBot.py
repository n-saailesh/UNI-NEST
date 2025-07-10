def retrival_from_html(city, minimum, maximum, structures):
    
    print(city, minimum, maximum, structures)

    return f"{city} {minimum} {maximum} {structures}"



retrival_from_html("brampton, ontario", "1000", "2000", ["apartment", "house"])