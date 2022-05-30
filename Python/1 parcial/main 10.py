name=input('name:')
print('..................................')
p1=input('ingress the product:')
c1=int(input('ingres the cost:'))
p2=input('ingres the product:')
c2=int(input('ingres the cost: '))
p3=input('ingres the product:')
c3=int(input('ingress the cost:'))
p4=input('ingres the product:')
c4=int(input('ingress the cost:'))
p5=input('ingres the product:')
c5=int(input('ingress the cost:'))
print('..................................')

print("1.",p1,"$",c1)
print("2.",p2,"$", c2)
print("3.",p3, "$",c3)
print("4.",p4,"$",c4)
print("5.",p5,"$",c5)



totalcost=(c1+c2+c3+c4+c5)
print('your subtotal cost is:', totalcost)

iva=(totalcost*0.16)
print('your iva is:',iva)
print('your total cost with iva is:', totalcost+iva)