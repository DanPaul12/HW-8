

user_input = input("Enter the temperature in Celsius: ")

def temp_converter():
        try:
            num = float(user_input)
            converted_temp = round(((num - 32) * 5/9), 2)
        except ValueError:
            print("Please enter integers only")
        else:
            print(f"{user_input} degrees Farenheit is {converted_temp} degrees Celsius")
        finally:
            print("Thanks for using this application!")

temp_converter()