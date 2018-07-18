# Prints a list of list of strings and displays as an organized table.

def printTable( data ):

    colWidths = [0] * len(data)

    for l in range(len(data[0])):
        for i in range(len(data)):                
            if i == 0:
                try:
                    colWidths[i] = data[i][l]
                    print(colWidths[i].rjust(len(max(data[i], key=len))), end = ' ')
                except:
                    print(' '.rjust(len(max(data[i], key=len))), end = ' ')

            elif i < (len(data) - 1):
                    try:
                        colWidths[i] = data[i][l]
                        print(colWidths[i].center(len(max(data[i], key=len))), end = ' ')
                    except:
                        print(' '.center(len(max(data[i], key=len))), end = ' ')
  
            else:
                    try:
                        colWidths[i] = data[i][l]
                        print(colWidths[i].ljust(len(max(data[i], key=len))))
                    except:
                        print(' '.ljust(len(max(data[i], key=len))))



def main():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose'],
                 ['yes', 'no'],
                 ['potatos', 'carrots', 'beets', 'celery'],
                 ['boysenberries', 'stawberries', 'blueberries', 'blackberries'],
                 ['toyota', 'mitsubishi', 'nissan'],
                 ['Black', 'White', 'Yellow'],
                 ['Ybor', 'Dale Mabry', 'Brandon', 'South Shore'],
                 ['good']]

    tableData.sort(reverse=True, key=len)
    
    printTable( tableData )

    return
main()
