from MulLayer import *

apple =100
apple_num = 2
tax = 1.1

# layer
mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer() 

# forward
apple_price = mul_apple_layer.forward(apple,apple_num)
price = mul_tax_layer.forward(apple_price, tax)

print(price)
# backward 从右到左
dprice = 1
dapple_price, dtax = mul_tax_layer.backward(dprice) #只需要输入上一层流过来的数就行，xy保存在内部
dapple, dapple_num = mul_apple_layer.backward(dapple_price)

print(dapple, dapple_num, dtax,dapple_price)