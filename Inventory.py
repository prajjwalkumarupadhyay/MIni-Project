def main():
    print('Enter the respective items you have in inventory')
    Inventory={'Arrow':'','Gold coin':'','Rope':'','Torch':'','Daggers':''}
    for i in Inventory:
        print(i,end=' ')
        Inventory[i]=int(input())
    print()
    print('Inventory:')
    count=0
    for j in Inventory:
        print(Inventory[j],j)
        count+=Inventory.get(j)
    print('\nTotal no of items: ',count)
main()