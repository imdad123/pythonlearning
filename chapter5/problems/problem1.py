dic_translation ={"name":"asam","age":"umur","city":"sehr","country":"mulk"}
print(dic_translation.keys())
user_input = input("Enter a word in above to get Translation : " )
print(f"Translation of {user_input} is : {dic_translation.get(user_input)}")