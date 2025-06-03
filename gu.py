odd = []
even = []
a = [even.append(i) if i%2 ==0 else odd.append(i) for i in range(1,10)] 
print(f"even: {even}")
print(f"odd: {odd}")