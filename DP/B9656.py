

n = int(input())

# moc = n // 3
# remainder = n % 3
sangkeun = 'SK'
moc, remainder = divmod(n,3)

if ((moc%2) == 1) :
    if remainder == 0 :
        print('CY')
    elif remainder == 1 :
        print('SK')
    else :
        print('CY')
else :
    if remainder == 0 :
        print('SK')
    elif remainder == 1 :
        print('CY')
    else :
        print('SK')

