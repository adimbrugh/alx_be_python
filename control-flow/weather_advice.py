weather = input("what's the weather like to day? (sunny/rainy/cold):").lower()

if weather == "sunny":
    print('Wear a t-shirt and sunglasses.')

elif weather == "rainy":
    print("Don't forget your unbrella and raincoat.")

elif weather == "cold":
    print('Make sure to wear a warm coat and a scarf.')

else:
    print("Sorry, I dont't have recommendations for this weather.")