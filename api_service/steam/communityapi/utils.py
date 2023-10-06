def cent_to_euro(amount_cent):
    try:
        amount_cent = int(amount_cent)
        amount_euro = amount_cent / 100.0
        return round(amount_euro, 2)
    except ValueError:
        print("Invalid input. Please provide a valid integer value.")
        return None
