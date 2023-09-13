sai: str = 'hello'

print(f' {sai:10}: hai')
print(f' {sai:<10}')
print(f' {sai:>10}')
print(f' {sai:^10}')



number: float = 10000.12367

print(f'{number:.2f}') # printing 2 decimal numbers must keep dot(.)
print(f' {number:.3f}')  # printing 3 decimal numbers
print(f' {number:,.3f}')  # ,. is keeping the number in order